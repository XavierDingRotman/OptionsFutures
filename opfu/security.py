import matplotlib.pyplot as plt
import numpy as np

from opfu.binary_search import binary_search


class Security(object):

    def __init__(self, is_short, price=0, name="Unnamed security", market_price=None):
        self.is_short = is_short
        self.price = price
        self.sign = -1 if is_short else 1
        self.name = name
        self.market_price = self.price if market_price is None else market_price

    def cost(self):
        return self.sign * self.price

    def market_profit(self):
        return 0 if self.market_price == None else self.market_price

    def payoff(self, P):
        # P is mature price
        if self.is_short:
            return -self.payoff_long(P)
        return self.payoff_long(P)

    def payoff_long(self, P):
        raise NotImplementedError

    def profit(self, P):
        return self.payoff(P) - (self.price if not self.is_short else - self.price)

    def graph_payoff(self, start=0, end=100, num=100):
        x = np.linspace(start, end, num)
        y = [self.payoff(x_i) for x_i in x]
        plt.plot(x, y, label="payoff")
        plt.axhline(y=0, color='r', linestyle='--')
        plt.legend()
        plt.show()

    def graph_profit(self, start=0, end=100, num=100):
        x = np.linspace(start, end, num)
        y = [self.profit(x_i) for x_i in x]
        plt.plot(x, y, label="profit")
        plt.axhline(y=0, color='r', linestyle='--')
        plt.legend()
        plt.show()

    def greek_letter(self, greek, dd=0, method="BSM"):
        raise NotImplementedError

    def find_break_even(self, start=0, end=1000, num=100, tol=1e-5, max_iter=1000):
        x = np.linspace(start, end, num)
        y = [self.profit(x_i) for x_i in x]
        result = []
        for i in range(0, num - 1):
            if y[i] * y[i + 1] < 0:
                result.append(binary_search(x[i], x[i + 1], func=self.profit, max_iter=max_iter, tol=tol))
        return result

    def find_break_even_payoff(self, start=0, end=1000, num=100, tol=1e-5, max_iter=1000):
        x = np.linspace(start, end, num)
        y = [self.payoff(x_i) for x_i in x]
        result = []
        for i in range(0, num - 1):
            if y[i] * y[i + 1] < 0:
                result.append(binary_search(x[i], x[i + 1], func=self.payoff, max_iter=max_iter, tol=tol))
        return result

    def report(self, underlying_current_price=None, start=0, end=100, num=100, max_iter=1000, tol=1e-5,
               report_greek=True, report_market_profit=True):
        self.graph_payoff(start=start, end=end, num=num)
        self.graph_profit(start=start, end=end, num=num)
        print('Report for : {}'.format(self.name))
        print('Totol cost : {}'.format(self.cost()))
        print('Breakeven : {}'.format(self.find_break_even(start=start, end=end, max_iter=max_iter, tol=tol)))
        print('Current underlying price : {}'.format(underlying_current_price))
        if report_greek:
            for greek in ['delta', 'gamma', 'theta', 'vega', 'rho']:
                print('{} : {}'.format(greek, self.greek_letter(greek)))
        if report_market_profit:
            print('Deal Profit : {}'.format(self.market_profit()))
