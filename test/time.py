from datetime import datetime as dt
from bin.time import get_T

if __name__ == '__main__':
    dt1 = dt(year=2020, month=7, day=17)
    dt2 = dt(2020, 6, 19)
    print(get_T(dt2, dt1))
