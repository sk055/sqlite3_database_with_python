import sqlite3

conn = sqlite3.connect("Demo.db")

print("Database Opened...")
conn.close()
