import numpy as np
import pandas as pd

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a - b)
print(b ** 2)

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A * B)
print(A.dot(B))
print(np.dot(A, B))

a = np.random.random((2, 3))
print(a)
print(a.sum())
print(a.max())
print(a.min())

b = np.arange(12).reshape(3, 4)
print(b.sum(axis=0))
print(b.min(axis=1))
print(b.cumsum(axis=1))

dt = pd.DataFrame(np.arange(20).reshape(4, 5), np.arange(0, 4), np.arange(0, 5))
dt1 = dt
dt2 = dt
