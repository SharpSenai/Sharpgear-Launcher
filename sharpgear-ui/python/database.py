import customtkinter as ctk
import sqlite3
import os
from datetime import datetime


class bancodepica():
    def configurar_banco():
        db_path = os.path.join("C:\\Users\\lucas_h_francisco\Documents\\GitHub\\Sharpgear-Launcher\\sharpgear-ui\\database")
        os.makedirs(db_path, exist_ok=True)  # Garante que o diretório exista

        db_file = os.path.join(db_path, "sharp_database.db")
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Criação da tabela 'users', se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL, 
                user TEXT UNIQUE NOT NULL, 
                email TEXT UNIQUE NOT NULL, 
                senha TEXT NOT NULL, 
                nasc TEXT NOT NULL
            )
        ''')
        connection.commit()
        connection.close()
        return db_file