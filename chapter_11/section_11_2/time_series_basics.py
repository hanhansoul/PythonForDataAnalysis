import pandas as pd
import numpy as np
from datetime import datetime
from pandas.tseries.offsets import Day, MonthEnd

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = pd.Series(np.random.randn(6), index=dates)

# indexing selection subsetting
stamp = ts.index[2]
ts['1/10/2011']
ts['20110110']

# 利用periods处理较长的时间范围
# 日期相关的index操作
longer_ts = pd.Series(np.random.randn(1000),
                      index=pd.date_range('1/1/2000', periods=1000))
print(longer_ts['2001'])
print(longer_ts['2001-05'])
print(ts[datetime(2011, 1, 7):])
print(ts.truncate(after='1/9/2011'))

dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100, 4),
                       index=dates,
                       columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(long_df.loc['5-2001'])
print(long_df['Texas'])

# 处理重复的时间index

dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000',
                          '1/2/2000', '1/3/2000'])
dup_ts = pd.Series(np.arange(5), index=dates)
print(dup_ts.index.is_unique)
print(dup_ts['1/3/2000'])  # 唯一项
print(dup_ts['1/2/2000'])  # 重复项

grouped = dup_ts.groupby(level=0)  # 对重复项进行分组
print(grouped.mean())
print(grouped.count())

#
now = datetime(2011, 11, 17)
now + 3 * Day()
now + MonthEnd()
now + MonthEnd(2)

offset = MonthEnd()
offset.rollforward(now)

ts = pd.Series(np.random.randn(20),
               index=pd.date_range('1/15/2000', periods=20, freq='4d'))
ts.groupby(offset.rollforward).mean()
