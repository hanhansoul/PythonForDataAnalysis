import pandas as pd
import numpy as np

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

print("frame:")
print(frame)

# 取DataFrame的前5条或若干条
print("frame.head():")
print(frame.head())
print("frame.head(10):")
print(frame.head(10))

# 为DataFrame指定columns和index
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print("frame2.columns: ", frame2.columns)
# 返回DataFrame指定的列
# 返回的是一个Series对象
print("frame2['state']: ", frame2['state'])
print("frame2.year: ", frame2.year)
# 返回指定的行DataFrame.loc[]
print("frame2.loc['three']: ")
print(frame2.loc['three'])
# 新增修改列
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(6.)
print(frame2)

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)
# 删除列
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
del frame2['eastern']
print(frame2)

# nested dict
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
print(frame3.T)     # 通过转置T操作可以将DataFrame的行列互换
frame3.index.name = "year"
frame3.columns.name = "state"
print(frame3)

pdata = {"Ohio": frame3["Ohio"][:-1], "Nevada": frame3["Nevada"][:2]}

pd.DataFrame(pdata)

print(frame3.values)
print(frame3.index)
print(frame3.columns)

# DataFrame构造函数
# 一维数组或二位数组
d1 = [1, 2, 3, 4, 5]
f1 = pd.DataFrame(d1)  # 1行1列的DataFrame
d2 = [[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd']]
f2 = pd.DataFrame(d2)  # 2列4行的DataFrame
f3 = pd.DataFrame(d2, index=['r1', 'r2', 'r3', 'r4'], columns=['c1', 'c2'])
print(f2)

# dict
d2 = {'a': [1, 2, 3], 'b': (10, 20, 30), 'c': np.array(100, 200, 300)}
f4 = pd.DataFrame(d2)
print(f4)

# numpy矩阵
d3 = np.random.randn(5, 5)
f5 = pd.DataFrame(d3)

# Series字典
d4 = {'a': pd.Series([1, 2, 3]), 'b': pd.Series([10, 20, 30])}
f6 = pd.DataFrame(d4)

# nested dict
# 每一个nested dict视为一列
d5 = {'a': {'A': 1, 'B': 2, 'C': 3}, 'b': {'D': 4, 'E': 5, 'F': 6}, 'c': {'G': 7, 'H': 8, 'I': 9}}
f7 = pd.DataFrame(d5)
print(f7)

# 字典或Series列表
# 列表中每个元素视为一行
d6 = [{'A': 1, 'B': 2, 'C': 3}, {'D': 4, 'E': 5, 'F': 6}, {'G': 7, 'H': 8, 'I': 9}]
f8 = pd.DataFrame(d6)
print(f8)

f9 = pd.DataFrame(f8)
