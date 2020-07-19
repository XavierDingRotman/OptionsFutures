from opfu.ir_curve import IRCurve

if __name__ == '__main__':
    t = [-1, -0.5, -0.25, 0, 0.25, 0.5, 1]
    f = [0.005, 0.02, 0.02, 0.035, 0.05, 0.055, 0.075]
    ir_curve = IRCurve(t, f)
    ir_curve.plot()
