from opfu.euro_option import EuroCall, EuroPut

if __name__ == '__main__':
    call_1 = EuroCall(10, 3)
    print(call_1.payoff(1))
    print(call_1.payoff(100))
    put_1 = EuroPut(10, 3)
    print(put_1.payoff(1))
    print(put_1.payoff(100))
    call_2 = EuroCall(10, 3, True)

    call_1.graph_payoff()
    call_2.graph_payoff()

    call_3 = EuroCall(K=10, T=0.5, is_short=False, price="BSM", S0=5, r=0.001, sigma=1)
    print(call_3.greek_letter("delta"))
    print(call_3.greek_letter("gamma"))
    print(call_3.greek_letter("theta"))
    print(call_3.greek_letter("vega"))
    print(call_3.greek_letter("rho"))
