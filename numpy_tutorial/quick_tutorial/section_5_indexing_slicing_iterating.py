import numpy as np

a = np.arange(10) ** 3
print(a[2:5])
print(a[:6:2])
a[:6:2] = -1000
print(a)
print(a[::-1])


# 多为矩阵

def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print(b[2, 3])
print(b[0:5, 1])
print(b[:, 1])
print(b[1:3, :])

c = np.arange(12).reshape(2, 3, 2)
print(c.shape)
print(c[1, ...])
print(c[..., 1])

# 遍历
for element in c.flat:
    print(element)

