import sqlite3

conn = sqlite3.connect("Demo.db")

print("Database Opened...")

query = "create table test (id int, name text(40)) "

conn.execute(query)

print("Table created...")
conn.close()