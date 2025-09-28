import os
import sys
import pandas as pd


def normalize_platforms(df, col):
    # просто приводим названия платформ к одному виду
    mapping = {
        "XOne": "Xbox One",
        "XB": "Xbox",
        "XBOX": "Xbox",
        "X360": "X360",
        "PS": "PS",
        "PS1": "PS",
        "PS2": "PS2",
        "PS3": "PS3",
        "PS4": "PS4",
        "PS5": "PS5",
        "PSP": "PSP",
        "PSV": "PSV",
        "WiiU": "Wii U",
        "Wii": "Wii",
        "GC": "GC",
        "N64": "N64",
        "NES": "NES",
        "SNES": "SNES",
        "GB": "GB",
        "GBA": "GBA",
        "DS": "DS",
        "3DS": "3DS",
        "PC": "PC",
        "DC": "DC",
        "SAT": "SAT",
        "GEN": "GEN",
        "2600": "2600",
        "SCD": "SCD",
        "TG16": "TG16",
        "3DO": "3DO",
        "GG": "GG",
        "NG": "NG",
    }
    return df[col].astype(str).str.strip().map(lambda x: mapping.get(x, x))


def count_distinct_vowels(text, vowels):
    # считаем разные гласные в строке
    if not isinstance(text, str):
        return 0
    s = text.lower()
    return len({ch for ch in s if ch in vowels})


def main():
    base_dir = os.path.dirname(__file__)
    vgsales_path = os.path.join(base_dir, "vgsales.csv")
    metacritic_path = os.path.join(base_dir, "metacritic_games.csv")

    # читаем файлы
    vgs = pd.read_csv(vgsales_path)
    meta = pd.read_csv(metacritic_path)

    # приводим тип года и платформы
    vgs["Year"] = pd.to_numeric(vgs["Year"], errors="coerce")
    vgs["Platform_norm"] = normalize_platforms(vgs, "Platform")
    meta["platform_norm"] = normalize_platforms(meta, "platform")

    # 1) все платформы
    platforms = (
        vgs.loc[vgs["Platform"].notna(), "Platform"].astype(str).str.strip().unique()
    )
    platforms_sorted = sorted(platforms)
    print("1) Платформы (из vgsales):")
    print(", ".join(platforms_sorted))
    print()

    # 2) добавляем рейтинг из metacritic по name+platform
    vgs["_key_name"] = vgs["Name"].astype(str).str.strip().str.lower()
    meta["_key_name"] = meta["name"].astype(str).str.strip().str.lower()

    vgs_copy = vgs.copy()
    merged = vgs_copy.merge(
        meta[["_key_name", "platform_norm", "rating"]],
        left_on=["_key_name", "Platform_norm"],
        right_on=["_key_name", "platform_norm"],
        how="left",
    )
    merged.rename(columns={"rating": "metacritic_rating"}, inplace=True)

    print("2) Добавлен столбец metacritic_rating (пример 10 строк):")
    print(merged[["Name", "Platform", "metacritic_rating"]].head(10))
    print()

    # 3) игры с M и год >= 2012
    filtered = merged[(merged["metacritic_rating"] == "M") & (merged["Year"] >= 2012)]
    print("3) Игры с рейтингом 'M' и годом >= 2012:")
    if filtered.empty:
        print("Нет игр, удовлетворяющих условиям.")
    else:
        print(filtered[["Name", "Platform", "Year", "Genre", "metacritic_rating"]].to_string(index=False))
    print()

    # 4) описательная статистика
    print("4) Описательные статистики (числовые столбцы):")
    if filtered.empty:
        print("—")
    else:
        numeric_cols = filtered.select_dtypes(include=["number"]).columns
        print(filtered[numeric_cols].describe())
    print()

    # 5) жанры с >=3 разными гласными
    vowels = set("aeiouy")
    genres = vgs["Genre"].dropna().astype(str)
    mask = genres.apply(lambda g: count_distinct_vowels(g, vowels) >= 3)
    genres_to_count = genres[mask]
    counts = genres_to_count.value_counts()
    print("5) Жанры (>=3 различных гласных) с количеством игр:")
    for genre, cnt in counts.items():
        print(f"{genre} - {cnt}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Ошибка выполнения: {exc}", file=sys.stderr)
        raise


