import sqlite3

conn = sqlite3.connect("Demo.db")

print("Database Opened...")

query = "insert into test values (02,'Shanky') "

conn.execute(query)
conn.commit()
print("Record Inserted..")
conn.close()