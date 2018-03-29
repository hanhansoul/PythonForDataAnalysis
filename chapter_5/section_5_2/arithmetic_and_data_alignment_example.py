import numpy as np
import pandas as pd

s1 = pd.Series([7.3, -2.5, 3.4, 15], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

print(s1)
print(s2)
# NaN值在后续计算中不会被覆盖，而是被保留
# Series对应索引的值相加、相减、相乘、相除
print(s1 + s2)


df1 = pd.DataFrame(np.arange(9.).reshape(3, 3), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# 对应的行列位置相加
print(df1 + df2)

df3 = pd.DataFrame(np.arange(12.).reshape(3, 4), columns=list('abcd'))
df4 = pd.DataFrame(np.arange(20.).reshape(4, 5), columns=list('abcde'))
df4.loc[1, 'b'] = np.nan

print(df3 + df4)
# fill_value可以指定NaN或空项的值
df3.add(df4, fill_value=0)
print(df3)

print(1 / df3)
print(df3.rdiv(1))

df3.reindex(columns=df4.columns, fill_value=0)
print(df4.columns)
print(df3)

# 按行依次运算，即广播
arr = np.arange(12.).reshape(3, 4)
print(arr)
print(arr[0])
print(arr - arr[0])

# Series操作同上
frame = pd.DataFrame(np.arange(12.).reshape(4, 3),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]  # 此处DataFrame的一行同样可以看做一个Series对象
print(frame - series)

series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(frame + series2)

# 通过axis指定按列运算
series3 = frame['d']
print(series3)
print(frame.sub(series3, axis='index'))
