
import exceptions
import traceback
from os import environ
from sqlalchemy import create_engine
import logging.config
from dotenv import load_dotenv
from config.settings import dotenv_path
from io import StringIO
import csv

logging.config.fileConfig("common/log_conf.ini",disable_existing_loggers=False)
_DBHandler_logger=logging.getLogger('%s.%s' % (__name__, 'DBHandler'))

load_dotenv(dotenv_path)
from config import settings

class DBHandler():

    def __init__(self):

        self.db_uri = environ.get('SQLALCHEMY_DATABASE_URI').format(settings.DB_DRIVER,
                                                                    settings.DB_USER,
                                                                    settings.DB_PASS,
                                                                    settings.DB_HOST,
                                                                    settings.DB_NAME)
        self.engine = create_engine(self.db_uri, echo=True)

    def psql_insert_copy(self, table, conn, keys, data_iter):
        dbapi_conn = conn.connection
        with dbapi_conn.cursor() as cur:
            s_buf = StringIO()
            writer = csv.writer(s_buf)
            writer.writerows(data_iter)
            s_buf.seek(0)

            columns = ', '.join('"{}"'.format(k) for k in keys)
            if table.schema:
                table_name = '{}.{}'.format(table.schema, table.name)
            else:
                table_name = table.name

            sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
                table_name, columns)
            cur.copy_expert(sql=sql, file=s_buf)

    def save(self,df, table):
        df.to_sql(table, self.engine, if_exists='replace', method=self.psql_insert_copy)
