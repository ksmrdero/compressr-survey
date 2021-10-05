from sqlalchemy import create_engine
import urllib
import os


class SqlDb:
    def __init__(self) -> None:
        self.engine = self.start_engine()

    def start_engine(self):
        params = urllib.parse.quote_plus(os.getenv('SQL_CONNECTION_STRING'))
        conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
        return create_engine(conn_str, echo=True)

    def insert(self, imageSet, imageName, rank):

        with self.engine.connect() as con:
            statement = """INSERT INTO ranks (ImageSet, ImageName, Rank)
                    VALUES (%d, %d, %d);""" % (imageSet, imageName, rank)

            con.execute(statement)
