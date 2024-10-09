import sqlite3

conn = sqlite3.connect("connect4.sqlite")
c = conn.cursor()

with open("connect4_schema.sql", "r") as sql_file:
    sql = sql_file.read()

try:
    c.executescript(sql)
    conn.commit()
except sqlite3.Error as e:
    print(f"An error has occured {e}")
finally:
    conn.rollback()

conn.close()
