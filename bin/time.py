from datetime import datetime as dt


def get_T(trans_date, mature_date, base=365.2425):
    return (mature_date - trans_date).days/base

