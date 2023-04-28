import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE feedback (eventype TEXT, ratings INTEGER)')
print("Created table successfully!")

conn.close()