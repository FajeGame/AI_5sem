import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def graph1():
    # гистограмма с KDE
    np.random.seed(42)
    # создаем данные с двумя пиками
    data1 = np.random.normal(1.5, 0.3, 200)
    data2 = np.random.normal(4.5, 0.4, 300)
    data3 = np.random.normal(6.0, 0.2, 100)
    petal_length = np.concatenate([data1, data2, data3])
    
    plt.figure(figsize=(8, 5))
    
    # гистограмма
    plt.hist(petal_length, bins=30, density=True, alpha=0.7, color='lightcoral', edgecolor='black')
    
    # KDE
    kde = stats.gaussian_kde(petal_length)
    x_kde = np.linspace(0, 8, 200)
    plt.plot(x_kde, kde(x_kde), color='darkred', linewidth=2)
    
    plt.xlabel('petal_length')
    plt.ylabel('density')
    plt.xlim(0, 8)
    plt.ylim(0, 0.25)
    plt.show()

def graph2():
    # линейный график с встроенным подграфиком
    x = np.linspace(0, 100, 100)
    y = 2 * x  # y = 2x
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # основной график
    ax.plot(x, y, 'b-', linewidth=2)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 200)
    
    # встроенный подграфик
    ax_inset = fig.add_axes([0.6, 0.6, 0.25, 0.25])
    ax_inset.plot(x, y, 'b-', linewidth=2)
    ax_inset.set_xlabel('x')
    ax_inset.set_ylabel('y')
    ax_inset.set_xlim(0, 100)
    ax_inset.set_ylim(0, 200)
    
    plt.show()

def graph3():
    # два подграфика рядом
    x = np.linspace(0, 100, 100)
    y = 2 * x  # y = 2x
    z = x**2   # z = x²
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # левый подграфик - толстая синяя линия
    ax1.plot(x, y, 'b-', linewidth=8)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 200)
    
    # правый подграфик - красная пунктирная линия
    ax2.plot(x, z, 'r--', linewidth=2)
    ax2.set_xlabel('x')
    ax2.set_ylabel('z')
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 10000)
    
    plt.tight_layout()
    plt.show()

def main():
    graphs = {
        '1': ('Гистограмма с KDE', graph1),
        '2': ('Линейный график с встроенным подграфиком', graph2),
        '3': ('Два подграфика рядом', graph3)
    }
    
    while True:
        print("\nВыберите график:")
        for key, (name, _) in graphs.items():
            print(f"{key}. {name}")
        print("0. Выход")
        
        choice = input("\nВведите номер: ")
        
        if choice == '0':
            break
        elif choice in graphs:
            print(f"Показываю: {graphs[choice][0]}")
            graphs[choice][1]()
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
