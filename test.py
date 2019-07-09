import sqlite3
import time

conn = sqlite3.connect('/home/faymek/oauth-client/oauthClient/test.db')
c = conn.cursor()
c.execute("select * from Student")
values = c.fetchall()
for v in values:
    print(v)
#print(values)
c.close()
conn.commit()
conn.close()
