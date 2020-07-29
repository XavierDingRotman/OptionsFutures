from opfu.interest_rate import InterestRate, SpotRate

if __name__ == '__main__':
    ir_1 = InterestRate(rate=0.1, settle=0, end=1)
    print(ir_1.get_rate(1))
    ir_2 = ir_1.convert_to(1)
    print(ir_2.get_rate())
    ir_short = SpotRate(rate=0.1, end=1)
    ir_long = SpotRate(rate=0.2, end=2)
    forward_rate = ir_short.get_forward_rate(ir_long)
    print(forward_rate.rate)
