import numpy as np

a = np.arange(6)
print(a)

b = np.arange(12).reshape(4, 3)
print(b)

c = np.arange(24).reshape(2, 3, 4)
print(c)

print(np.arange(10000).reshape(100, 100))
