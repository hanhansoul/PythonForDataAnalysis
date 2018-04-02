import numpy as np

a = np.arange(12) ** 2
i = np.array([1, 1, 3, 8, 5])
print(a[i])
j = np.array([[3, 4], [9, 7]])
print(a[j])

palette = np.array([[0, 0, 0],
                    [255, 0, 0],
                    [0, 255, 0],
                    [0, 0, 255],
                    [255, 255, 255]])
image = np.array([[0, 1, 2, 0],
                  [0, 3, 4, 0]])
palette[image]

a = np.arange(12).reshape(3, 4)
i = np.array([[0, 1], [1, 2]])
j = np.array([[2, 1], [3, 3]])
print(a[i, j])
print(a[i, 2])
print(a[:, j])

#
time = np.linspace(20, 145, 5)
data = np.sin(np.arange(20)).reshape(5, 4)
print(time)
print(data)
ind = data.argmax(axis=0)
time_max = time[ind]
# data_max = data[ind, xrange(data.shape[1])]
