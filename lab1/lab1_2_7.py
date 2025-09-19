import numpy as np

a = np.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49])
v = 3.09066280756759
print(a[np.argmin(np.abs(a - v))])


