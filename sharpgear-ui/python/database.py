import sqlite3
import os
import json

#Conexão com o Banco de Dados
path_db = os.path.join("C:", "Dados","sh")

connection = sqlite3.connect("sharpgear-ui\\database\\sharp_database.db")
print(connection.total_changes)
cursor = connection.cursor()

def get_gameInfo(gameName: str) :
    gameInfo = {}
    
    connection = sqlite3.connect("sharpgear-ui\\database\\sharp_database.db")
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT * FROM games WHERE name = ?", (gameName,))
        result = cursor.fetchone()
        
        if result:
            columns = [col[0] for col in cursor.description]
            gameInfo = dict(zip(columns, result))
        else:
            print(f"{gameName} não encontrado.")
    except sqlite3.Error as e:
        print(f"Erro: {e}")
        
    finally: cursor.close(); connection.close()
    
    return gameInfo

def get_gameImages(gameName: str):
    gameImages = {}
        
    connection = sqlite3.connect("sharpgear-ui\\database\\sharp_database.db")
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT images FROM games WHERE name = ?", (gameName,))
        result = cursor.fetchone()
        
        if result: 
            gameImages = json.loads(result[0])
        else:
            print(f"Jogo não encontrado {gameName}")
    except sqlite3.Error as e:
        print(f"Erro: {e}")
        
    finally:
        cursor.close(); connection.close()
        
    return gameImages
            
def add_jogos(_nome, _dev, _desc, _url, _imagesurl, _isExe):
    connection = sqlite3.connect("sharpgear-ui\\database\\sharp_database.db")
    cursor = connection.cursor()
    
    try:
        # Verificar se o jogo já existe no banco de dados
        cursor.execute("SELECT id FROM games WHERE name = ?", (_nome,))
        result = cursor.fetchone()
        
        if result:
            # Atualizar as informações do jogo existente
            cursor.execute("""
                UPDATE games
                SET developer = ?, desc = ?, gameURL = ?, images = ?, isExe = ?
                WHERE name = ?
            """, (_dev, _desc, _url, _imagesurl, _isExe, _nome))
            print(f"Jogo '{_nome}' atualizado com sucesso.")
        else:
            # Inserir um novo jogo
            cursor.execute("""
                INSERT INTO games (name, developer, desc, gameURL, images, isExe)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (_nome, _dev, _desc, _url, _imagesurl, _isExe))
            print(f"Jogo '{_nome}' adicionado com sucesso.")
        
        connection.commit()
    except sqlite3.Error as e:
        print(f"Erro ao adicionar ou atualizar o jogo: {e}")
    finally:
        connection.close()


def add_jogo_biblioteca(_user, _game):
    conn = sqlite3.connect("sharpgear-ui\\database\\sharp_database.db")
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
    conn = sqlite3.connect("sharpgear-ui\\database\\sharp_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM games")
    games = cursor.fetchall()
    for game in games:
        print(f"Nome: {game[0]}")
    conn.close()

def list_user_library(username):
    conn = sqlite3.connect("sharpgear-ui\\database\\sharp_database.db")
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

class currentUser:
    def __init__(self, id):
        self._userInfo = None
        self._tempId = id
        self.updInfo()
        
    def getInfo(self): return self._userInfo or {}
    def updInfo(self):
        conn = sqlite3.connect("sharpgear-ui\\database\\sharp_database.db")
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
               gameURL TEXT,
               images TEXT,
               isExe INTEGER
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


add_jogos("Hell-O World", "Adrian Barbosa\nSharpgear Underground", 
                                        "HELL-O WORLD é um jogo PvP para 2-4 jogadores\n"
                                        "que utiliza o sistema de Rollback Beta do GMS2.\n"
                                        "Convide seus amigos (se você tiver algum) para\n"
                                        "destruí-los nesse jogo de tiro competitivo Top-Down.\n"
                                        "-Criado e desenvolvido por AdriN.",
            "https://gx.games/pt-br/games/mzuh34/hell-o-world/", 
          json.dumps(
              {
                  "Capa": "sharpgear-ui\images\hw\splash_hell0world.png",
                  "Thumb":"sharpgear-ui\images\hw\library_hell0world.png",
                  "Screenshot0":"sharpgear-ui\images\hw\hw_screenshot0.png",
                  "Screenshot1":"sharpgear-ui\images\hw\hw_screenshot1.png"
              }
          ), 0)


add_jogos("Surv N Live", "Adrian Barbosa\nSharpgear Underground",
                                        "Surv N' Live é um jogo coop top down no qual você\n"
                                        "assume o papel de três jovens de um grupo de\n"
                                        "hackers que foram “convidados” de maneira curta\n"
                                        "e gentil a participar de uma série de desafios que\n"
                                        "valem sua liberdade... ou até mesmo sua vida.",
                                        "https://gx.games/games/g14inf/surv-n-live-0-0-0-7-old-ver-/tracks/f2d8415e-9385-43f6-8776-0deec28eb368/", 
          json.dumps(
              {
                  "Capa": "sharpgear-ui\images\snl\splash_survnlive.png",
                  "Thumb":"sharpgear-ui\images\snl\library_survnlive.png",
                  "Screenshot0":"sharpgear-ui\images\snl\snl_screenshot0.png",
                  "Screenshot1":"sharpgear-ui\images\snl\snl_screenshot1.png"
              }
          ), 0)

connection.commit()
connection.close()