import numpy as np
import pandas as pd

# Series.sort_index() 对索引进行排序
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())

# DataFrame.sort_index() 对行索引进行排序
# DataFrame.sort_index(axis=1) 对列索引进行排序
frame = pd.DataFrame(np.arange(8).reshape(2, 4),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
print(frame.sort_index())
print(frame.sort_index(axis=1))
print(frame.sort_index(axis=1, ascending=False))

obj = pd.Series([4, 7, -3, 2])
obj.sort_values()

obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
obj.sort_values()
obj.sort_values(ascending=False)

frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame.sort_values(by='b')
frame.sort_values(by=['a', 'b'])

obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj)
print(obj.sort_values())
print(obj.sort_values().rank())
print(obj.rank())
print(obj.rank(method='first'))
print(obj.rank(ascending=False, method='max'))
print(obj.rank(ascending=False, method='min'))

frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
print(frame)
print(frame.rank(axis='columns'))
print(frame.rank(axis='index'))
