from opfu.interest_rate_curve import SpotRateCurve


class Bond(object):
    def __init__(self, payments: dict, discount_curve, is_short=False):
        self.payments = payments
        self.discount_curve = discount_curve
        self.is_short = is_short

    def price(self):
        result = 0
        for payment_date in self.payments.keys():
            result += self.payments[payment_date] * self.discount_curve.get_value(payment_date).discount_factor() \
                      * (-1 if self.is_short else 1)
        return result


class FixedIntervalBond(Bond):
    def __init__(self, payments, payment_period, time_to_mature, discount_curve, is_short=False):
        self.payment_period = payment_period
        self.time_to_mature = time_to_mature
        time = self.payment_period
        settled_payments = {}
        while (time <= self.time_to_mature):
            settled_payments[time] = payments[time]
            time += self.payment_period
        Bond.__init__(self, settled_payments, discount_curve, is_short)


class FixedPaymentFixedIntervalBond(FixedIntervalBond):
    def __init__(self, payment_rate, principle, time_to_mature, discount_curve, is_short=False, payment_period=None,
                 number_of_payments=None,
                 pay_principle=True):
        self.payment_rate = payment_rate
        self.principle = principle
        if isinstance(number_of_payments, int):
            payment_period = time_to_mature / number_of_payments
            self.payment_period = payment_period
        else:
            self.payment_period = payment_period
        self.number_of_payments = 0
        time = self.payment_period
        settled_payments = {}
        while (time < time_to_mature):
            settled_payments[time] = payment_rate * principle
            self.number_of_payments += 1
            if time + self.payment_period >= time_to_mature:
                if time + self.payment_period == time_to_mature:
                    self.number_of_payments += 1
                    settled_payments[time_to_mature] = payment_rate * principle
                    if pay_principle:
                        settled_payments[time_to_mature] += principle
                else:
                    if pay_principle:
                        settled_payments[time] += principle
            time += self.payment_period
        FixedIntervalBond.__init__(self, settled_payments, self.payment_period, time_to_mature, discount_curve,
                                   is_short=is_short)


class FloatingPaymentFixedIntervalBond(FixedIntervalBond):
    def __init__(self, payment_rate_curve, principle, time_to_mature, discount_curve, is_short=False,
                 payment_period=None,
                 number_of_payments=None, pay_principle=True):
        self.payment_rate_curve = payment_rate_curve
        self.principle = principle
        if isinstance(number_of_payments, int):
            payment_period = time_to_mature / number_of_payments
            self.payment_period = payment_period
        else:
            self.payment_period = payment_period
        self.number_of_payments = 0
        time = self.payment_period
        settled_payments = {}
        while (time < time_to_mature):
            settled_payments[time] = payment_rate_curve[time] * principle
            self.number_of_payments += 1
            if time + self.payment_period >= time_to_mature:
                if time + self.payment_period == time_to_mature:
                    self.number_of_payments += 1
                    settled_payments[time_to_mature] = payment_rate_curve[time_to_mature] * principle
                    if pay_principle:
                        settled_payments[time_to_mature] += principle
                else:
                    if pay_principle:
                        settled_payments[time] += principle
            time += self.payment_period
        FixedIntervalBond.__init__(self, settled_payments, self.payment_period, time_to_mature, discount_curve,
                                   is_short=is_short)


class ForwardRateCurvePaymentFixedIntervalBond(FloatingPaymentFixedIntervalBond):
    def __init__(self, forward_rate_curve, principle, time_to_mature, discount_curve, is_short=False,
                 payment_period=None, number_of_payments=None,
                 pay_principle=True):
        if isinstance(number_of_payments, int):
            payment_period = time_to_mature / number_of_payments
            self.payment_period = payment_period
        else:
            self.payment_period = payment_period
        self.number_of_payments = 0
        time = payment_period
        payment_rate_curve = {}
        while (time <= time_to_mature):
            forward_rate = forward_rate_curve.get_value(time - self.payment_period, time).convert_to('simple').rate
            payment_rate_curve[time] = forward_rate * self.payment_period
            self.number_of_payments += 1
            time += self.payment_period
        FloatingPaymentFixedIntervalBond.__init__(self, payment_rate_curve, principle, time_to_mature, discount_curve,
                                                  is_short=is_short,
                                                  payment_period=self.payment_period,
                                                  number_of_payments=self.number_of_payments,
                                                  pay_principle=pay_principle)


if __name__ == '__main__':
    discount_curve = SpotRateCurve(function=lambda x: x * x / 100)

    forward_rate_curve_floating_payment_bond = ForwardRateCurvePaymentFixedIntervalBond(
        forward_rate_curve=discount_curve.get_forward_rate_curve(),
        principle=100, number_of_payments=4, time_to_mature=1, discount_curve=discount_curve,
        pay_principle=True)

    print(forward_rate_curve_floating_payment_bond.price())
