import sqlite3

conn = sqlite3.connect("Demo.db")

query = "delete from test where id = 2"

conn.execute(query)
conn.commit()

print("Deleted successfully...")
conn.close()