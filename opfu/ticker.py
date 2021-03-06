dict_month = {"A": 1, "B": 2, "C": 3,
              "D": 4, "E": 5, "F": 6,
              "G": 7, "H": 8, "I": 9,
              "J": 10, "K": 11, "L": 12,
              "M": 1, "N": 2, "O": 3,
              "P": 4, "Q": 5, "R": 6,
              "S": 7, "T": 8, "U": 9,
              "V": 10, "W": 11, "X": 12}

dict_is_call = {"A": True, "B": True, "C": True,
                "D": True, "E": True, "F": True,
                "G": True, "H": True, "I": True,
                "J": True, "K": True, "L": True,
                "M": False, "N": False, "O": False,
                "P": False, "Q": False, "R": False,
                "S": False, "T": False, "U": False,
                "V": False, "W": False, "X": False}


def get_option_info_from_ticker(ticker, equity_length=3):
    asset = ticker[:equity_length]
    exp_month_code = ticker[equity_length]
    month = dict_month[exp_month_code]
    is_call = dict_is_call[exp_month_code]
    day = int(ticker[equity_length + 1:equity_length + 3])
    year = int(ticker[equity_length + 3:equity_length + 5]) + 2000
    K = int(ticker[equity_length + 5:-2]) / 100
    country = ticker[-1]
    return asset, is_call, month, day, year, K, country

