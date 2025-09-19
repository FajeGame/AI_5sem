import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 5, 100)
y = x**2 - x - 6

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y, 'b-', linewidth=2, label='y(x) = x² - x - 6')
ax.axhline(y=0, color='r', linestyle='--', alpha=0.7, label='y = 0')
ax.plot(-2, 0, 'ro', markersize=8, label='Корень x = -2')
ax.plot(3, 0, 'ro', markersize=8, label='Корень x = 3')
ax.axvline(x=-2, color='g', linestyle=':', alpha=0.5)
ax.axvline(x=3, color='g', linestyle=':', alpha=0.5)

ax.set_xlim(-4, 5)
ax.set_ylim(-8, 10)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('График функции y(x) = x² - x - 6')
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.show()

print("Корни: x₁ = -2, x₂ = 3")
