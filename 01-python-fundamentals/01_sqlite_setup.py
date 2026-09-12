import sqlite3

connection = sqlite3.connect("customers.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    balance REAL
)
""")

connection.commit()
connection.close()

print("Database and customers table created successfully.")