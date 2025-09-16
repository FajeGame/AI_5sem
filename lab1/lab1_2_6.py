import numpy as np

a = np.array([1., 7., 8., 2., 0.1, 3., 15., 2.5])
k = 4
idx = np.argpartition(a, k)[:k]
print(np.sort(a[idx]))


