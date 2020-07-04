from bin.deal import get_deal_from_ticker
from datetime import datetime as dt

if __name__ == '__main__':
    ticker = "XPOG172008500.U"
    deal = get_deal_from_ticker(ticker,
                         position=-100,
                         vwap=2.5,
                         S0 = None,
                         r=0.01,
                         sigma=0.1,
                         comission=0.1839,
                         timestamp=dt(year=2020, month=6, day=19))
    print(deal)
