import sqlite3
import os

path_db = os.path.join("C:", "Dados","sh")

connection = sqlite3.connect("sharpgear-ui\database\sharp_database.db")
print(connection.total_changes)

cursor = connection.cursor()
cursor.execute('''
               CREATE TABLE users ( 
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT, 
               user TEXT UNIQUE, 
               email TEXT UNIQUE, 
               senha TEXT, 
               nasc TEXT
)
''')
