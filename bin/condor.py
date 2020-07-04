from bin.error import InputError
from bin.euro_option import EuroCall, EuroPut
from bin.portfolio import Portfolio


class Condor(Portfolio):

    def __init__(self, K1, K2, K3, K4, T, price_1=0, price_2=0, price_3=0, price_4=0, S0=None, r=0.01, sigma=0.1,
                 use_call=True):
        if use_call:
            Security = EuroCall
        else:
            Security = EuroPut

        if K1 > K2:
            raise InputError(message="Error", expression="K1 must be smaller than K2")

        if K2 > K3:
            raise InputError(message="Error", expression="K2 must be smaller than K3")

        if K3 > K4:
            raise InputError(message="Error", expression="K3 must be smaller than K4")

        self.sec_1 = Security(K=K1, T=T, is_short=False, price=price_1, S0=S0, r=r, sigma=sigma)
        self.sec_2 = Security(K=K2, T=T, is_short=True, price=price_2, S0=S0, r=r, sigma=sigma)
        self.sec_3 = Security(K=K3, T=T, is_short=True, price=price_3, S0=S0, r=r, sigma=sigma)
        self.sec_4 = Security(K=K4, T=T, is_short=False, price=price_4, S0=S0, r=r, sigma=sigma)

        Portfolio.__init__(self, [self.sec_1, self.sec_2, self.sec_3, self.sec_4])
