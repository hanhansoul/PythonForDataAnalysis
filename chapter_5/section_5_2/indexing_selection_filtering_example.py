import numpy as np
import pandas as pd

# 通过索引选择或过滤Series或DataFrame的片段

# Series
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj['a':'c'])
obj['a':'c'] = 5
print(obj)
print(obj[['b', 'a', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])

# DataFrame
data = pd.DataFrame(np.arange(16).reshape(4, 4),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
# DataFrame[columns]选择指定的列，每一列对应一个Series
print(data['two'])
print(data[['three', 'one']])
# 索引切片方式选择列是一种特殊的简易方式，通常传递一个元素或列表都表示列选择
print(data[:2])
print(data[data['three'] > 5])
print(data < 5)
print(data[data < 5])

# DataFrame的行选择使用loc[]和iloc[]
# loc[行索引, 列名]
print(data.loc['Colorado', ['two', 'three']])
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[[1, 2], [3, 0, 1]])
print(data.iloc[:, :3][data > 5])
