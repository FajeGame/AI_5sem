import pandas as pd


def main() -> None:
    s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
    print('Series s:')
    print(s)

    # 4 по 'd'
    explicit_4 = s['d']
    print('\n1) Значение по явному индексу \"d\":', explicit_4)

    # 2 по позиции
    implicit_2 = s.iloc[1]
    print('2) Значение по неявному индексу (позиция 1):', implicit_2)

    # добавляю f=6
    s['f'] = 6
    print('3) После добавления элемента (f=6):')
    print(s)

    # срез 3..5
    slice_345 = s.iloc[2:5]
    print('4) Срез значений 3, 4, 5:')
    print(slice_345)

    # DataFrame col1, col2
    data = [[1, 2], [5, 3], [3.7, 4.8]]
    df = pd.DataFrame(data, columns=['col1', 'col2'])
    print('\nDataFrame df:')
    print(df)

    # беру 3.7
    elem_37 = df.iloc[2, 0]
    print('\n6) Элемент 3.7 (df.iloc[2, 0]):', elem_37)

    # 3 -> 9 (строка 1, col2)
    df.loc[1, 'col2'] = 9
    print('7) После изменения элемента 3 на 9:')
    print(df)

    # строки 1 и 2
    rows_1_2 = df.loc[1:2]
    print('8) Срез строк с индексами 1 и 2:')
    print(rows_1_2)

    # col3 = col1*col2
    df['col3'] = df['col1'] * df['col2']
    print('9) После добавления col3 = col1 * col2:')
    print(df)

    main()


