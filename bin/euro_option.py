from bin.bsm import bsm_call_price, bsm_put_price
from bin.bsm_greek import delta, gamma, theta, vega, rho
from bin.error import InputError
from bin.option import Option
from bin.security import Security


class EuroOption(Option):
    def __init__(self, K, T, is_short, price=0, S0=None, r=0.01, sigma=0.1):
        Option.__init__(self, K, T, is_short, price, S0, r, sigma)

    def graph_payoff(self, start=0, end=None, num=100):
        if end == None:
            end = self.K * 2
        Security.graph_payoff(self, start, end, num)

    def greek_letter_base(self, greek, is_call, dd=0, method="BSM"):
        sign = -1 if self.is_short else 1
        if self.S0 == None:
            raise InputError("Error", "Error Input of S0")
        if method == "BSM":
            if greek == "delta":
                return sign * delta(self.S0, self.K, self.r, self.sigma, self.T, dd, is_call)
            if greek == "gamma":
                return gamma(self.S0, self.K, self.r, self.sigma, self.T, dd, is_call)
            if greek == "theta":
                return sign * theta(self.S0, self.K, self.r, self.sigma, self.T, dd, is_call)
            if greek == "vega":
                return sign * vega(self.S0, self.K, self.r, self.sigma, self.T, dd, is_call)
            if greek == "rho":
                return sign * rho(self.S0, self.K, self.r, self.sigma, self.T, dd, is_call)
        else:
            raise NotImplementedError


class EuroCall(EuroOption):
    # Engine of pricing EuroCall option
    def __init__(self, K, T, is_short=False, price=0, S0=None, r=0.01, sigma=0.1):
        if price == "BSM":
            if S0 == None:
                print("Missing S0")
                raise Exception()
            self.price = bsm_call_price(S0, K, r, sigma, T)
            price = self.price
        EuroOption.__init__(self, K, T, is_short, price, S0, r, sigma)

    def payoff_long(self, P):
        return 0 if P < self.K else P - self.K

    def greek_letter(self, greek, dd=0, method="BSM"):
        is_call = True
        return EuroOption.greek_letter_base(self, greek, is_call, dd, method)


class EuroPut(EuroOption):
    # Engine of pricing EuroPut option
    def __init__(self, K, T, is_short=False, price=0, S0=None, r=0.01, sigma=0.1):
        if price == "BSM":
            if S0 == None:
                print("Missing S0")
                raise Exception()
            self.price = bsm_put_price(S0, K, r, sigma, T)
            price = self.price
        EuroOption.__init__(self, K, T, is_short, price, S0, r, sigma)

    def payoff_long(self, P):
        return self.K - P if P < self.K else 0

    def greek_letter(self, greek, dd=0, method="BSM"):
        is_call = False
        return EuroOption.greek_letter_base(self, greek, is_call, dd, method)
