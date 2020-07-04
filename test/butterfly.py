from bin.butterfly import Butterfly

if __name__ == '__main__':
    butterfly = Butterfly(K1=10, K3=20, T=0.5, price_1="BSM", price_2="BSM", price_3="BSM", S0=15)
    butterfly.graph_profit(start=0, end=40)
