import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    filename = None
    for fn in os.listdir('.'):
        if fn.lower().endswith('.csv') and 'crime' in fn.lower():
            filename = fn
            break
    if filename is None:
        for fn in os.listdir('.'):
            if fn.lower().endswith('.csv'):
                filename = fn
                break
    if filename is None:
        print('CSV файл не найден в папке.', file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(filename, low_memory=False)

    # простое определение нужных колонок
    cols = {c.lower().strip(): c for c in df.columns}

    def pick(cands):
        for key, orig in cols.items():
            for c in cands:
                if c == key or c in key:
                    return orig
        return None

    vict_sex_col = pick(['vict sex', 'vict_sex', 'victim sex', 'sex'])
    crime_desc_col = pick(['crm cd desc', 'crime description', 'crime desc', 'offense'])
    vict_descent_col = pick(['vict descent', 'victim descent', 'descent', 'race'])
    area_name_col = pick(['area name', 'area', 'district', 'reporting district'])

    # 2) размерность
    print('shape:', df.shape)

    # 3) имена столбцов и типы
    print('columns:', list(df.columns))
    print('dtypes:')
    print(df.dtypes)

    # 4) уникальные
    nunique = df.nunique(dropna=True)
    print('nunique:')
    print(nunique)

    # 5) пропуски
    na_counts = df.isna().sum()
    print('na_counts:')
    print(na_counts)

    # 6) женщины vs мужчины (если колонка найдена)
    if vict_sex_col is not None:
        sex_counts = df[vict_sex_col].value_counts(dropna=True)
        f = int(sex_counts.get('F', 0) + sex_counts.get('Female', 0))
        m = int(sex_counts.get('M', 0) + sex_counts.get('Male', 0))
        print('victims_female:', f, 'victims_male:', m, 'female_more:', f > m)
    else:
        print('victim sex column not found')

    # 7) топ-10 преступлений и график
    if crime_desc_col is not None:
        top10 = df[crime_desc_col].value_counts().head(10)
        print('\ntop10 crimes:')
        print(top10)
        plt.figure(figsize=(9, 4))
        top10.sort_values(ascending=True).plot(kind='barh')
        plt.title('Top-10 crimes')
        plt.xlabel('count')
        plt.ylabel('crime')
        plt.tight_layout()
        plt.show()
    else:
        print('crime description column not found')

    # 8) по полу: какие преступления чаще у женщин/мужчин
    if crime_desc_col is not None and vict_sex_col is not None:
        pivot = (df[[crime_desc_col, vict_sex_col]]
                 .dropna()
                 .value_counts()
                 .rename('count')
                 .reset_index()
                 .pivot_table(index=crime_desc_col, columns=vict_sex_col, values='count', fill_value=0))
        # приведем к стандартным меткам если есть
        f_col = None
        m_col = None
        for c in pivot.columns:
            cl = str(c).strip().lower()
            if cl in ('f', 'female'):
                f_col = c
            if cl in ('m', 'male'):
                m_col = c
        if f_col is not None and m_col is not None:
            diff_f = (pivot[f_col] - pivot[m_col]).sort_values(ascending=False)
            diff_m = (pivot[m_col] - pivot[f_col]).sort_values(ascending=False)
            print('\nmore for females (top 10):')
            print(diff_f.head(10))
            print('\nmore for males (top 10):')
            print(diff_m.head(10))
        else:
            print('sex labels not standard, skip comparison by sex')
    else:
        print('cannot compare crimes by sex')

    # 9) кто чаще всего подвергается (по происхождению)
    if vict_descent_col is not None:
        descent_counts = df[vict_descent_col].value_counts(dropna=True)
        print('\nmost frequent victim descent:')
        print(descent_counts.head(10))
    else:
        print('victim descent column not found')

    # 10) районы: сортировка и график
    if area_name_col is not None:
        area_counts = df[area_name_col].value_counts()
        print('\nareas by crime count:')
        print(area_counts)
        # показать самый безопасный и самый опасный
        safest = area_counts.sort_values(ascending=True).head(5)
        dangerous = area_counts.sort_values(ascending=False).head(5)
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        safest.sort_values(ascending=True).plot(kind='barh', color='tab:green')
        plt.title('Safest areas (fewest crimes)')
        plt.xlabel('count')
        plt.ylabel('area')
        plt.subplot(1, 2, 2)
        dangerous.sort_values(ascending=True).plot(kind='barh', color='tab:red')
        plt.title('Most dangerous areas (most crimes)')
        plt.xlabel('count')
        plt.ylabel('area')
        plt.tight_layout()
        plt.show()
    else:
        print('area/district column not found')


if __name__ == '__main__':
    main()


