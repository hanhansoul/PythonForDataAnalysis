import pandas as pd
import numpy as np

arr = np.arange(12).reshape(3, 4)
np.concatenate([arr, arr])

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

pd.concat([s1, s2, s3])
pd.concat([s1, s2, s3], axis=1)

s4 = pd.concat([s1, s3])
pd.concat([s1, s4], axis=1)
pd.concat([s1, s4], axis=1, join='inner')

pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])
pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])

