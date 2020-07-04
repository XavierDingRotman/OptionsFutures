from bin.euro_option import EuroCall, EuroPut
from bin.portfolio import Portfolio


class Butterfly(Portfolio):

    def __init__(self, K1, K3, T, price_1=0, price_2=0, price_3=0, S0=None, r=0.01, sigma=0.1, use_call=True):
        if use_call:
            Security = EuroCall
        else:
            Security = EuroPut

        K2 = (K1 + K3) / 2

        sec_1 = Security(K=K1, T=T, is_short=False, price=price_1, S0=S0, r=r, sigma=sigma)
        sec_2 = Security(K=K2, T=T, is_short=True, price=price_2, S0=S0, r=r, sigma=sigma)
        sec_3 = Security(K=K2, T=T, is_short=True, price=price_2, S0=S0, r=r, sigma=sigma)
        sec_4 = Security(K=K3, T=T, is_short=False, price=price_3, S0=S0, r=r, sigma=sigma)

        Portfolio.__init__(self, [sec_1, sec_2, sec_3, sec_4])
