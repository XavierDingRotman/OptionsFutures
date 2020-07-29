from opfu.interest_rate_curve import SpotRateCurve

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
