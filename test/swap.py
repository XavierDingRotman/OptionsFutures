from opfu.interest_rate_curve import SpotRateCurve
from opfu.swap import Swap

if __name__ == '__main__':
    libor_curve = SpotRateCurve(function=lambda x: x / 100)
    ois_curve = SpotRateCurve(function=lambda x: x * x / 100)
    swap = Swap(payment_rate=0.01 / 100, time_to_mature=3, forward_curve=libor_curve.get_forward_rate_curve(),
                discount_curve=ois_curve)
    print(swap.price())
    print(swap)
