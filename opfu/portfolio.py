from opfu.security import Security


class Portfolio(Security):
    def __init__(self, deals, is_short=False):
        self.deals = deals
        Security.__init__(self, is_short, self.cost())

    def cost(self):
        result = 0
        for deal in self.deals:
            result += deal.cost()
        return result

    def payoff(self, p):
        result = 0
        for deal in self.deals:
            result += deal.payoff(p)
        return result

    def profit(self, p):
        result = 0
        for deal in self.deals:
            result += deal.profit(p)
        return result

    # def graph_payoff(self, start=0, end=None, num=100):
    #     if end == None:
    #         end = 1000
    #     x = np.linspace(start, end, num)
    #     y = [self.payoff(x_i) for x_i in x]
    #     plt.plot(x, y, label="payoff")
    #     plt.legend()
    #     plt.show()

    # def graph_profit(self, start=0, end=None, num=100):
    #     if end == None:
    #         end = 1000
    #     x = np.linspace(start, end, num)
    #     y = [self.profit(x_i) for x_i in x]
    #     plt.plot(x, y, label="profit")
    #     plt.legend()
    #     plt.show()

    def greek_letter(self, greek, dd=0, method="BSM"):
        result = 0
        for deal in self.deals:
            ddd = dd
            if isinstance(dd, dict):
                ddd = dd[greek]
            result += deal.greek_letter(greek, ddd, method)
        return result

    # def find_break_even(self, start=0, end=1000, num=100, tol=1e-5, max_iter=1000):
    #     x = np.linspace(start, end, num)
    #     y = [self.profit(x_i) for x_i in x]
    #     result = []
    #     for i in range(0, num - 1):
    #         if y[i] * y[i + 1] < 0:
    #             result.append(binary_search(x[i], x[i + 1], func=self.profit, max_iter=max_iter, tol=tol))
    #     return result

    def market_profit(self):
        result = 0
        for deal in self.deals:
            result += deal.market_profit()
        return result
