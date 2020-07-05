from datetime import datetime as dt

from opfu.deal import get_deal_from_ticker, DealEquity
from opfu.deal_combo import DealCombo

if __name__ == '__main__':
    xpo = DealEquity(position=500, price=74, commission=0.0073, ticker="XPO", timestamp=dt(2020, 6, 26))
    S0 = 79.18
    xpo_call_1 = get_deal_from_ticker("XPOG172008500.U", position=-100, price=2.5, S0=S0,
                                      r=0.01, sigma=0.1, comission=0.1839, timestamp=dt(2020, 6, 19))
    xpo_call_2 = get_deal_from_ticker("XPOG172008750.U", position=100, price=2.1, S0=S0,
                                      r=0.01, sigma=0.1, comission=0.1839, timestamp=dt(2020, 6, 19))
    xpo_put_1 = get_deal_from_ticker("XPOS172007000.U", position=100, price=1.85, S0=S0,
                                     r=0.01, sigma=0.1, comission=0.1839, timestamp=dt(2020, 6, 19))
    xpo_put_2 = get_deal_from_ticker("XPOS172007500.U", position=-100, price=3, S0=S0,
                                      r=0.01, sigma=0.1, comission=0.1839, timestamp=dt(2020, 6, 19))

    deal_combo_1 = DealCombo([xpo_call_1, xpo_call_2, xpo_put_1, xpo_put_2])
    deal_combo_1.graph_payoff(start=40, end=120)
    deal_combo_1.graph_profit(start=40, end=120)
    deal_combo_2 = DealCombo([xpo, xpo_call_1, xpo_call_2, xpo_put_1, xpo_put_2])
    deal_combo_2.graph_profit(start=40, end=120)

    print(deal_combo_1.find_break_even(start=40, end=120))
    print(deal_combo_2.find_break_even(start=40, end=120))