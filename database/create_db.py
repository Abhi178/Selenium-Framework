import sqlite3

conn = sqlite3.connect("database/test.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
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
