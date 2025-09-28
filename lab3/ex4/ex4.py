import pandas as pd
import numpy as np


def fh_to_status(x: float) -> str:
    # Free: 1.0–2.5; Partly Free: 3.0–5.0; Not Free: 5.5–7.0
    if pd.isna(x):
        return np.nan  # останется NaN
    if x <= 2.5:
        return "free"
    if x <= 5.0:
        return "partly free"
    return "not free"


def main() -> None:
    # 1) загрузка (без тотального dropna)
    polit = pd.read_csv("polit.csv", low_memory=False, index_col=0, decimal=",")

    # приведение типов (чтобы фильтры работали)
    for col in ["fh09", "polity09", "fparl08", "corr0509", "gini"]:
        if col in polit.columns:
            polit[col] = pd.to_numeric(polit[col], errors="coerce")
    for col in ["afri", "lati"]:
        if col in polit.columns:
            polit[col] = pd.to_numeric(polit[col], errors="coerce").fillna(0).astype(int)

    # 2) fh09 > 5 (только где fh09 не NaN)
    sel1 = polit.dropna(subset=["fh09"]) 
    sel1 = sel1[sel1["fh09"] > 5]
    print("fh09>5 rows:", len(sel1))

    # 3) afri==1 и fparl08 > 30
    sel2 = polit.dropna(subset=["fparl08"]) if "fparl08" in polit.columns else polit
    if "afri" in sel2.columns:
        sel2 = sel2[(sel2["afri"] == 1) & (sel2["fparl08"] > 30)]
    else:
        sel2 = sel2.iloc[0:0]
    print("afri & fparl08>30 rows:", len(sel2))

    # 4) (afri==1 или lati==1) и polity09 >= 8
    needed = [c for c in ["afri", "lati", "polity09"] if c in polit.columns]
    sel3 = polit.dropna(subset=["polity09"]) if "polity09" in polit.columns else polit
    if all(c in sel3.columns for c in ["afri", "lati"]):
        sel3 = sel3[((sel3["afri"] == 1) | (sel3["lati"] == 1)) & (sel3["polity09"] >= 8)]
    else:
        sel3 = sel3.iloc[0:0]
    print("(afri|lati) & polity09>=8 rows:", len(sel3))

    # 5) corr_round = round(corr0509, 2)
    polit["corr0509"] = pd.to_numeric(polit["corr0509"], errors="coerce")
    polit["corr_round"] = polit["corr0509"].round(2)

    # 6) fh_status по fh09
    polit["fh_status"] = polit["fh09"].apply(fh_to_status)

    # 7) агрегирование gini по fh_status
    grp_df = polit.dropna(subset=["fh_status", "gini"]) if "gini" in polit.columns else polit.iloc[0:0]
    agg = grp_df.groupby("fh_status")["gini"].agg(["min", "mean", "max"]).reset_index()
    print("\nGini by fh_status:")
    print(agg)

    # 8) сохранить группы в отдельные csv
    for status, grp in polit.groupby("fh_status"):
        if pd.isna(status):
            fname = "polit_status_nan.csv"
        else:
            fname = f"polit_{status.replace(' ', '_')}.csv"
        grp.to_csv(fname, index=False)


if __name__ == "__main__":
    main()


