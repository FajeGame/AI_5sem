import matplotlib.pyplot as plt
import numpy as np

def graph1():
    # вертикальная столбчатая диаграмма (синяя)
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22, 18, 9, 8, 7.5, 6.5]
    
    plt.figure(figsize=(8, 5))
    plt.bar(languages, popularity, color='blue')
    plt.title('Popularity of Programming Language Worldwide, Oct 2017 compared to a year ago')
    plt.xlabel('Languages')
    plt.ylabel('Popularity')
    plt.ylim(0, 25)
    plt.grid(True, alpha=0.3, color='red')
    plt.show()

def graph2():
    # горизонтальная столбчатая диаграмма (зеленая)
    languages = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
    popularity = [22, 17, 9, 8, 7.5, 6.5]
    
    plt.figure(figsize=(8, 5))
    plt.barh(languages, popularity, color='green')
    plt.title('Popularity of Programming Language Worldwide, Oct 2017 compared to a year ago')
    plt.xlabel('Popularity')
    plt.ylabel('Languages')
    plt.xlim(0, 25)
    plt.grid(True, alpha=0.3, color='red')
    plt.show()

def graph3():
    # цветная столбчатая диаграмма
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22, 17, 9, 8, 7.5, 6.5]
    colors = ['red', 'black', 'green', 'blue', 'yellow', 'lightblue']
    
    plt.figure(figsize=(8, 5))
    plt.bar(languages, popularity, color=colors)
    plt.title('Popularity of Programming Language Worldwide, Oct 2017 compared to a year ago')
    plt.xlabel('Languages')
    plt.ylabel('Popularity')
    plt.ylim(0, 25)
    plt.grid(True, alpha=0.3, color='red')
    plt.show()

def graph4():
    # столбчатая диаграмма с точными значениями
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(languages, popularity, color='blue')
    plt.title('Popularity of Programming Language Worldwide, Oct 2017 compared to a year ago')
    plt.xlabel('Languages')
    plt.ylabel('Popularity')
    plt.ylim(0, 25)
    plt.grid(True, alpha=0.3, color='red')
    
    # добавляем значения на столбцы
    for bar, value in zip(bars, popularity):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                f'{value:.6f}', ha='center', va='bottom')
    plt.show()

def graph5():
    # простая столбчатая диаграмма с разной шириной столбцов
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22, 17, 9, 8, 7.5, 6.5]
    widths = [0.8, 0.6, 0.4, 0.3, 0.2, 0.1]  # разная ширина для каждого столбца
    
    plt.figure(figsize=(8, 5))
    plt.bar(languages, popularity, width=widths, color='blue')
    plt.title('Popularity of Programming Language Worldwide, Oct 2017 compared to a year ago')
    plt.xlabel('Languages')
    plt.ylabel('Popularity')
    plt.ylim(0, 25)
    plt.grid(True, alpha=0.3, color='red')
    plt.show()

def graph6():
    # группированная столбчатая диаграмма
    persons = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_scores = [22, 30, 33, 30, 26]
    women_scores = [25, 32, 30, 34, 29]
    
    x = np.arange(len(persons))
    width = 0.35
    
    plt.figure(figsize=(8, 5))
    plt.bar(x - width/2, men_scores, width, label='Men', color='green')
    plt.bar(x + width/2, women_scores, width, label='Women', color='red')
    
    plt.title('Scores by person')
    plt.xlabel('Person')
    plt.ylabel('Scores')
    plt.xticks(x, persons)
    plt.legend()
    plt.ylim(0, 35)
    plt.grid(True, alpha=0.3)
    plt.show()

def graph7():
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [31.3, 24.8, 12.4, 11.3, 10.8, 9.4]
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
    
    plt.figure(figsize=(8, 6))
    plt.pie(popularity, labels=languages, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('Popularity of Programming Language Worldwide, Oct 2017 compared to a year ago')
    plt.axis('equal')
    plt.show()

def graph8():
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [31.3, 24.8, 12.4, 11.3, 10.8, 9.4]
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
    
    plt.figure(figsize=(8, 6))
    plt.pie(popularity, labels=languages, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('Popularity of Programming Language Worldwide, Oct 2017 compared to a year ago')
    plt.axis('equal')
    plt.show()

def main():
    graphs = {
        '1': ('Вертикальная столбчатая диаграмма (синяя)', graph1),
        '2': ('Горизонтальная столбчатая диаграмма (зеленая)', graph2),
        '3': ('Цветная столбчатая диаграмма', graph3),
        '4': ('Столбчатая диаграмма с точными значениями', graph4),
        '5': ('Простая столбчатая диаграмма', graph5),
        '6': ('Группированная столбчатая диаграмма', graph6),
        '7': ('Первая круговая диаграмма', graph7),
        '8': ('Вторая круговая диаграмма', graph8)
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
