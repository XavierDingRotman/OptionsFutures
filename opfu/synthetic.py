import matplotlib.pyplot as plt
import numpy as np

from opfu.euro_option import EuroCall, EuroPut
from opfu.security import Security
from opfu.stock import Stock


class Synthetic(Security):
    def __init__(self, securities, is_short=False):
        self.securities = securities
        self.is_short = is_short
        self.sign = -1 if self.is_short else 1
        Security.__init__(self, is_short=is_short, price=self.get_price())

    def get_price(self):
        result = 0
        for security in self.securities:
            result += self.sign * security.price
        return result

    def payoff(self, P):
        result = 0
        for security in self.securities:
            result += self.sign * security.payoff(P)
        return result

    def profit(self, P):
        result = 0
        for security in self.securities:
            result += self.sign * security.profit(P)
        return result

    def graph_payoff(self, start=0, end=None, num=100):
        if end == None:
            end = 1000
        x = np.linspace(start, end, num)
        y = [self.payoff(x_i) for x_i in x]
        plt.plot(x, y, label="payoff")
        plt.legend()
        plt.show()

    def graph_profit(self, start=0, end=None, num=100):
        if end == None:
            end = 1000
        x = np.linspace(start, end, num)
        y = [self.profit(x_i) for x_i in x]
        plt.plot(x, y, label="profit")
        plt.legend()
        plt.show()


class CoveredCall(Synthetic):
    def __init__(self, K, T, is_short, price=0, S0=None, r=0.01, sigma=0.1):
        securities = [EuroCall(K, T, True, price, S0, r, sigma), Stock(S0, T, is_short=False)]
        Synthetic.__init__(self, securities, is_short)


class ProtectivePut(Synthetic):
    def __init__(self, K, T, is_short, price=0, S0=None, r=0.01, sigma=0.1):
        securities = [EuroPut(K, T, False, price, S0, r, sigma), Stock(S0, T, is_short=False)]
        Synthetic.__init__(self, securities, is_short)
