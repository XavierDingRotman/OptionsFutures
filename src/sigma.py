import numpy as np
from math import sqrt


def est_sigma(hist, tau="day"):
    if tau == "day":
        tau = 1 / 252


    n = len(hist) - 1

    u = np.log(hist[1:n + 1] / hist[0:n])

    s = np.std(u) * sqrt(n) / sqrt(n - 1)

    sigma = s / sqrt(tau)

    return sigma