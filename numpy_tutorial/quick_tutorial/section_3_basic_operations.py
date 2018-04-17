import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)

c = a - b

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A * B)
print(A.dot(B))
print(np.dot(A, B))

a = np.random.random((2, 3))
print(a.sum())
print(a.min())
print(a.max())

a = np.ones((2, 3), dtype=int)
b = np.random.random((2, 3))
a *= 3
b += 3

a = np.ones(3, dtype=int)
b = np.linspace(0, np.pi, 3)
c = a + b
d = np.exp(c * 1j)

# 以ndarray中的相关方法为基础
b = np.arange(12).reshape(3, 4)
b.sum()
b.min()
a.max()
b.sum(axis=0)
b.sum(axis=1)
b.cumsum(axis=1)
b.cumsum(axis=0)

# 基本函数
B = np.arange(3)
np.exp(B)
np.sqrt(B)
np.square(B)


"""
arange()
linspace(start, stop, count)
"""