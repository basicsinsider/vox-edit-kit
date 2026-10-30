"""ITU-R BS.1770-4 integrated loudness (LUFS) at 48 kHz, gated."""
import numpy as np
from scipy import signal

_B1 = [1.53512485958697, -2.69169618940638, 1.19839281085285]
_A1 = [1.0, -1.69065929318241, 0.73248077421585]
_B2 = [1.0, -2.0, 1.0]
_A2 = [1.0, -1.99004745483398, 0.99007225036621]


def integrated_lufs(x, sr=48000):
    x = np.asarray(x, float)
    if x.ndim == 1:
        x = x[:, None]
    y = signal.lfilter(_B2, _A2, signal.lfilter(_B1, _A1, x, axis=0), axis=0)
    blk, hop = int(0.4 * sr), int(0.1 * sr)
    if len(y) < blk:
        y = np.pad(y, ((0, blk - len(y)), (0, 0)))
    nb = 1 + (len(y) - blk) // hop
    z = np.array([np.mean(y[i * hop:i * hop + blk] ** 2, axis=0).sum() for i in range(nb)])
    lk = -0.691 + 10 * np.log10(z + 1e-20)
    z1 = z[lk > -70]
    if len(z1) == 0:
        return -70.0
    rel = -0.691 + 10 * np.log10(z1.mean()) - 10
    z2 = z1[(-0.691 + 10 * np.log10(z1 + 1e-20)) > rel]
    return float(-0.691 + 10 * np.log10(z2.mean()))
