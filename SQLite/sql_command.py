from functions.db_connection import create_connection

DATABASE_PATH = r"db\main.db" #The location/name of the database
#Do this one to just make the table and add the single primary key
# SQL_COMMAND = """CREATE TABLE IF NOT EXISTS Stocks (
#                     ticker VARCHAR(10),
#                     PRIMARY KEY (ticker)
#                     );"""

#Do this to query
# SQL_COMMAND = """SELECT * FROM Stocks"""

#Do this to put a new row in (not working)
SQL_COMMAND = """INSERT INTO Stocks VALUES ("AAPL")"""

conn = create_connection(DATABASE_PATH)
cur = conn.cursor()

cur.execute(SQL_COMMAND)

cur.close()
conn.close()
