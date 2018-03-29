import pandas as pd
import numpy as np

# hierarchical index允许用户使用多级多层次的index

data = pd.Series(np.random.randn(9),
                 index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])

# partial indexing
print(data['b'])
print(data['b':'c'])
print(data.loc[['b', 'c']])
print(data.loc[:, 2])

# unstack()
# 将多级索引的Series转换为DataFrame类型
data.unstack()
data.unstack().stack()

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

frame.swaplevel('key1', 'key2')
frame.sort_index(level=1)
frame.swaplevel(0, 1).sort_index(level=0)

frame.sum(level='key2')
frame.sum(level='color', axis=1)

# set_index() / reset_index()
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two',
                            'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})
frame1 = frame.set_index(['c', 'd'])
frame.set_index(['c', 'd'], drop=False)
frame2 = frame1.reset_index()
