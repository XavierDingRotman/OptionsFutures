import matplotlib.pyplot as plt
import numpy as np


class Portfolio:
    def __init__(self, securities):
        self.securities = securities

    def payoff(self, P):
        result = 0
        for security in self.securities:
            result += security.payoff(P)
        return result

    def profit(self, P):
        result = 0
        for security in self.securities:
            result += security.profit(P)
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
