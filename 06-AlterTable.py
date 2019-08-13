import sqlite3

conn = sqlite3.connect("Demo.db")

query = "Alter table test add Address text(40)"
conn.execute(query)
print("table altered..")
conn.commit()

conn.close()
