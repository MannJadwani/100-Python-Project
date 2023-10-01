import sqlite3
conn = sqlite3.connect("expense.db")
cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS expenses
            (id INTEGER PRIMARY KEY,
            Date DATE
            description TEXT
            category TEXT
            price REAL)""")

conn.commit()
conn.close()