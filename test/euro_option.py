from bin.euro_option import EuroCall, EuroPut

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
