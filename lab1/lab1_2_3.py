import numpy as np

a = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])
u, counts = np.unique(a, return_counts=True)
print(u)
print(counts)


