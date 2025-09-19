import numpy as np

a1 = np.array([200., 300., np.nan, np.nan, np.nan, 700.])
print(a1[~np.isnan(a1)])

a2 = np.array([[1., 2., 3.], [np.nan, 0., np.nan], [6., 7., np.nan]])
print(a2[~np.isnan(a2)])


