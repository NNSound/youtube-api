import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
cursor = c.execute("SELECT *  from COMPANY")
print(cursor.fetchone())
conn.close()