import sqlite3
from sqlite3 import Error
from db_connection import create_connection

DATABASE_PATH = r""

TABLE_NAME = "stocks"
COLUMN_NAME = "is_tradeable_on_rh"
DATA_TYPE = "BOOLEAN"

sql_add_column_command = """ALTER TABLE {} ADD COLUMN {} {}
                         """.format(TABLE_NAME, COLUMN_NAME, DATA_TYPE)

def add_column(conn, column_sql):
    cur = conn.cursor()
    cur.execute(column_sql)

if __name__ == '__main__':
    conn = create_connection(DATABASE_PATH)
    add_column(conn, sql_add_column_command)
    conn.close()
