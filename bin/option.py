from bin.security import Security


class Option(Security):
    def __init__(self, K, T, is_short, price):
        # K is the strike price
        self.K = K
        # T is the time to mature, in year
        self.T = T
        # Check whether it is a short position
        Security.__init__(self, is_short, price)
