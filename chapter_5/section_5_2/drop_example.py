import numpy as np
import pandas as pd

# 删除Series中一个或多个索引及其对应值
# 通过axis也可以指定删除索引或列名
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
obj1 = obj.drop('c')
print(obj1)
obj2 = obj.drop(['d', 'e'])
print(obj2)
obj.drop('c', inplace=True)
print(obj)

data = pd.DataFrame(np.arange(16).reshape(4, 4),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data.drop(['Colorado', 'Ohio']))
print(data.drop(['two'], axis=1))
