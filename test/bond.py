from opfu.bond import ForwardRateCurvePaymentFixedIntervalBond
from opfu.interest_rate_curve import SpotRateCurve

if __name__ == '__main__':
    discount_curve = SpotRateCurve(function=lambda x: x * x / 100)

    forward_rate_curve_floating_payment_bond = ForwardRateCurvePaymentFixedIntervalBond(
        forward_rate_curve=discount_curve.get_forward_rate_curve(),
        principle=100, number_of_payments=4, time_to_mature=1, discount_curve=discount_curve,
        pay_principle=True, is_short=True)

    print(forward_rate_curve_floating_payment_bond.price)

    print(forward_rate_curve_floating_payment_bond)
