from src.deal_combo import DealCombo
from src.deal import get_deal_from_ticker, DealEquity, DealEuroCall, DealEuroPut
from datetime import datetime as dt
from src.sigma import est_sigma
import pandas as pd

if __name__ == '__main__':
    r = 0.68/100
    sigma = est_sigma(pd.read_csv("../../data/XPO.csv")['Close'].to_numpy(), "day")
    xpo = DealEquity(position=500, price=74, commission=0.0073, ticker="XPO", timestamp=dt(2020, 6, 26))
    S0 = 79.18
    xpo_call_1 = get_deal_from_ticker("XPOG172008500.U", position=-100, price=2.5, S0=S0,
                                    r=r, sigma=sigma, comission=0.1839, timestamp=dt(2020, 6, 19))
    xpo_call_2 = get_deal_from_ticker("XPOG172008750.U", position=100, price=2.1, S0=S0,
                                    r=r, sigma=sigma, comission=0.1839, timestamp=dt(2020, 6, 19))
    xpo_put_1 = get_deal_from_ticker("XPOS172007000.U", position=100, price=1.85, S0=S0,
                                      r=r, sigma=sigma, comission=0.1839, timestamp=dt(2020, 6, 19))
    xpo_put_2 = get_deal_from_ticker("XPOS172007500.U", position=-100, price=3, S0=S0,
                                      r=r, sigma=sigma, comission=0.1839, timestamp=dt(2020, 6, 19))



    deal_combo_1 = DealCombo([xpo_call_1, xpo_call_2, xpo_put_1, xpo_put_2])
    deal_combo_1.graph_payoff(start=40, end=120)
    deal_combo_1.graph_profit(start=40, end=120)
    deal_combo_2 = DealCombo([xpo, xpo_call_1, xpo_call_2, xpo_put_1, xpo_put_2])
    deal_combo_2.graph_profit(start=40, end=120)

    print(deal_combo_1.find_break_even(start=40, end=120))
    print(deal_combo_2.find_break_even(start=40, end=120))

    print(xpo_call_1.security.get_bsm_price()) # 2.5 vs 2.44 => sell vs short
    print(xpo_call_2.security.get_bsm_price()) # 2.1 vs 1.8 => sell vs long
    print(xpo_put_1.security.get_bsm_price()) # 1.85 vs 1.21 => sell vs long
    print(xpo_put_2.security.get_bsm_price()) # 3 vs 2.7 => sell vs short