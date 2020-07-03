from bin.bsm import bsm_call_price, bsm_put_price
from bin.option import Option
from bin.security import Security


class EuroOption(Option):
    def __init__(self, K, T, is_short, price=0):
        Option.__init__(self, K, T, is_short, price)

    def graph_payoff(self, start=0, end=None, num=100):
        if end == None:
            end = self.K * 2
        Security.graph_payoff(self, start, end, num)


class EuroCall(EuroOption):
    # Engine of pricing EuroCall option
    def __init__(self, K, T, is_short=False, price=0, S0=None, r=0.01, sigma=0.1):
        if price == "BSM":
            if S0 == None:
                print("Missing S0")
                raise Exception()
            self.price = bsm_call_price(S0, K, r, sigma, T)
            price = self.price
        EuroOption.__init__(self, K, T, is_short, price)

    def payoff_long(self, P):
        return 0 if P < self.K else P - self.K


class EuroPut(EuroOption):
    # Engine of pricing EuroPut option
    def __init__(self, K, T, is_short=False, price=0, S0=None, r=0.01, sigma=0.1):
        if price == "BSM":
            if S0 == None:
                print("Missing S0")
                raise Exception()
            self.price = bsm_put_price(S0, K, r, sigma, T)
            price = self.price
        EuroOption.__init__(self, K, T, is_short, price)

    def payoff_long(self, P):
        return self.K - P if P < self.K else 0
