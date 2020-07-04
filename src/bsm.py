# BSM Model

from math import sqrt

import numpy as np
from scipy.stats import norm


def N(x):
    return norm.cdf(x)


def d1(S0, K, r, sigma, T):
    return (np.log(S0 / K) + (r + sigma * sigma / 2) * T) / (sigma * sqrt(T))


def d2(S0, K, r, sigma, T):
    return d1(S0, K, r, sigma, T) - sigma * sqrt(T)


def bsm_call_price(S0, K, r=0.01, sigma=0.1, T=1):
    return S0 * N(d1(S0, K, r, sigma, T)) - K * np.exp(-r * T) * N(d2(S0, K, r, sigma, T))


def bsm_put_price(S0, K, r=0.01, sigma=0.1, T=1):
    return -S0 * N(-d1(S0, K, r, sigma, T)) + K * np.exp(-r * T) * N(-d2(S0, K, r, sigma, T))


def bsm_price(S0, K, r=0.01, sigma=0.1, T=1, is_call=True):
    if is_call:
        return bsm_call_price(S0, K, r, sigma, T)
    else:
        return bsm_put_price(S0, K, r, sigma, T)
