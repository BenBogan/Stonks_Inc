import sqlite3
from sqlite3 import Error

DATABASE_PATH = r"" #The location/name of the database

def create_connection(db_file):
    """ create a database connection to the SQLite database specified
        return: Connection object
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

if __name__ == '__main__':
    conn = create_connection(DATABASE_PATH)
    conn.close()
