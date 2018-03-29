import pandas as pd
import numpy as np

'''
当将整型数作为Series的索引时，数据选择都以索引的label值为准。
使用loc和iloc可以使操作更加准确。
'''

ser = pd.Series(np.arange(3.))
print(ser)
# print(ser[-1])    # error

ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print(ser2[-1])
