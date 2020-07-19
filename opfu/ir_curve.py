import matplotlib.pyplot as plt
import numpy as np

from opfu.b_splines import BSplines


class IRCurve(object):
    def __init__(self, t, f, is_last_mature=True):
        #  index of t : 0 , 1,  2,  3, ..., N+2, N+3, (N+4, N+5, N+6, N+7)
        #  math index : -3, -2, -1, 0, ..., N-1, N,   N+1, N+2, N+3, N+4
        if len(t) != len(f):
            raise AttributeError
        # you need to sort them
        if np.any(t[:-1] > t[1:]):
            raise AttributeError
        if is_last_mature:
            t = np.append(t, [t[len(t) - 1] + 0.25, t[len(t) - 1] + 0.5, t[len(t) - 1] + 1, t[len(t) - 1] + 1.25])
        else:
            f = f[0:(len(t) - 4)]
        self.d = 3
        self.t = t
        self.N = len(self.t) - 8
        self.settle = self.t[3]
        self.mature = self.t[self.N + 3]
        self.f = f
        self.bsplinees = BSplines(t_grids=self.t)

    def get_func(self):
        return self.bsplinees.func(d=3, f_grids=self.f)

    def plot(self):
        t = np.linspace(self.settle, self.mature, 100)
        y = [self.get_func()(tt) for tt in t]
        plt.plot(t, y)
        plt.show()
