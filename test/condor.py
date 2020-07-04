from src.condor import Condor

if __name__ == '__main__':
    condor = Condor(K1=10, K2=15, K3=25, K4=30, T=0.5, price_1="BSM", price_2="BSM", price_3="BSM",
                    price_4="BSM", S0=17.5)
    condor.graph_profit(start=0, end=55)
