from datetime import datetime

import pandas as pd
import numpy as np
from pandas.tseries.offsets import Day, MonthEnd

ts = pd.Series(np.random.randn(4),
               index=pd.date_range('1/1/2000', periods=4, freq='M'))

# 移动数据
ts.shift(2)
ts.shift(-2)

# 移动index时间轴
ts.shift(2, freq='M')  # 平移月份
ts.shift(3, freq='D')  # 平移天数
ts.shift(1, freq='90T')  # T代表分钟

now = datetime(2011, 11, 17)
now + 3 * Day()
now + MonthEnd()
now + MonthEnd(2)

offset = MonthEnd()
offset.rollforward(now)
offset.rollback(now)

ts = pd.Series(np.random.randn(20),
               index=pd.date_range('1/15/2000', periods=20, freq='4d'))
ts.groupby(offset.rollforward).mean()
