import sqlite3

conn = sqlite3.connect("Demo.db")

print("Database Opened...")

query = "update test set Address = 'Sonipat' where id = 01 "

conn.execute(query)

conn.commit()
print("Successfully updated...")

conn.close()