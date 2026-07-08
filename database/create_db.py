import sqlite3
import os

DB_PATH = "database/test.db"

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL
)
""")

cursor.execute("""
INSERT INTO products
(product_name, price)
VALUES
('Sauce Labs Backpack', 29.99)
""")

conn.commit()
conn.close()

print("Database created successfully")
