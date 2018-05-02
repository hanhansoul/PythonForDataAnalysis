import numpy as np
import sympy as sy
import scipy.linalg as la

A = np.array([[1, 2, 2, 2], [0, 0, 2, 4], [0, 0, 0, 0]])
B = np.array([0, 0, 0])

# print(A)
# print(B)

#
# x = np.linalg.solve(A, B)
# print(x)

C = np.array([[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 1]])
print(C)
# print(la.qr(C))

(c, q) = la.qr(C)
print(c)
print(q)