import customtkinter as ctk
import sqlite3

connection = sqlite3.connect("sharp.db")
print(connection.total_changes)

cursor = connection.cursor()
'''
cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
'''
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        #Labels
        self.label = ctk.CTkLabel(self,text='SEJA BEM VINDO!',font=('Codec Cold Trial',25,'bold'))
        self.label.grid(row=0, column=0, padx=20,pady=20,sticky = 'w')

        self.label = ctk.CTkLabel(self,text='Faça login na sua conta Sharpgear Launcher',font=('Codec Pro',15,'bold'))
        self.label.grid(row=1, column=0, padx=20,sticky = 'w')

        self.label = ctk.CTkLabel(self,text='Não possui uma conta? Cadastrar')
        self.label.grid(row=2, column=0, padx=20,sticky = 'w')

        self.label = ctk.CTkLabel(self,text='Esqueceu a senha? Redefina sua Senha')
        self.label.grid(row=5, column=0, padx=20,sticky = 'w')

        #Entradas
        self.ent_user = ctk.CTkEntry(self,placeholder_text='Usuário ou Email')
        self.ent_user.grid(row= 3,column = 0,padx = 20, sticky = 'w')

        self.ent_senha = ctk.CTkEntry(self,placeholder_text='Senha')
        self.ent_senha.grid(row= 4,column = 0,padx = 20, pady = 10, sticky = 'w')

        #Botões
        self.btt_login = ctk.CTkButton(self,text='ENTRAR')
        self.btt_login.grid(row = 6, column = 0,padx = 20, sticky='w')
