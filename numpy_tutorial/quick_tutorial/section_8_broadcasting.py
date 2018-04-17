import numpy as np

x = np.arange(4)
xx = x.reshape(4, 1)
y = np.ones(5)
z = np.ones((3, 4))

a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([1.0, 2.0, 3.0])
a[:, np.newaxis] + b