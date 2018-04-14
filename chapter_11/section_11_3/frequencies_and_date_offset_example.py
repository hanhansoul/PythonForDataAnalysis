import pandas as pd
from pandas.tseries.offsets import Hour, Minute

"""
Hour
Minute
...
"""
four_hour = Hour(4)

pd.date_range('2000-01-01', '2000-01-03 23:59', freq='4h')

Hour(4) + Minute(40)
