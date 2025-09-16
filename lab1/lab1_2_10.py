import numpy as np

# a) x^2 - 4x + 7
coeffs_a = np.array([1, -4, 7])
roots_a = np.roots(coeffs_a)
print(roots_a)

# b) x^4 - 11x^3 + 9x^2 + 11x - 10
coeffs_b = np.array([1, -11, 9, 11, -10])
roots_b = np.roots(coeffs_b)
print(roots_b)


