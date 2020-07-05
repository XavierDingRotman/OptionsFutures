from opfu.stock import Stock

if __name__ == '__main__':
    stock_1 = Stock(10, 3, is_short=True)
    print(stock_1.payoff(20))

    stock_1.graph_payoff()
    print(stock_1.find_break_even())
