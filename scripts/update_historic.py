import pandas as pd

from datetime import datetime

excel_path = "./input/historic/2_1_2c25_smc.xls"


def get_value_date(sheet_name: str):
    df = pd.read_excel(
        excel_path,
        usecols="D",
        header=None,
        nrows=1,
        skiprows=4,
        sheet_name=sheet_name,
    )
    value_date = datetime.strptime(
        str(df.iloc[0, 0]).lstrip("Fecha Valor: "), "%d/%m/%Y"
    ).date()
    return value_date


def main():
    excel = pd.read_excel(
        excel_path,
        usecols="B,G",
        header=8,
        index_col=0,
        skiprows=[9],
        nrows=21,
        sheet_name=["26092025", "24092025"],
    )
    for sheet_name, df in excel.items():
        print(get_value_date(sheet_name=sheet_name))
        print(df.loc["USD"].iloc[0])


if __name__ == "__main__":
    main()
