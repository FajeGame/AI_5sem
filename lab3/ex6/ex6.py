import os
import sys
import pandas as pd


def find_input_file(base_dir):
    for name in os.listdir(base_dir):
        if name.lower().endswith('.txt'):
            return os.path.join(base_dir, name)
    for name in os.listdir(base_dir):
        if name.lower().endswith('.csv'):
            return os.path.join(base_dir, name)
    return None


def main():
    base_dir = os.path.dirname(__file__)
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
    else:
        csv_path = find_input_file(base_dir)
    if not csv_path or not os.path.exists(csv_path):
        print('Не найден входной файл. Укажите путь: python ex6.py <path_to_txt_or_csv>')
        return

    # 1. читаем файл и задаем имена столбцов
    cols = ['index', 'year', 'month', 'day', 'min_t', 'average_t', 'max_t', 'rainfall']
    if str(csv_path).lower().endswith('.txt'):
        df = pd.read_csv(csv_path, sep=';', header=None, names=cols, engine='python')
    else:
        df = pd.read_csv(csv_path, header=None, names=cols)

    # 2. убираем index
    df = df.drop(columns=['index'])

    # 3. смотрим пропуски
    print('info():')
    df.info()
    na_counts = df.isna().sum().sort_values(ascending=False)
    print('\nЕсть ли пропуски:', int(na_counts.sum()) > 0)
    if na_counts.sum() > 0:
        print('Больше всего пропусков в столбце:', na_counts.index[0])

    # 4. год с наибольшим числом пропусков
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    mis_per_year = df.isna().groupby(df['year']).sum().sum(axis=1)
    if len(mis_per_year) > 0:
        year_max_miss = mis_per_year.idxmax()
        print('\nГод с наибольшим числом пропусков:', int(year_max_miss) if pd.notna(year_max_miss) else year_max_miss)

    # 5. собираем дату
    for c in ['month', 'day']:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']], errors='coerce')

    # 6. размах температур и дни без осадков (через цикл)
    for c in ['min_t', 'average_t', 'max_t', 'rainfall']:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df['temp_range'] = df['max_t'] - df['min_t']
    dry_before = []
    cur = 0
    for r in df['rainfall']:
        dry_before.append(cur)
        if pd.notna(r) and r > 0:
            cur = 0
        else:
            if pd.notna(r) and r == 0:
                cur += 1
            else:
                cur = cur  # оставим как есть для NaN
    df['dry_days_before'] = dry_before

    # 7. самый длинный период засухи (подряд нулевые осадки)
    max_len = 0
    max_end = -1
    cur_len = 0
    for i, r in enumerate(df['rainfall']):
        if pd.notna(r) and r == 0:
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
                max_end = i
        else:
            cur_len = 0
    if max_len > 0:
        start_i = max_end - max_len + 1
        start_date = df.iloc[start_i]['date']
        end_date = df.iloc[max_end]['date']
        print('\nСамая длинная засуха (дней):', max_len)
        print('Период:', start_date, '-', end_date)
    else:
        print('\nЗасух не найдено')

    # 8. по годам: средняя температура и сумма осадков
    yearly_avg_t = df.groupby('year')['average_t'].mean()
    yearly_rain = df.groupby('year')['rainfall'].sum()
    print('\nСреднегодовая температура (первые 10):')
    print(yearly_avg_t.head(10))
    print('\nГод с макс. температурой:', yearly_avg_t.idxmax())
    print('Год с мин. температурой:', yearly_avg_t.idxmin())
    print('\nСуммарные осадки по годам (первые 10):')
    print(yearly_rain.head(10))
    print('\nМакс. осадков в году:', yearly_rain.idxmax())
    print('Мин. осадков в году:', yearly_rain.idxmin())

    # 9. фильтры
    very_cold = df[df['average_t'] < -30]
    # используем побитовое & для Series
    hot_and_dry = df[(df['average_t'] > 27) & (df['dry_days_before'] > 3)]

    print('\nСредняя температура < -30 (первые 10):')
    print(very_cold.head(10))
    print('\nСредняя температура > 27 и дней без осадков > 3 (первые 10):')
    print(hot_and_dry.head(10))


if __name__ == '__main__':
    main()


