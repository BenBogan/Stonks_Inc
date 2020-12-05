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

# COLUMN_NAME =
# DATA_TYPE =
# sql_add_column_command = """ALTER TABLE Stocks ADD COLUMN {} {}
#                          """.format(COLUMN_NAME, DATA_TYPE)

SQL_COMMAND = """INSERT INTO Stocks VALUES ("AAPL")"""

conn = create_connection(DATABASE_PATH)
cur = conn.cursor()

cur.execute(sql_add_column_command)

cur.execute("SELECT * FROM Stocks")
print(cur.fetchall())

while(True):
    commit = input("commit? (y/n)")
    if commit == "y":
        conn.commit()
        break
    elif commit == "n":
        break
    else:
        print("say y or n faggot")

cur.close()
conn.close()
