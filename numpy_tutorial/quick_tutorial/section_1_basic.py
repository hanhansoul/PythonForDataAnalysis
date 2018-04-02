import numpy as np

a = np.arange(15).reshape(3, 5)
print(a.shape)
print(a.ndim)  # ndarray的维数
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.data)

# list
a = np.array([2, 3, 4])
b = np.array([1.2, 3.5, 5.2])

c = np.array([(1.5, 2, 3), (4, 5, 6)])

d = np.array([[1, 2], [3, 4]], dtype=complex)


z = np.zeros((3, 4, 3))

o = np.ones((2, 3, 4), dtype=np.int)

l1 = np.linspace(0, 2, 9)
x = np.linspace(0, 2 * np.pi, 100)
l2 = np.sin(x)
