from datetime import datetime as dt

import pandas as pd
import yfinance as yf
from yahoo_fin import stock_info as si

from opfu.deal import get_deal_from_ticker, DealEquity
from opfu.portfolio import Portfolio
from opfu.sigma import est_sigma

if __name__ == '__main__':
    market_date = dt(2020, 7, 3)
    r = 0.68 / 100
    # sigma = est_sigma(pd.read_csv("Data/XPO.csv")['Close'].to_numpy(), "day")
    sigma = est_sigma(yf.Ticker('XPO').history(period='5y')['Close'].to_numpy(), "day")
    xpo = DealEquity(position=500, price=74, commission=0.0073, ticker="XPO", timestamp=dt(2020, 6, 26),
                     market_date=market_date, market_price=0.55)
    S0 = 79.18
    xpo_call_1 = get_deal_from_ticker("XPOG172008500.U", position=-100, price=2.5, S0=S0,
                                      r=r, sigma=sigma, comission=0.1839, timestamp=dt(2020, 6, 19),
                                      market_date=market_date, market_price=0.55)
    xpo_call_1.name = "XPO Short Call"
    xpo_call_2 = get_deal_from_ticker("XPOG172008750.U", position=100, price=2.1, S0=S0,
                                      r=r, sigma=sigma, comission=0.1839, timestamp=dt(2020, 6, 19),
                                      market_date=market_date, market_price=0.25)
    xpo_call_2.name = "XPO Long Call"
    xpo_put_1 = get_deal_from_ticker("XPOS172007000.U", position=100, price=1.85, S0=S0,
                                     r=r, sigma=sigma, comission=0.1839, timestamp=dt(2020, 6, 19),
                                     market_date=market_date, market_price=0.50)
    xpo_put_1.name = "XPO Long Put"
    xpo_put_2 = get_deal_from_ticker("XPOS172007500.U", position=-100, price=3, S0=S0,
                                     r=r, sigma=sigma, comission=0.1839, timestamp=dt(2020, 6, 19),
                                     market_date=market_date, market_price=2.55)
    xpo_put_2.name = "XPO Short Put"

    xpo_current_price = si.get_live_price('XPO')

    deal_combo_1 = Portfolio([xpo_call_1, xpo_call_2, xpo_put_1, xpo_put_2])
    deal_combo_1.name = "Combination without equity"
    deal_combo_1.report(xpo_current_price, start=40, end=120)

    deal_combo_2 = Portfolio([xpo, xpo_call_1, xpo_call_2, xpo_put_1, xpo_put_2])
    deal_combo_2.name = "Combination with equity"
    deal_combo_2.report(xpo_current_price, start=40, end=120)

    dict_deals = {}
    for deal in [xpo_call_1, xpo_call_2, xpo_put_1, xpo_put_2]:
        dict_deals.update({deal.name: {"position": deal.position,
                                       "price": deal.price,
                                       "BSM price": deal.security.get_bsm_price(),
                                       "Recommended Position": "Short" if deal.price > deal.security.get_bsm_price() else "Long"}})
    pd.DataFrame(dict_deals)

    dict_deals = {}
    for deal in [xpo_call_1, xpo_call_2, xpo_put_1, xpo_put_2]:
        dict_deals.update({deal.name: {"position": deal.position,
                                       "market price": deal.market_price,
                                       "Est. market price": deal.est_market_price(),
                                       "Recommended Position": "Short" if deal.market_price > deal.est_market_price() else "Long"}})
    pd.DataFrame(dict_deals)
