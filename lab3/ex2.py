import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    # данные
    data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
            ["Гайка", "Gadget Hackwrench", "mouse", None],
            ["Дейл", "Dale", "chipmunk", "1"],
            ["Рокфор", "Monterey Jack", "mouse", "0.8"],
            ["Чип", "Chip", "chipmunk", "0.2"]]

    # 1) датафрейм и cheer как float
    df = pd.DataFrame(data, columns=["ru_name", "en_name", "class", "cheer"])
    df["cheer"] = pd.to_numeric(df["cheer"], errors="coerce")

    # 2) число строк
    print("rows:", len(df))

    # 3) число не-NaN в cheer
    print("cheer non-NaN:", df["cheer"].notna().sum())

    # 4) элемент (3-я строка, 2-й столбец)
    print("[3,2]:", df.iloc[2, 1])

    # 5) df1: строки 2..4, столбцы 1..3 (вкл.)
    df1 = df.iloc[1:4, 0:3]
    print("\ndf1:")
    print(df1)

    # 6) имена столбцов
    df.columns = ["ru_name", "en_name", "class", "cheer"]

    # 7) лог cheer
    df["logcheer"] = np.log(df["cheer"])  # NaN останутся NaN

    # 8) значения и частоты по class
    counts = df["class"].value_counts()
    x = counts.index.to_numpy()
    y = counts.values

    plt.figure(figsize=(5, 3))
    plt.bar(x, y)
    plt.title("Class counts")
    plt.xlabel("class")
    plt.ylabel("count")
    plt.tight_layout()
    plt.show()

    main()



