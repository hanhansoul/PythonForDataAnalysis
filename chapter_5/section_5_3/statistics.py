import numpy as np
import pandas as pd

'''
返回DataFrame和Series的数学统计数据
'''

frame = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
                     index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
print(frame)

# sum()
print(frame.sum())
print(frame.sum(axis='columns'))

# mean()
print(frame.mean(axis='columns'))
print(frame.mean(axis='columns', skipna=False))

# idxmax() / idxmin()
print(frame.max())
print(frame.idxmax())

# cumsum()
print(frame.cumsum())

# describe()
print(frame.describe())
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj.describe())
