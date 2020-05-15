import sqlite3

connection = sqlite3.connect('player.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, descrip text)"
cursor.execute(create_table)

connection.commit()

connection.close()