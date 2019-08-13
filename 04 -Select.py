import sqlite3

conn = sqlite3.connect("Demo.db")

print("Database Opened...")

# query =
cursor =  conn.execute("select * from test")

# print(cursor)
for row in cursor:
    print("\nID  = {}".format( row[0]))
    print("Name  = "+ row[1])
    print("Address  = {}".format( row[2]))

print("\nOperation done successfully")
conn.close()