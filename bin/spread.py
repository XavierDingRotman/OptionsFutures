from bin.euro_option import EuroCall, EuroPut
from bin.portfolio import Portfolio


class BullSpread(Portfolio):

    def __init__(self, K1, K2, T, price_1=0, price_2=0, S0=None, r=0.01, sigma=0.1, use_call=True):
        if use_call:
            security_1 = EuroCall(K1, T, is_short=False, price=price_1, S0=S0, r=r, sigma=sigma)
            security_2 = EuroCall(K2, T, is_short=True, price=price_2, S0=S0, r=r, sigma=sigma)
        else:
            security_1 = EuroPut(K1, T, is_short=False, price=price_1, S0=S0, r=r, sigma=sigma)
            security_2 = EuroPut(K2, T, is_short=True, price=price_2, S0=S0, r=r, sigma=sigma)
        Portfolio.__init__(self, [security_1, security_2])


class BearSpread(Portfolio):

    def __init__(self, K1, K2, T, price_1=0, price_2=0, S0=None, r=0.01, sigma=0.1, use_call=True):
        if use_call:
            security_1 = EuroCall(K1, T, is_short=True, price=price_1, S0=S0, r=r, sigma=sigma)
            security_2 = EuroCall(K2, T, is_short=False, price=price_2, S0=S0, r=r, sigma=sigma)
        else:
            security_1 = EuroPut(K1, T, is_short=True, price=price_1, S0=S0, r=r, sigma=sigma)
            security_2 = EuroPut(K2, T, is_short=False, price=price_2, S0=S0, r=r, sigma=sigma)
        Portfolio.__init__(self, [security_1, security_2])
