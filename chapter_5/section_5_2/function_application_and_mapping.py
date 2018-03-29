import numpy as np
import pandas as pd

# DataFrame.apply(func)按行或者按列依次进行函数操作
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(np.abs(frame))
# 依次取每一行的最大值和最小值之差
f = lambda x: x.max() - x.min()
print(frame.apply(f))


def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])


print(frame.apply(f))
# 通过axis可以指定对列进行函数操作
print(frame.apply(f, axis='columns'))

# applymap()可以依次对DataFrame中各个元素调用函数操作
ff = lambda x: '%.2f' % x
frame.applymap(ff)
# Series中的map()可以实现applymap()操作
frame['e'].map(ff)
