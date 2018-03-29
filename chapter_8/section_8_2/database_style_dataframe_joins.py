import pandas as pd
import numpy as np

# pandas.merge 根据一个或多个键进行join操作
# pandas.concat 沿着index或column方向将DataFrame拼接起来
# combine_first

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
df5 = pd.DataFrame({'key': ['a', 'c'],
                    'data3': range(2)})

pd.merge(df1, df2) # 未指定key时以具有相同column的列作为key
pd.merge(df1, df2, on='key') # 同上，指定了用于连接的column值
pd.merge(pd.merge(df1, df2, on='key'), df5, on='key')

df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
# 分别指定两个DataFrame的key
pd.merge(df3, df4, left_on='lkey', right_on='rkey')

# how指定连接方式inner、outer、left、right
pd.merge(df1, df2, how='outer')

# many-to-many
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'], 'data2': range(5)})
pd.merge(df1, df2, on='key', how='left')

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})
# 指定多个key值
pd.merge(left, right, on=['key1', 'key2'], how='outer')

