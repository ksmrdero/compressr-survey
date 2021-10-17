import os
import urllib
from sqlalchemy import create_engine
from datetime import datetime


class SqlDb:
    def __init__(self) -> None:
        self.engine = self.start_engine()

    def start_engine(self):
        params = urllib.parse.quote_plus(
            str(os.getenv('SQL_CONNECTION_STRING')))
        conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
        return create_engine(conn_str, echo=True)

    def insert(self, imageSet, imageName, rank, model):
        now = datetime.now()
        date = now.strftime('%Y-%m-%d %H:%M:%S')
        with self.engine.connect() as con:
            statement = """INSERT INTO ranks (ImageSet, ImageName, Rank, Date, Model)
                    VALUES (%d, %d, %d, '%s', '%s');""" % (imageSet, imageName, rank, date, model)

            con.execute(statement)
