import numpy as np
import pandas as pd

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
print(uniques)

print(obj.value_counts())
print(pd.value_counts(obj.values, sort=False))

# isin()
print(obj)
mask = obj.isin(['b', 'c'])
print(mask)

# print(np.random.randn(12))
frame = pd.DataFrame(np.arange(12).reshape(3, 4),
                     columns=['a', 'b', 'c', 'd'],
                     index=[1, 2, 3])
print(frame['a'].isin([2]))
print(frame.loc[1].isin([1, 2, 3]))

# Index.get_indexer()
# 创建一个Series中元素到另一个Index对象中元素的映射关系
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
pd.Index(unique_vals).get_indexer(to_match)

# 柱状图
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                     'Qu2': [2, 3, 1, 2, 3],
                     'Qu3': [1, 5, 2, 4, 4]})
result = data.apply(pd.value_counts).fillna(0)
print(result)
