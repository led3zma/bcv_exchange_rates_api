import pandas as pd

from datetime import datetime

from sqlalchemy import text

from app.core.db import engine

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
    with engine.connect() as conn:
        conn.execute(
            text(
                """CREATE TABLE IF NOT EXISTS rate (
                 id INTEGER PRIMARY KEY,
                 value_date DATE NOT NULL UNIQUE,
                 rate FLOAT NOT NULL
                 )"""
            )
        )
        conn.commit()
    excel = pd.read_excel(
        excel_path,
        usecols="B,G",
        header=8,
        index_col=0,
        skiprows=[9],
        nrows=21,
        sheet_name=["26092025", "24092025"],
    )

    insert_rates = []
    for sheet_name, df in excel.items():
        date = get_value_date(sheet_name=sheet_name)
        value = df.loc["USD"].iloc[0]
        print(date)
        print(value)
        insert_rates.append({"date": date, "value": value})

    with engine.connect() as conn:
        conn.execute(
            text(
                """INSERT OR IGNORE INTO rate (value_date,rate) VALUES (:date,:value)"""
            ),
            insert_rates,
        )
        conn.commit()


if __name__ == "__main__":
    main()
