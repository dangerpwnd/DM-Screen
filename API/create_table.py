import sqlite3

connection = sqlite3.connect('player.db')

cursor = connection.cursor()

create_tab_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, descrip text)"
cursor.execute(create_tab_items)

create_tab_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_tab_users)

connection.commit()

connection.close()
