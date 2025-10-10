from sqlalchemy import create_engine

engine = create_engine(url="sqlite:///database.sqlite3", echo=True)
