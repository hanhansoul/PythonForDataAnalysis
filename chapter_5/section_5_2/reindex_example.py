import numpy as np
import pandas as pd

# reindex实现Series的索引重排、筛选等功能
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj)
print(obj2)

obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3.reindex(range(6), method='ffill'))

frame = pd.DataFrame(np.arange(9).reshape(3, 3), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)
states = ['Texas', 'Utah', 'California']
frame3 = frame.reindex(columns=states)
print(frame3)

frame4 = frame.loc[['a', 'b', 'c', 'd'], states]
print(frame4)
