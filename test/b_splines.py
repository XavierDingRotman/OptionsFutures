import matplotlib.pyplot as plt
import numpy as np

from opfu.b_splines import BSplines

if __name__ == '__main__':
    t = np.linspace(0, 1, 101)
    t_grids = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    f_grids = np.repeat(1, len(t_grids))
    bsplines = BSplines(t_grids)

    # d == 1
    func_b = bsplines.basis_function(k=5, d=1)
    y = [func_b(tx) for tx in t]
    plt.plot(t, y)
    plt.show()

    # d == 2
    func_b = bsplines.basis_function(k=5, d=2)
    y = [func_b(tx) for tx in t]
    plt.plot(t, y)
    plt.show()

    # d == 3
    func_b = bsplines.basis_function(k=5, d=3)
    y = [func_b(tx) for tx in t]
    plt.plot(t, y)
    plt.show()

    # test f
    func_f = bsplines.func(d=1, f_grids=np.repeat(1, len(t_grids) - 2))
    y = [func_f(tx) for tx in t]
    plt.plot(t, y)
    plt.show()

    # test f
    func_f = bsplines.func(d=2, f_grids=np.repeat(1, len(t_grids) - 3))
    y = [func_f(tx) for tx in t]
    plt.plot(t, y)
    plt.show()

    # test f
    func_f = bsplines.func(d=3, f_grids=np.repeat(1, len(t_grids) - 4))
    y = [func_f(tx) for tx in t]
    plt.plot(t, y)
    plt.show()
