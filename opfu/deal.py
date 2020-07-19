from datetime import datetime as dt
from math import inf

from opfu.euro_option import EuroCall, EuroPut
from opfu.security import Security
from opfu.stock import Stock
from opfu.ticker import get_option_info_from_ticker
from opfu.time import get_T


class Deal(Security):
    def __init__(self, position, price, commission=0, ticker=None, timestamp=dt.today(), market_date=dt.today(),
                 market_price=None):
        self.ticker = ticker
        self.position = position
        self.price = price
        self.contract_size = 1
        self.commission = commission
        self.timestamp = timestamp
        self.trading_volume = abs(self.position)
        self.is_short = self.position < 0
        self.security = Security(is_short=self.is_short, price=self.price)
        self.market_date = market_date
        self.market_price = self.price if market_price is None else market_price
        Security.__init__(self, self.is_short, self.price)

    def cost(self):
        return self.price * self.position

    def payoff(self, p):
        return self.trading_volume * self.contract_size * self.security.payoff(p)

    def profit(self, p):
        return self.trading_volume * self.contract_size * self.security.profit(p) - self.commission

    def greek_letter(self, greek, dd=0, method="BSM"):
        return self.trading_volume * self.contract_size * self.security.greek_letter(greek, dd, method)

    def market_profit(self):
        sign = -1 if self.is_short else 1
        return self.trading_volume * sign * (self.market_price - self.price)

    def est_market_price(self, method="BSM"):
        raise NotImplementedError


class DealEquity(Deal):
    def __init__(self, position, price, commission=0, ticker=None, timestamp=dt.today(), market_date=dt.today(),
                 market_price=None):
        Deal.__init__(self, position, price, commission, ticker, timestamp, market_date, market_price)
        self.commission = self.commission * self.trading_volume
        self.contract_size = 1
        self.security = Stock(S=price, T=inf, is_short=self.is_short)

    def est_market_price(self, method="BSM"):
        return self.market_price


class DealEuroCall(Deal):
    def __init__(self, position, price, K, T=None, S0=None, r=0.01, sigma=0.1, commission=0, ticker=None, timestamp=dt.today(),
                 time_mature=None, ticker_underlying=None, market_date=dt.today(), market_price=None):
        Deal.__init__(self, position, price, commission, ticker, timestamp, market_date, market_price)
        self.time_mature=time_mature
        self.contract_size = 100
        self.ticker_underlying = ticker_underlying
        self.security = EuroCall(K=K, T=T, is_short=self.is_short, price=self.price, S0=S0, r=r, sigma=sigma)

    def est_market_price(self, method="BSM"):
        temp = EuroCall(K=self.security.K, T=get_T(self.market_date, self.time_mature), is_short=self.security.is_short,
                        price=method, S0=self.security.S0, r=self.security.r, sigma=self.security.sigma)
        return temp.price


class DealEuroPut(Deal):
    def __init__(self, position, price, K, T=None, S0=None, r=0.01, sigma=0.1, commission=0, ticker=None, timestamp=dt.today(),
                 time_mature=None, ticker_underlying=None, market_date=dt.today(), market_price=None):
        Deal.__init__(self, position, price, commission, ticker, timestamp, market_date, market_price)
        self.time_mature = time_mature
        self.contract_size = 100
        self.ticker_underlying = ticker_underlying
        self.security = EuroPut(K=K, T=T, is_short=self.is_short, price=price, S0=S0, r=r, sigma=sigma)

    def est_market_price(self, method="BSM"):
        temp = EuroPut(K=self.security.K, T=get_T(self.market_date, self.time_mature), is_short=self.security.is_short,
                       price=method, S0=self.security.S0, r=self.security.r, sigma=self.security.sigma)
        return temp.price


def get_deal_from_ticker(ticker, position, price, S0=None, r=0.01, sigma=0.1, comission=0, timestamp=dt.today(),
                         market_date=dt.today(), market_price=None, equity_length=3):
    asset, is_call, month, day, year, K, country = get_option_info_from_ticker(ticker, equity_length)
    time_mature = dt(year, month, day)
    T = get_T(timestamp, time_mature)
    ticker_underlying = asset
    DealOption = DealEuroCall if is_call else DealEuroPut
    return DealOption(position, price, K, T, S0, r, sigma, comission,
                      ticker, timestamp, time_mature, ticker_underlying, market_date, market_price)
