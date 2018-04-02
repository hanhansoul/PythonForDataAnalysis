import numpy as np

"""
引用相等
"""
a = np.arange(12)
b = a
print(b is a)
a.shape = 3, 4
print(b)

"""
视图/浅拷贝
"""
c = a.view()
print(c is a)
print(c.base is a)
print(c.flags.owndata)
# 切片返回原array的视图
s = a[:, 1:3]
s[:] = 10

"""
深拷贝
"""
d = a.copy()
print(d is a)
print(d.base is a)
d[:] = 99
