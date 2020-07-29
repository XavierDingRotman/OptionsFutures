from opfu.interest_rate import SpotRate, ForwardRate


class InterestRateCurve(object):
    def __init__(self, function, compounding_base='continuous', rounding=6):
        self.function = function
        self.compounding_base = compounding_base
        self.rounding = rounding

    def get_num_value(self, input):
        if isinstance(self.function, dict):
            return round(self.function[input], self.rounding)
        if callable(self.function):
            return round(self.function(input), self.rounding)


class SpotRateCurve(InterestRateCurve):
    def __init__(self, function, compounding_base='continuous', rounding=6):
        InterestRateCurve.__init__(self, function, compounding_base, rounding)

    def get_value(self, input):
        return SpotRate(rate=self.get_num_value(input), end=input, rounding=self.rounding)

    def get_forward(self, settle, end):
        return self.get_value(settle).get_forward_rate(self.get_value(end))

    def get_forward_rate_curve(self):
        return ForwardRateCurve(function=lambda x, y: self.get_forward(x, y).rate,
                                compounding_base=self.compounding_base, rounding=self.rounding)


class ForwardRateCurve(InterestRateCurve):
    def __init__(self, function, compounding_base='continuous', rounding=6):
        InterestRateCurve.__init__(self, function, compounding_base, rounding)

    def get_num_vale_forward_rate(self, start, end):
        return self.function(start, end)

    def get_value(self, settle, end):
        return ForwardRate(rate=self.get_num_vale_forward_rate(settle, end), settle=settle, end=end,
                           rounding=self.rounding)


if __name__ == '__main__':
    def curve(x):
        return x / 100


    spot_rate_curve = SpotRateCurve(curve)

    print(spot_rate_curve.get_forward(1, 2).rate)

    curve = {0.25: 0.01, 0.5: 0.01, 0.75: 0.03, 1: 0.05, 1.25: 0.05, 1.5: 0.09}

    spot_rate_curve = SpotRateCurve(curve)

    print(spot_rate_curve.get_forward(1.25, 1.5).rate)

    forward_rate_curve = spot_rate_curve.get_forward_rate_curve()

    print(forward_rate_curve.get_value(0.25, 0.5).rate)
