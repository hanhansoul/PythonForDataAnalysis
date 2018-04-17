import pandas as pd
import numpy as np
from datetime import datetime

"""
pd.Periods表示时间跨度
"""
p = pd.Period(2007, freq='A-DEC')  # 表示从2007-1-1至2007-12-31
print(p + 5)
print(p - 2)

# PeriodIndex表示一个period序列，可以作为index
rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')

# frequency conversion

p = pd.Period('2007', freq='A-DEC')
p.asfreq('M', how='start')
p.asfreq('M', how='end')

rng = pd.period_range('2006', '2009', freq='A-DEC')
pd.Series(np.random.randn(len(rng)), index=rng)


"""
Period和PeriodIndex可以通过asfreq方法转换间隔
"""

rng = pd.date_range('2000-01-01', periods=3, freq='M')
ts = pd.Series(np.random.randn(3), index=rng)
pts = ts.to_period()


p = pd.Period('2014Q4', freq='Q-JAN')
p.asfreq('D', 'start')
p.asfreq('D', 'end')
