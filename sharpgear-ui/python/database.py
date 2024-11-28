import sqlite3
import os

path_db = os.path.join("C:", "Dados","sh")

connection = sqlite3.connect("sharpgear-ui\database\sharp_database.db")
print(connection.total_changes)
cursor = connection.cursor()

def add_jogos(_nome,_dev,_desc):
    connection = sqlite3.connect("sharpgear-ui\database\sharp_database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO games (name,developer,desc) VALUES (?, ?, ?)", (_nome, _dev, _desc))
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

##Criar Tabela Usuários
cursor.execute('''
               CREATE TABLE IF NOT EXISTS games(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               developer TEXT,
               desc TEXT
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


add_jogos("Surv N Live", "Sharpgear Underground","teste")
add_jogos("Hell-O World", "Sharpgear Underground","teste2")
add_jogos("Darkness Trigger", "Sharpgear Underground","teste3")

add_jogo_biblioteca("AdriN","Surv N Live")

connection.commit()
connection.close()