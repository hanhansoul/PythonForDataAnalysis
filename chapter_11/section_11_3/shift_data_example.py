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
ts.shift(2, freq='M')
ts.shift(3, freq='D')

now = datetime(2011, 11, 17)
now + 3 * Day()
