import matplotlib.pyplot as plt
import numpy as np

def graph1():
    x = np.linspace(0, 50, 100)
    y = 3 * x
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.title('Draw a line.')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.grid(True, alpha=0.3)
    plt.show()

def graph2():
    x = [10, 20, 30]
    y1 = [20, 40, 10]
    y2 = [40, 10, 30]
    plt.figure(figsize=(8, 5))
    plt.plot(x, y1, 'b-', linewidth=3, label='line1-width-3')
    plt.plot(x, y2, 'r-', linewidth=5, label='line2-width-5')
    plt.title('Two or more lines with different widths and colors with suitable legends')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

def graph3():
    x = [10, 20, 30]
    y1 = [20, 40, 10]
    y2 = [40, 10, 30]
    plt.figure(figsize=(8, 5))
    plt.plot(x, y1, 'b:', linewidth=2, label='line1-dotted')
    plt.plot(x, y2, 'r--', linewidth=2, label='line2-dashed')
    plt.title('Plot with two or more lines with different styles')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

def graph4():
    x = [1, 4, 5, 6, 7]
    y = [2, 6, 3, 6, 3]
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'r:', linewidth=2, marker='o', markersize=8, 
             markerfacecolor='blue', markeredgecolor='blue')
    plt.title('Display marker')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.grid(True, alpha=0.3)
    plt.show()

def graph5():
    x1 = [3, 4, 5, 7, 9]
    y1 = [2, 6, 10.5, 20, 22]
    x2 = [2, 3, 5, 6, 8]
    y2 = [1, 5, 10, 18, 20]
    
    plt.figure(figsize=(8, 5))
    plt.scatter(x1, y1, c='red', marker='o', s=50, label='Series 1')
    plt.scatter(x2, y2, c='blue', marker='*', s=100, label='Series 2')
    plt.xlim(0, 10)
    plt.ylim(0, 30)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

def graph6():
    dates = ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07']
    closing_values = [772.5, 776.4, 776.5, 777.0, 774.8]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, closing_values, 'r-o', linewidth=2, markersize=6)
    plt.title('Closing stock value of Alphabet Inc.')
    plt.xlabel('Date')
    plt.ylabel('Closing Value')
    plt.ylim(772, 777.5)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    graphs = {
        '1': ('Простая линия', graph1),
        '2': ('Две линии с разной шириной и цветом', graph2),
        '3': ('Две линии с разными стилями', graph3),
        '4': ('Отображение маркеров', graph4),
        '5': ('Точечный график', graph5),
        '6': ('График акций Alphabet', graph6)
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
