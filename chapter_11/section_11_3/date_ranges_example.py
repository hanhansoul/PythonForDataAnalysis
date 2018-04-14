import pandas as pd
import numpy as np
from datetime import datetime

"""
通过date_range生成时间访问DatetimeIndex
start指定起始时间
end指定结束时间
periods指定时间区间中时间点的数量
freq指定时间间隔模式
"""
pd.date_range('2012-04-01', '2012-06-01')
pd.date_range(start='2012-04-01', periods=20)
pd.date_range(end='2012-06-01', periods=20)

pd.date_range('2000-01-01', '2000-12-01', freq='BM')
pd.date_range('2012-05-02 12:34:56', periods=5, normalize=True)
