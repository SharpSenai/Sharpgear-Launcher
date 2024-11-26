# Libraries
import sqlite3
import validation

# Class
class DataBase():
    def __init__(self):
        self.createDb()
   
    def __createConnection(self):
        self.connection = sqlite3.connect("database.db")

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
                            CREATE TABLE userDataBase (
                                userId    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                persona   TEXT NOT NULL,
                                username  TEXT NOT NULL UNIQUE,
                                email     TEXT NOT NULL UNIQUE,
                                password  TEXT NOT NULL,
                                birthDate TEXT NOT NULL,
                            )
                            """)
        
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

        
        