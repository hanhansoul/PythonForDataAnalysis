import pandas as pd
import numpy as np

'''
loc[row_label, column_label]
iloc[row_index, column_index]
at[row_label, column_label]
iat[row_index, column_index]

loc / iloc支持slice，at / iat不支持slice
'''
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

# 选择单行多列
print(data.loc['Colorado', ['two', 'three']])
# 同上，但使用整型数作为索引
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[2])
# 多行多列
print(data.iloc[[1, 2], [3, 0, 1]])

# 切片
print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3][data.three > 5])

print(data.at[:'Utah', 'two'])
