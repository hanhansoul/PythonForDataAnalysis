import numpy as np
import matplotlib.pyplot as plt

n = 20
Z = np.random.uniform(0, 1, n)
plt.axes([0.025, 0.025, 0.95, 0.95])

plt.pie(Z, explode=Z * .05, colors=['%f' % (i / float(n)) for i in range(n)])
plt.gca().set_aspect('equal')
plt.xticks([]), plt.yticks([])

plt.show()
