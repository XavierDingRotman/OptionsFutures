import pandas as pd

from opfu.bond import FixedPaymentFixedIntervalBond, ForwardRateCurvePaymentFixedIntervalBond


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

    def cashflow(self):
        dict_result = {}
        dict_result['fixed_payment'] = self.fix_leg.cashflow()
        dict_result['floating_payment'] = self.floating_leg.cashflow()
        df = pd.DataFrame(dict_result)
        df['total'] = df['fixed_payment'] + df['floating_payment']
        return dict(df['total'])

    def __str__(self):
        dict_result = {}
        dict_result['fixed_payment'] = self.fix_leg.cashflow()
        dict_result['floating_payment'] = self.floating_leg.cashflow()
        dict_result['cashflow'] = self.cashflow()
        df = pd.DataFrame(dict_result)
        result = 'cashflow : \n{}\n'.format(str(df))
        result += 'price : {}\n'.format(self.price())
        return result
