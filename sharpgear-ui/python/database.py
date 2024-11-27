# Libraries
import sqlite3
import os 

# Class
class DataBase:
    def __init__(self):
        self.createDb()
   
    def __createConnection(self):
        _directorydb = os.path.join(os.path.dirname(__file__), "../database")
        _pathdb = os.path.join(_directorydb, "database.db")
        
        os.makedirs(_directorydb, exist_ok=True)
      
        self.connection = sqlite3.connect(_pathdb)
        
    def __closeConnection(self):
        self.connection.close()
        self.cursor = None
  
    def __createCursor(self):
        self.cursor = self.connection.cursor()
        
    def __commitDatabase(self):
        self.connection.commit()
        
    def createDb(self):
        self.__createConnection()
        self.__createCursor() 
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS userDataBase (
                userId    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                persona   TEXT NOT NULL,
                username  TEXT NOT NULL UNIQUE,
                email     TEXT NOT NULL UNIQUE,
                password  TEXT NOT NULL,
                birthDate DATE NOT NULL
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ownedGames (
                libId     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                userId    INTEGER NOT NULL,
                gameName  TEXT NOT NULL,
                purchaseDate TEXT NOT NULL,
                
                FOREIGN KEY (userId) REFERENCES userDataBase (userId) ON DELETE CASCADE
            );
        """)
        
        self.connection.commit()
        
        self.__closeConnection()


    def queryInformation(self, query, optInfo):
        self.__createConnection()
        self.__createCursor()
        
        match query:
            case "checkLogin":
                self.cursor.execute("""
                                    SELECT * FROM userDataBase WHERE
                                    (username = ? or email = ?) AND password = ?
                                    """, optInfo)
                result = self.cursor.fetchone()
                self.__closeConnection()

                if result:
                    return True
                else:
                    return False      
                
            case "registerAccount":
                try:
                    
                    self.cursor.execute("""
                        INSERT INTO userDataBase 
                        (persona, username, email, password, birthDate) 
                        VALUES (?, ?, ?, ?, ?)
                    """, optInfo)
                    
                    self.__commitDatabase()
                    self.__closeConnection()
                    return True
                
                except sqlite3.IntegrityError as e:
                    self.__closeConnection()
                    if "UNIQUE constraint" in str(e):
                        return False
                    return False
            
            case "returnInfo":
                    try:
                        if len(optInfo) == 1:
                            query = "SELECT * FROM userDataBase WHERE userId = ?"
                            
                        elif len(optInfo) == 2:
                            field = optInfo[0]
                            if field not in ["username", "email"]:
                                raise ValueError("Invalid search info.")
                            
                            query = f"SELECT * FROM userDataBase WHERE {field} = ?"
                            optInfo = (optInfo[1],)  
                            
                        else:
                            raise ValueError("Invalid optinfo format.")
                        
                        self.cursor.execute(query, optInfo)
                        result = self.cursor.fetchall()  
                        self.__closeConnection()

                        return result if result else None 

                    except Exception as e:
                        self.__closeConnection()
                        print(f"Error finding information: {e}")
                        return None
