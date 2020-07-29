from opfu.security import Security


class Bond(Security):
    def __init__(self, payments: dict, discount_curve, is_short=False, name="Unnamed Bond", market_price=None,
                 calculate_price_at_initialization=True):
        self.payments = payments
        self.discount_curve = discount_curve
        self.is_short = is_short
        if not calculate_price_at_initialization:
            price = None
        else:
            price = self.get_price()
        Security.__init__(self, is_short=is_short, price=price, name=name, market_price=market_price)

    def cashflow(self):
        symbol = -1 if self.is_short else 1
        result = {}
        for key in self.payments.keys():
            result[key] = symbol * self.payments[key]
        return result

    def get_price(self):
        result = 0
        for payment_date in self.payments.keys():
            result += self.payments[payment_date] * self.discount_curve.get_value(payment_date).discount_factor() \
                      * (-1 if self.is_short else 1)
        return result

    def __repr__(self):
        return str(self.cashflow())

    def __str__(self):
        result = 'Name : {}\n'.format(self.name)
        result += 'Payment schedule : {} \n'.format(self.__repr__())
        result += 'Price : {} \n'.format(self.price)
        return result


class FixedIntervalBond(Bond):
    def __init__(self, payments, payment_period, time_to_mature, discount_curve, is_short=False,
                 calculate_price_at_initialization=True, name='Unnamed Fixed Interval Bond'):
        self.payment_period = payment_period
        self.time_to_mature = time_to_mature
        time = self.payment_period
        settled_payments = {}
        while (time <= self.time_to_mature):
            settled_payments[time] = payments[time]
            time += self.payment_period
        Bond.__init__(self, settled_payments, discount_curve, is_short, calculate_price_at_initialization=False,
                      name=name)
        if calculate_price_at_initialization:
            self.price = self.get_price()


class FixedPaymentFixedIntervalBond(FixedIntervalBond):
    def __init__(self, payment_rate, principle, time_to_mature, discount_curve, is_short=False, payment_period=None,
                 number_of_payments=None,
                 pay_principle=True,
                 calculate_price_at_initialization=True, name='Unnamed Fixed Payment Fixed Interval Bond'):
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
                                   is_short=is_short, calculate_price_at_initialization=False, name=name)
        if calculate_price_at_initialization:
            self.price = self.get_price()


class FloatingPaymentFixedIntervalBond(FixedIntervalBond):
    def __init__(self, payment_rate_curve, principle, time_to_mature, discount_curve, is_short=False,
                 payment_period=None,
                 number_of_payments=None, pay_principle=True, calculate_price_at_initialization=True,
                 name='Unnamed Floating Payment Fixed Interval Bond'):
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
                                   is_short=is_short, calculate_price_at_initialization=False, name=name)
        if calculate_price_at_initialization:
            self.price = self.get_price()


class ForwardRateCurvePaymentFixedIntervalBond(FloatingPaymentFixedIntervalBond):
    def __init__(self, forward_rate_curve, principle, time_to_mature, discount_curve, is_short=False,
                 payment_period=None, number_of_payments=None,
                 pay_principle=True,
                 calculate_price_at_initialization=True,
                 name='Unnamed Forward Rate Curve Payment Fixed Interval Bond'):
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
                                                  pay_principle=pay_principle,
                                                  calculate_price_at_initialization=False,
                                                  name=name)
        if calculate_price_at_initialization:
            self.price = self.get_price()
