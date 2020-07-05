from math import sqrt, exp

from scipy.stats import norm

from opfu.bsm import N, bsm_price, d1, d2


def N_d(x):
    return norm.pdf(x)


def delta(S0, K, r=0.01, sigma=0.1, T=1, ds=0, is_call=True):
    if ds == 0:
        # the theortical result
        if is_call:
            return N(d1(S0, K, r, sigma, T))
        else:
            return N(d1(S0, K, r, sigma, T)) - 1
    # approach
    p = bsm_price(S0 + ds / 2, K, r, sigma, T, is_call)
    m = bsm_price(S0 - ds / 2, K, r, sigma, T, is_call)
    return (p - m) / ds


def gamma(S0, K, r=0.01, sigma=0.1, T=1, ds=0, is_call=True):
    if ds == 0:
        return N_d(d1(S0, K, r, sigma, T)) / (S0 * sigma * sqrt(T))
    # approach
    p = delta(S0 + ds / 2, K, r, sigma, T, ds, is_call)
    m = delta(S0 - ds / 2, K, r, sigma, T, ds, is_call)
    return (p - m) / ds


def theta(S0, K, r=0.01, sigma=0.1, T=1, dt=0, is_call=True):
    if dt == 0:
        return -S0 * N_d(d1(S0, K, r, sigma, T)) * sigma / (2 * sqrt(T)) - r * K * exp(-r * T) * N(
            d2(S0, K, r, sigma, T)) \
            if is_call else \
            -S0 * N_d(d1(S0, K, r, sigma, T)) * sigma / (2 * sqrt(T)) + r * K * exp(-r * T) * N(-d2(S0, K, r, sigma, T))
    # approach
    p = bsm_price(S0, K, r, sigma, T + dt / 2, is_call)
    m = bsm_price(S0, K, r, sigma, T - dt / 2, is_call)
    return -(p - m) / dt


def vega(S0, K, r=0.01, sigma=0.1, T=1, dsigma=0, is_call=True):
    if dsigma == 0:
        return S0 * sqrt(T) * N_d(d1(S0, K, r, sigma, T))
    # approach
    p = bsm_price(S0, K, r, sigma + dsigma / 2, T, is_call)
    m = bsm_price(S0, K, r, sigma - dsigma / 2, T, is_call)
    return (p - m) / dsigma


def rho(S0, K, r=0.01, sigma=0.1, T=1, dr=0, is_call=True):
    if dr == 0:
        return K * T * exp(-r * T) * N(d2(S0, K, r, sigma, T)) if is_call else -K * T * exp(-r * T) * N(
            -d2(S0, K, r, sigma, T))
    # approach
    p = bsm_price(S0, K, r + dr / 2, sigma, T, is_call)
    m = bsm_price(S0, K, r - dr / 2, sigma, T, is_call)
    return (p - m) / dr
