import pandas as pd

from datetime import datetime


def main():
    df = pd.read_excel(
        "./input/historic/2_1_2c25_smc.xls",
        usecols="D",
        header=None,
        nrows=1,
        skiprows=4,
        sheet_name="26092025",
    )
    value_date = datetime.strptime(
        str(df.iloc[0, 0]).lstrip("Fecha Valor: "), "%d/%m/%Y"
    ).date()
    print(value_date)
    df = pd.read_excel(
        "./input/historic/2_1_2c25_smc.xls",
        usecols="B,G",
        header=8,
        index_col=0,
        skiprows=[9],
        nrows=21,
        sheet_name="26092025",
    )
    print(df.loc["USD"].iloc[0])


if __name__ == "__main__":
    main()
