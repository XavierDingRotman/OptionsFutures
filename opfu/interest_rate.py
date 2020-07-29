from math import exp, log


def get_rate_from_compound(compound, base, time_span):
    if isinstance(base, (int, float)):
        result = base * (exp(log(compound) / (time_span * base)) - 1)
    else:
        result = log(compound) / time_span

    if base == 'simple':
        result = (compound - 1) / time_span
    return result


def get_forward_rate(ir_short, ir_long, base=None):
    if ir_short.settle != ir_long.settle:
        raise TypeError
    if ir_long.end < ir_short.end:
        raise TypeError
    time_span = ir_long.end - ir_short.end
    if base is None:
        base = ir_short.compounding_base
    compound = ir_long.compound() / ir_short.compound()
    rounding = max(ir_short.rounding, ir_long.rounding)
    return ForwardRate(rate=round(get_rate_from_compound(compound, base, time_span), rounding),
                       settle=ir_short.end, end=ir_long.end,
                       compounding_base=base,
                       rounding=max(ir_short.rounding, ir_long.rounding))


class InterestRate(object):
    def __init__(self, rate, settle, end, compounding_base: object = 'continuous', rounding=6):
        self.settle = settle
        self.end = end
        self.compounding_base = compounding_base
        self.rate = rate
        self.time_span = self.end - self.settle
        self.rounding = rounding

    def compound(self):
        if isinstance(self.compounding_base, (int, float)):
            result = (1 + self.rate / self.compounding_base) ** ((self.time_span) * self.compounding_base)
        else:
            result = exp(self.rate * (self.time_span))

        if self.compounding_base == 'simple':
            result = (1 + self.rate * self.time_span)

        return round(result, self.rounding)

    def discount_factor(self):
        return 1 / self.compound()

    def get_rate(self, base: object = 'continuous'):
        return round(get_rate_from_compound(self.compound(), base, time_span=self.time_span), self.rounding)

    def convert_to(self, base: object = 'continuous'):
        return InterestRate(rate=self.get_rate(base), settle=self.settle, end=self.end, compounding_base=base,
                            rounding=self.rounding)


class SpotRate(InterestRate):
    def __init__(self, rate, end, compounding_base='continuous', rounding=6):
        InterestRate.__init__(self, rate, 0, end, compounding_base, rounding)

    def get_forward_rate(self, long_spot_rate):
        return get_forward_rate(self, long_spot_rate)


class ForwardRate(InterestRate):
    def __init__(self, rate, settle, end, compounding_base='continuous', rounding=6):
        InterestRate.__init__(self, rate, settle, end, compounding_base, rounding)

