import sqlite3

try:
    sqlite3.connect(':memory:')
    print("SQLite is working.")
except Exception as e:
    print("Error:", e)
