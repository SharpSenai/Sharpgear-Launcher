import sqlite3
import os

path_db = os.path.join("C:", "Dados","sh")

connection = sqlite3.connect("sharpgear-ui\database\sharp_database.db")
print(connection.total_changes)
cursor = connection.cursor()

class currentUser:
    def __init__(self, id):
        self._userInfo = None
        self._tempId = id
        self.updInfo()
        
    def getInfo(self): return self._userInfo or {}
    def updInfo(self):
        conn = sqlite3.connect("sharpgear-ui/database/sharp_database.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        try:
            cursor.execute(""" 
                           SELECT *
                           FROM users
                           WHERE ID = ?
                           """,(self._tempId,))
            result = cursor.fetchone()
            
            if result:
                self._userInfo = dict(result)
                print(self._userInfo)
            else:
                print(f"Informação de usuário não encontrada: {id}")
        except sqlite3.Error as e: 
            print("Erro ao conectar ao banco de dados: ", e)
        finally: 
            conn.close()
        
def add_jogos(_nome,_dev,_desc,_url):
    connection = sqlite3.connect("sharpgear-ui\database\sharp_database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO games (name,developer,desc, gameURL) VALUES (?, ?, ?, ?)", (_nome, _dev, _desc, _url))
    connection.commit()
    print("jogo adicionado")
    connection.close()

def add_jogo_biblioteca(_user, _game):
    conn = sqlite3.connect("sharpgear-ui\database\sharp_database.db")
    cursor = conn.cursor()
    
    # Recuperar IDs do usuário e do jogo
    cursor.execute("SELECT id FROM users WHERE user = ?", (_user,))
    user_id = cursor.fetchone()
    cursor.execute("SELECT id FROM games WHERE name = ?", (_game,))
    game_id = cursor.fetchone()
    
    if user_id and game_id:
        user_id, game_id = user_id[0], game_id[0]
        cursor.execute("INSERT INTO bibliotecas (user_id, game_id) VALUES (?, ?)", (user_id, game_id))
        conn.commit()
        print(f"Jogo '{_game}' foi adicionado à biblioteca de '{_user}'.")
    else:
        print("Erro: Usuário ou jogo não encontrado.")
    
    conn.close()

def list_all_games():
    conn = sqlite3.connect("sharpgear-ui\database\sharp_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM games")
    games = cursor.fetchall()
    for game in games:
        print(f"Nome: {game[0]}")
    conn.close()

def list_user_library(username):
    conn = sqlite3.connect("sharpgear-ui\database\sharp_database.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT g.name
        FROM bibliotecas ul
        JOIN users u ON ul.user_id = u.id
        JOIN games g ON ul.game_id = g.id
        WHERE u.user = ?
    """, (username,))
    
    games = cursor.fetchall()
    if games:
        print(f"Biblioteca de '{username}':")
        for game in games:
            print(f"Nome: {game[0]}")
    else:
        print(f"'{username}' não tem jogos na biblioteca.")
    
    conn.close()

##Criar Tabela Usuários
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users ( 
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL, 
               user TEXT UNIQUE  NOT NULL, 
               email TEXT UNIQUE NOT NULL, 
               senha TEXT  NOT NULL, 
               nasc TEXT  NOT NULL
)
''')

##Criar Tabela Jogos
cursor.execute('''
               CREATE TABLE IF NOT EXISTS games(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               developer TEXT,
               desc TEXT,
               gameURL TEXT
               )
''')

#Criar Tabela Bibliotecas
cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS bibliotecas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INT NOT NULL,
                game_id INT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (game_id) REFERENCES games (id)
                )
''')

list_user_library("admin")
connection.commit()
connection.close()