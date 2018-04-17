import numpy as np

"""
reshape()
resize()
ravel()
"""

a = np.floor(10 * np.random.random((3, 4)))
a.shape

a.ravel()

a.reshape(6, 2)
a.reshape(6, 1)

a.resize((2, 6))
a.resize((1, 6))

a = np.array([[0, 1, 4], [2, 3, 5]])
a.reshape(3, 2)
a.resize(3, 1)


"""
合并矩阵
hstack()
vstack()
column_stack()
concatenate()
c_[]
r_[]
"""
a = np.floor(10 * np.random.random((2, 2)))
b = np.floor(10 * np.random.random((2, 2)))

np.vstack((a, b))
np.hstack((a, b))
np.column_stack((a, b))

a = np.array([4, 2])
b = np.array([3, 8])
np.column_stack((a, b))

"""
分割矩阵
hsplit()
vsplit()
"""
a = np.floor(10 * np.random.random((2, 12)))
np.hsplit(a, 3)
np.vsplit(a, 2)
