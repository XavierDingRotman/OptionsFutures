from opfu.spread import BullSpread

if __name__ == '__main__':
    bullspread = BullSpread(K1=10, K2=20, T=1,
                            price_1="BSM", price_2="BSM", S0=15, r=0.01, sigma=0.1, use_call=True)
    bullspread.graph_profit(start=0, end=30)
