from opfu.security import Security


class Stock(Security):
    def __init__(self, S, T, is_short=False):
        self.S = S
        self.K = self.S
        self.T = T
        Security.__init__(self, is_short, price=0)

    def payoff_long(self, P):
        return P - self.S

    def graph_payoff(self, start=0, end=None, num=100):
        if end == None:
            end = self.S * 2
        Security.graph_payoff(self, start, end, num)

    def get_bsm_price(self):
        return self.S

    def greek_letter(self, greek, dd=0, method="BSM"):
        if greek == "delta":
            return 1
        if greek == "gamma":
            return 0
        return 0
