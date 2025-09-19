import matplotlib.pyplot as plt
import numpy as np

def f(x):
    try:
        base = 1 + np.tan(1/(1 + np.sin(x)**2))
        arg = (x**2 + 1) * np.exp(-np.abs(x)/10)
        return np.log(arg) / np.log(base)
    except:
        return np.nan

x = np.linspace(-10, 10, 1000)
y = [f(xi) for xi in x]

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('log_{1+tan(1/(1+sin²(x)))} ((x²+1) * exp(-|x|/10))')
plt.grid(True, alpha=0.3)
plt.show()
