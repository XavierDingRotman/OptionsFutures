import matplotlib.pyplot as plt


class Security():
    def __init__(self, is_short, price=0):
        self.is_short = is_short
        self.price = -price if self.is_short else price

    def payoff(self, P):
        # P is mature price
        if self.is_short:
            return -self.payoff_long(P)
        return self.payoff_long(P)

    def payoff_long(self, P):
        raise NotImplementedError

    def profit(self, P):
        return self.payoff(P) - self.price

    def graph_payoff(self, start, end, num=100):
        x = np.linspace(start, end, num)
        y = [self.payoff(x_i) for x_i in x]
        plt.plot(x, y)

    def graph_profit(self, start, end, num=100):
        x = np.linspace(start, end, num)
        y = [self.profit(x_i) for x_i in x]
        plt.plot(x, y)
        plt.axhline(y=0, color='r', linestyle='-')
        plt.show()
