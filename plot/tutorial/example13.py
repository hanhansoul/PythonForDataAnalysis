import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    # return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
    return x + y


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

f(X, Y)

plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
plt.clabel(C, inline=1, fontsize=10)

plt.show()

# Z = np.random.randint(1, 10, 10).reshape(2, 5)
# print(Z)
# plt.contour(Z)
