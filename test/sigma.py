import pandas as pd
from src.sigma import est_sigma

if __name__ == '__main__':
    tau = "day"
    sigma = est_sigma(pd.read_csv("../data/XPO.csv")['Close'].to_numpy(), "day")
    print(sigma)
