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
    for greek in ['delta', 'gamma', 'theta', 'vega', 'rho']:
        print('{} : {}'.format(greek, call_3.greek_letter(greek)))

    call_3.graph_payoff()
    print(call_3.find_break_even())
