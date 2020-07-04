from bin.security import Security


class Option(Security):
    def __init__(self, K, T, is_short, price, S0=None, r=0.01, sigma=0.1):
        # K is the strike price
        self.K = K
        # T is the time to mature, in year
        self.T = T
        # Check whether it is a short position
        Security.__init__(self, is_short, price)
        self.S0 = S0
        self.r = r
        self.sigma = sigma
