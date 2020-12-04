import sqlite3
from sqlite3 import Error
from db_connection import create_connection

DATABASE_PATH = r""
TABLE_NAME = "stocks"

sql_create_table_command = """ CREATE TABLE IF NOT EXISTS {} (
                            stock VARCHAR(10) PRIMARY KEY
                            ); """.format(TABLE_NAME)

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

if __name__ == '__main__':

    conn = create_connection(DATABASE_PATH)
    create_table(conn, sql_create_table_command)
    conn.close()
