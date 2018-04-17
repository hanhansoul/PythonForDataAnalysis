import numpy as np

"""
arange()
array()
copy()

empty()
empty_like()
ones()
ones_like()
zeros()
zeros_like()

fromfile()
fromfunction()

identity()
eye()

linspace()
logspace()
"""

# 单位矩阵
np.identity(10)
np.eye(5)

np.fromfunction(lambda x, y: x*10 + y, (3, 4))
