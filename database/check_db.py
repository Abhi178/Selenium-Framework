# database/check_db.py

import sqlite3

conn = sqlite3.connect("database/test.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM products")

print(cursor.fetchall())

conn.close()