import pandas as pd
import numpy as np

obj = pd.Series([4, 7, -5, 3])
print("pd.Series:")
print(obj)
print("Series.values: ", obj.values)
print("Series.index: ", obj.index)

# 指定索引
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print("pd.Series:")
print(obj2)
print("Series.index: ", obj2.index)
# 取指定的行内容
print("obj2['a']: ", obj2['a'])
# 修改指定行内容
obj2['d'] = 10
print("pd.Series after update:")
print(obj2)
# 过滤器
print("obj2[obj2 > 0]: ")
print(obj2[obj2 > 0])
# Series的运算
print("obj2 * 2: ", obj2 * 2)
print("np.exp(obj2): ", np.exp(obj2))
print("'b' in obj2: ", 'b' in obj2)

# 通过dict创建Series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print("pd.isnull(obj4): ", pd.isnull(obj4))
print("obj4.isnull(): ", obj4.isnull())
print("pd.notnull(obj4): ", pd.notnull(obj4))
# 类似于join操作
print("obj3 + obj4: ")
print(obj3 + obj4)

# Series命名及索引命名
obj4.name = "population"
obj4.index.name = "index"
print(obj4)
