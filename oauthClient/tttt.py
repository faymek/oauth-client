import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("select * from Student")
values = c.fetchall()
print(values)
c.close()
conn.commit()
conn.close()
