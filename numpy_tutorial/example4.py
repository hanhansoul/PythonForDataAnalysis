import numpy as np
import numpy.linalg as nplg

a = np.array([[1, 0], [2, 3]])
b = np.array([[20, 5], [15, 10]])
c = np.array([[2, 1], [1, 4]])

print(a)
# 转置
print(a.transpose())
# 迹
print(np.trace(a))
print(a.trace())

# 特征值 特征向量
print(nplg.eig(a))

print(np.dot(b, c))

a = np.array([[1, 4], [5, 6]])
b = np.array([[4, 1], [2, 2]])

# 矩阵乘法的四种表示方式
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
np.dot(A, B)
A[:, 0] * 3 + A[:, 1] * 6 + A[:, 2] * 9
A[:, 0] * 6 + A[:, 1] * 5 + A[:, 2] * 4
A[:, 0] * 9 + A[:, 1] * 8 + A[:, 2] * 7
