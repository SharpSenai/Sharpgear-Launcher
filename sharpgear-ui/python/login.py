import customtkinter as ctk
import sqlite3
from register import abrir_janela_principal

connection = sqlite3.connect('sharpgear-ui\database\sharp_database.db')
cursor = connection.cursor()

def fazer_login():
    print("Input Entrar")

class LoginFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,)

        def login_user():
            username = self.ent_email.get()
            senha = self.ent_senha.get()

            connection = sqlite3.connect("sharpgear-ui\database\sharp_database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM users WHERE user = ? AND senha =?", (username, senha))
            user = cursor.fetchone()

            if user:
                print(f"Logou como:{username}")
                abrir_janela_principal()
            else:
                print("Usuario ou senha inválidos")

        #region ~~~~Labels~~~~
        #"Seja Bem-Vindo"
        self.label = ctk.CTkLabel(self,text='SEJA BEM VINDO!',font=('Codec Cold Trial',25,'bold'))
        self.label.grid(row=0, column=0, padx=20,pady=20,sticky = 'w')
        #"Crie sua conta[...]"
        self.label = ctk.CTkLabel(self,text='Entre em sua conta da Sharpgear Launcher',font=('Codec Pro',15,'bold'))
        self.label.grid(row=1, column=0, padx=20,sticky = 'w')
        #"Ou Entre[...]"
        self.label = ctk.CTkLabel(self,text='Ou')
        self.label.grid(row=2, column=0, padx=20,sticky = 'w')

        self.label = ctk.CTkLabel(self, text='Entre em sua conta Sharpgear', cursor="hand2", font=("Arial", 12, "bold", 'underline'))
        self.label.grid(row=2, column=0, padx=40, sticky='w')
        self.label.bind("<Button-1>", command=lambda _: master.abrir_registro())
        #"Ao Cadastrar[...]"
        self.label = ctk.CTkLabel(self,text='Esqueceu sua senha? Redefina sua Senha')
        self.label.grid(row=8, column=0, padx=20,sticky = 'w')
        #endregion
        #region ~~~~Entradas~~~~
        #Email
        self.ent_email = ctk.CTkEntry(self,placeholder_text='Usuário ou Email')
        self.ent_email.grid(row= 5,column = 0,padx = 20, pady = 10, sticky = 'w')
        #Senha
        self.ent_senha = ctk.CTkEntry(self,placeholder_text='Senha')
        self.ent_senha.grid(row= 6,column = 0,padx = 20, pady = 10, sticky = 'w')
        #endregion
        
        # Botão para Entrar
        self.btn_cadastrar = ctk.CTkButton(self, text='Entrar' ,command = login_user)
        self.btn_cadastrar.grid(row= 9,column = 0,padx = 20, pady = 10, sticky = 'w')

