import numpy as np

a = np.arange(15).reshape(3, 5)
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(a.size)
print(type(a))

b = np.array([6, 7, 8])
print(b)

# array创建

print(np.zeros((3, 4)))
print(np.zeros((3, 4), dtype=int))
print(np.ones((2, 3, 4), dtype=np.int16))
print(np.empty((2, 3)))
# arange() / linspace()
print(np.arange(10, 30, 5))
print(np.linspace(0, 2, 9))


