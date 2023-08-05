import datetime
import time

import torch
from lion_pytorch import Lion
from matplotlib import pyplot as plt
from torch import jit
from torch import nn
from torch.backends import cuda, cudnn

import optim

torch._C._set_cublas_allow_tf32(True)
torch.use_deterministic_algorithms(False)
cudnn.enabled = True
cudnn.benchmark = True
cudnn.deterministic = False
cudnn.allow_tf32 = True
cuda.matmul.allow_tf32 = True
jit.optimized_execution(True)
jit.fuser("fuser2")

wd = 1e-2
numbers = 1
features = 2 ** 5
depth = 1
input_scale = 1
lr = 1e-6
iterations = 2 ** 24
noise_scale_range = list(range(-12, -13, -1))
batch_size = 2 ** 8
offset = 2048 * 15
printervall = 2048 * 16


def p(*shape):
    a = torch.randn(shape) / (1 if len(shape) == 1 else shape[0] ** 0.5)
    return [nn.Parameter(a.detach().clone().contiguous().requires_grad_(True)) for _ in range(6)]


class MultiModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.p0 = p(numbers, features)
        self.p00 = p(features)
        self.p1 = p(features, features)
        self.p10 = p(features)
        self.p2 = p(features, numbers)
        self.p20 = p(features)
        for i, v in enumerate(self.p0 + self.p00 + self.p1 + self.p10 + self.p2 + self.p20):
            setattr(self, f"_param_for_model{i}", v)

    def forward(self, inp):
        out = torch.einsum("bn,gnf->bgf", inp, torch.stack(self.p0)) + torch.stack(self.p00).unsqueeze(0)

        out = torch.nn.functional.leaky_relu(out, inplace=True)
        out = torch.einsum("bgn,gnf->bgf", out / out.norm(p=2, dim=-1, keepdim=True).clamp(min=1e-8),
                           torch.stack(self.p1)) + torch.stack(self.p10).unsqueeze(0)

        out = torch.nn.functional.leaky_relu(out, inplace=True)
        out = torch.einsum("bgn,gnf->bgf", out / out.norm(p=2, dim=-1, keepdim=True).clamp(min=1e-8),
                           torch.stack(self.p2)) + torch.stack(self.p20).unsqueeze(0)

        return out


plt.yscale("log")
plt.xscale("log")
start_time = datetime.datetime.now()
colors = [lambda x: f"#{x:02x}0000", lambda x: f"#00{x:02x}00", lambda x: f"#0000{x:02x}",
          lambda x: f"#{x:02x}{x:02x}00", lambda x: f"#{x:02x}00{x:02x}", lambda x: f"#00{x:02x}{x:02x}"]

noise_scale = None


def get_noise():
    inp = torch.randn((batch_size, numbers), device="cuda:0") * input_scale
    noise = torch.randn_like(inp) * inp.std() * noise_scale
    return inp, noise


def noisy_square():
    inp, noise = get_noise()
    target = (noise + inp.square())
    ground_truth = inp.square()
    return inp, target, ground_truth


def rosenbrock(x, y):
    return (1 - x).square() + 100 * (y - x.square()).square()


def noisy_rosenbrock():
    inp, noise = get_noise()
    target = rosenbrock(*(inp + noise).chunk(2, 1))
    ground_truth = rosenbrock(*inp.chunk(2, 1))
    return inp, target, ground_truth


example = noisy_square

oo = []

for sc_idx, scale in enumerate(noise_scale_range):
    noise_scale = 2 ** scale
    all_losses = torch.zeros((iterations, 6))
    loss_group = []

    mod = MultiModel().cuda()
    ps = list(zip(mod.p0, mod.p00, mod.p1, mod.p10, mod.p2, mod.p20))
    oo = [torch.optim.AdamW(ps[0], lr=lr, weight_decay=wd),
          optim.Graft(ps[1], torch.optim.Adam(ps[1], lr=lr), Lion(ps[1], lr=1), weight_decay=wd * lr),
          optim.Graft(ps[2], torch.optim.Adam(ps[2], lr=lr), torch.optim.SGD(ps[2], lr=1), weight_decay=wd * lr),
          optim.Graft(ps[3], torch.optim.SGD(ps[3], lr=lr), torch.optim.Adam(ps[3], lr=1), weight_decay=wd * lr),
          optim.Sign(ps[4], torch.optim.Adam(ps[4], lr=lr), lr, weight_decay=wd * lr, graft_to_self=False),
          optim.Sign(ps[5], torch.optim.Adam(ps[5], lr=lr), weight_decay=wd * lr)]

    oo = [optim.OptimizerOptimizer(p, o) for p, o in zip(ps, oo)]
    start_ts = time.time()

    for i in range(iterations):
        inp, target, ground_truth = example()
        if i == 0:
            mod = torch.jit.script(mod, inp)
        target = target.mean(-1, keepdim=True).unsqueeze(1)
        ground_truth = ground_truth.mean(-1, keepdim=True).unsqueeze(1)

        out = mod(inp)
        (6 * (out - target).abs()).mean().backward()
        for o in oo:
            o.step()
        mod.zero_grad()
        with torch.no_grad():
            loss_group.append((out - ground_truth).abs().mean((0, 2)).detach().to(device="cpu", non_blocking=True))
        if i % printervall == offset and i > printervall:
            all_losses[i - printervall - offset:i - offset] = torch.stack(loss_group[:printervall])
            loss_group = loss_group[printervall:]
            it = i / (time.time() - start_ts)
            eta = datetime.datetime.now() + datetime.timedelta(
                seconds=int((iterations * (len(noise_scale_range) - sc_idx) - i) / it))
            print(
                f'{sc_idx} | {i:06d} | {datetime.datetime.now() - start_time} | {datetime.datetime.now()} | ETA: {eta} | {it:.1f} it/s | {" - ".join(f"{o.item():9.7f}" for o in all_losses[i - printervall - offset:i - offset].mean(0))}')

    all_losses = [[i.item() for i in losses] for losses in all_losses]
    skipped = len(all_losses) // 32
    for i, (name, ls) in enumerate(
            zip(["Adam#Adam", "Adam#Lion", "Adam#SGD", "SGD#Adam", "SGD#SignAdam", "Adam#SignAdam"], zip(*all_losses))):
        color = colors[i](round(255 - 128 * sc_idx / len(noise_scale_range)))
        plt.plot(list(range(skipped, len(ls))), [sum(ls[i:i + skipped]) / skipped for i in range(len(ls) - skipped)],
                 color=color, label=f"{name} - noise_scale=2**{scale}")
plt.legend()
plt.show()
