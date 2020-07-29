from opfu.bond import FixedPaymentFixedIntervalBond, ForwardRateCurvePaymentFixedIntervalBond
from opfu.interest_rate_curve import SpotRateCurve


class FixedLeg(FixedPaymentFixedIntervalBond):
    def __init__(self, payment_rate, principle, time_to_mature, discount_curve, is_short=False, payment_period=0.5,
                 number_of_payments=None, pay_principle=False):
        FixedPaymentFixedIntervalBond.__init__(self, payment_rate, principle, time_to_mature, discount_curve, is_short,
                                               payment_period, number_of_payments, pay_principle=pay_principle)


class FloatingLeg(ForwardRateCurvePaymentFixedIntervalBond):
    def __init__(self, forward_rate_curve, principle, time_to_mature, discount_curve, is_short=False,
                 payment_period=0.5, number_of_payments=None,
                 pay_principle=False):
        ForwardRateCurvePaymentFixedIntervalBond.__init__(self, forward_rate_curve, principle, time_to_mature,
                                                          discount_curve, is_short, payment_period, number_of_payments,
                                                          pay_principle=pay_principle)


class Swap(object):
    def __init__(self, payment_rate, time_to_mature, forward_curve, discount_curve, is_short=False, payment_period=0.5,
                 exchange_principle=False, principle=10e6):
        self.payment_period = payment_period
        self.principle = principle
        self.is_short = is_short
        self.fix_leg = FixedLeg(payment_rate, principle, time_to_mature, discount_curve, is_short=(not self.is_short),
                                payment_period=payment_period, pay_principle=exchange_principle)
        self.floating_leg = FloatingLeg(forward_curve, principle, time_to_mature, discount_curve,
                                        is_short=self.is_short,
                                        payment_period=payment_period, pay_principle=exchange_principle)

    def price(self):
        return self.fix_leg.price() + self.floating_leg.price()


if __name__ == '__main__':
    libor_curve = SpotRateCurve(function=lambda x: x)
    ois_curve = SpotRateCurve(function=lambda x: x)
    swap = Swap(payment_rate=0.1 / 100, time_to_mature=1, forward_curve=libor_curve.get_forward_rate_curve(),
                discount_curve=ois_curve)
    print(swap.price())
