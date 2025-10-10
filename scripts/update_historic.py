import os
import pathlib
import pandas as pd

from datetime import datetime

from sqlalchemy import text

from app.core.db import engine
from app.core.config import get_settings

settings = get_settings()


def get_value_date(filename: pathlib.Path, sheet_name: str):
    df = pd.read_excel(
        filename,
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
    for filename in pathlib.Path(settings.historic_path).iterdir():
        if filename.is_file() and filename.suffix == ".xls":
            excel = pd.read_excel(
                filename,
                usecols="B,G",
                header=8,
                index_col=0,
                skiprows=[9],
                nrows=21,
                sheet_name=None,
            )

            insert_rates = []
            for sheet_name, df in excel.items():
                date = get_value_date(filename=filename, sheet_name=sheet_name)
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
