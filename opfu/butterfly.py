from opfu.euro_option import EuroCall, EuroPut
from opfu.synthetic import Synthetic


class Butterfly(Synthetic):

    def __init__(self, K1, K3, T, price_1=0, price_2=0, price_3=0, S0=None, r=0.01, sigma=0.1, use_call=True):
        if use_call:
            Security = EuroCall
        else:
            Security = EuroPut

        K2 = (K1 + K3) / 2

        self.sec_1 = Security(K=K1, T=T, is_short=False, price=price_1, S0=S0, r=r, sigma=sigma)
        self.sec_2 = Security(K=K2, T=T, is_short=True, price=price_2, S0=S0, r=r, sigma=sigma)
        self.sec_3 = Security(K=K2, T=T, is_short=True, price=price_2, S0=S0, r=r, sigma=sigma)
        self.sec_4 = Security(K=K3, T=T, is_short=False, price=price_3, S0=S0, r=r, sigma=sigma)

        Synthetic.__init__(self, [self.sec_1, self.sec_2, self.sec_3, self.sec_4])
