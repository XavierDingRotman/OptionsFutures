from src.security import Security
from src.stock import Stock
from src.euro_option import EuroCall, EuroPut
from math import inf
from datetime import datetime as dt
from src.ticker import get_option_info_from_ticker
from src.time import get_T

class Deal:
    def __init__(self, position, price, commission=0, ticker=None, timestamp=dt.today()):
        self.ticker=ticker
        self.position = position
        self.price = price
        self.contract_size = 1
        self.commission=commission
        self.timestamp=timestamp
        self.trading_volume = abs(self.position)
        self.is_short = self.position < 0
        self.security = Security(is_short=self.is_short, price=self.price)

    def payoff(self, p):
        return self.trading_volume * self.contract_size * self.security.payoff(p)

    def profit(self, p):
        return self.trading_volume * self.contract_size * self.security.profit(p) - self.commission

    def greek_letter(self, greek, dd=0, method="BSM"):
        return self.trading_volume * self.contract_size * self.security.greek_letter(greek, dd, method)


class DealEquity(Deal):
    def __init__(self, position, price, commission=0, ticker=None, timestamp=dt.today()):
        Deal.__init__(self, position, price, commission, ticker, timestamp)
        self.commission = self.commission * self.trading_volume
        self.contract_size = 1
        self.security = Stock(S=price, T=inf, is_short=self.is_short)


class DealEuroCall(Deal):
    def __init__(self, position, price, K, T=None, S0=None, r=0.01, sigma=0.1, commission=0, ticker=None, timestamp=dt.today(),
                 time_mature=None, ticker_underlying=None):
        Deal.__init__(self, position, price, commission, ticker, timestamp)
        self.time_mature=time_mature
        self.contract_size = 100
        self.ticker_underlying = ticker_underlying
        self.security = EuroCall(K=K, T=T, is_short=self.is_short, price=self.price, S0=S0, r=r, sigma=sigma)


class DealEuroPut(Deal):
    def __init__(self, position, price, K, T=None, S0=None, r=0.01, sigma=0.1, commission=0, ticker=None, timestamp=dt.today(),
                 time_mature=None, ticker_underlying=None):
        Deal.__init__(self, position, price, commission, ticker, timestamp)
        self.time_mature = time_mature
        self.contract_size = 100
        self.ticker_underlying = ticker_underlying
        self.security = EuroPut(K=K, T=T, is_short=self.is_short, price=price, S0=S0, r=r, sigma=sigma)


def get_deal_from_ticker(ticker, position, price, S0 = None, r=0.01, sigma=0.1, comission=0, timestamp=dt.today()):
    asset, is_call, month, day, year, K, country = get_option_info_from_ticker(ticker)
    time_mature = dt(year, month, day)
    T = get_T(timestamp, time_mature)
    ticker_underlying = asset
    DealOption = DealEuroCall if is_call else DealEuroPut
    return DealOption(position, price, K, T, S0, r, sigma, comission,
                      ticker, timestamp, time_mature, ticker_underlying)