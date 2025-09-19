import matplotlib.pyplot as plt
import numpy as np

# данные для графика
x = np.linspace(0, 1, 100)  # x от 0 до 1
y1 = np.sin(2 * np.pi * x)  # синус для синей линии
y2 = np.cos(2 * np.pi * x)  # косинус для красной

# создаем фигуру
fig, ax = plt.subplots(figsize=(10, 6))

# 1. заголовок
ax.set_title('Элементы изображения (Title)', fontsize=14)

# 2. подписи осей
ax.set_xlabel('Подпись оси ОХ (X axis label)')
ax.set_ylabel('Подпись оси ОУ (Y axis label)')

# 3. настройка осей
ax.set_xlim(0, 1)
ax.set_ylim(-1.5, 1.5)

# 4. основные деления
ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_yticks([-1, 0, 1])

# 5. промежуточные деления
ax.set_xticks([0.125, 0.375, 0.625, 0.875], minor=True)
ax.set_yticks([-0.5, 0.5], minor=True)

# 6. подписи основных делений
ax.tick_params(axis='both', which='major', labelsize=10)

# 7. подписи промежуточных делений
ax.set_xticks([0.125, 0.375, 0.625, 0.875])
ax.tick_params(axis='x', which='major', labelsize=8)

# 8. сетка
ax.grid(True, which='major', linestyle='--', alpha=0.7)
ax.grid(True, which='minor', linestyle=':', alpha=0.5)

# 9. линии графиков
ax.plot(x, y1, 'b-', linewidth=2, label='Синяя линия')
ax.plot(x, y2, 'r-', linewidth=2, label='Красная линия')

# 10. маркеры
marker_x = [0.1, 0.3, 0.5, 0.7, 0.9]
marker_y = [np.cos(2 * np.pi * xi) for xi in marker_x]
ax.scatter(marker_x, marker_y, c='red', s=50, alpha=0.8)

# 11. линии осей координат
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

# 12. легенда
ax.legend(loc='upper right')

# 13. координатная плоскость
ax.set_aspect('auto')

plt.tight_layout()
plt.show()

print("График готов!")
