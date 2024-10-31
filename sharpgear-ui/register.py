import customtkinter as ctk
import sqlite3
from contextlib import closing
from login import LoginFrame
'''
cursor = connection.cursor()
cursor.execute("CREATE TABLE users (nome TEXT, user TEXT, email TEXT, senha TEXT, nasc TEXT)")
'''
def add_usuario():
    connection = sqlite3.connect('sharp_database.db')
    cursor = connection.cursor()
    
    nome = app.my_frame.ent_nome.get()   # type: ignore
    user = app.my_frame.ent_user.get()   # type: ignore
    email = app.my_frame.ent_email.get() # type: ignore
    senha = app.my_frame.ent_senha.get() # type: ignore
    nasc = app.my_frame.ent_nasc.get()   # type: ignore

    RegisterWindow.destroy()
    try: 
        cursor.execute('INSERT INTO users (nome, user, email, senha, nasc) VALUES (?,?,?,?,?)', (nome,user,email,senha,nasc))
        connection.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        connection.close()

def taquipariu():
    print('vogoza')

class RegisterFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #region ~~~~Labels~~~~
        #"Seja Bem-Vindo"
        self.label = ctk.CTkLabel(self,text='SEJA BEM VINDO!',font=('Codec Cold Trial',25,'bold'))
        self.label.grid(row=0, column=0, padx=20,pady=20,sticky = 'w')
        #"Crie sua conta[...]"
        self.label = ctk.CTkLabel(self,text='Crie sua conta na Sharpgear Launcher',font=('Codec Pro',15,'bold'))
        self.label.grid(row=1, column=0, padx=20,sticky = 'w')
        #"Ou Entre[...]"
        self.label = ctk.CTkLabel(self, text='Ou ')
        self.label.grid(row=2, column=0, padx=20,sticky = 'w')

        self.label = ctk.CTkLabel(self, text='Entre' , cursor="hand2",font=("Arial", 12, "bold" , 'underline'))
        self.label.grid(row=2, column=0, padx=40,sticky = 'w')
        self.label.bind("<Button-1>", lambda e: taquipariu())
        #endregion

        #region ~~~~Entradas~~~~
        #Nome Completo
        self.ent_nome = ctk.CTkEntry(self,placeholder_text='Nome Completo')
        self.ent_nome.grid(row= 3,column = 0,padx = 20, pady = 10, sticky = 'w')
        #Usuário
        self.ent_user = ctk.CTkEntry(self,placeholder_text='Usuário')
        self.ent_user.grid(row= 4,column = 0,padx = 20, pady = 10, sticky = 'w')
        #Email
        self.ent_email = ctk.CTkEntry(self,placeholder_text='Email')
        self.ent_email.grid(row= 5,column = 0,padx = 20, pady = 10, sticky = 'w')
        #Senha
        self.ent_senha = ctk.CTkEntry(self,placeholder_text='Senha')
        self.ent_senha.grid(row= 6,column = 0,padx = 20, pady = 10, sticky = 'w')
        #Data de Nascimento
        self.ent_nasc = ctk.CTkEntry(self,placeholder_text='Data de Nascimento')
        self.ent_nasc.grid(row= 7,column = 0,padx = 20, pady = 10, sticky = 'w')
        #endregion
    
        #region ~~~~Botões~~~~
        #Cadastrar
        self.btt_login = ctk.CTkButton(self,text='CADASTRAR',command=add_usuario)
        self.btt_login.grid(row = 9, column = 0,padx = 20, sticky='w')
        #endregion

class RegisterWindow(ctk.CTkToplevel):
    def __init__(self,master):
        super().__init__(master)
        self.title('Sharpgear Launcher')
        self.geometry('960x540')

        self.register_frame = RegisterFrame(self)
        self.register_frame.grid(row=0, column=0, padx=0, pady=0, sticky="w")

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Sharpgear Launcher')
        self.geometry('960x540')

        self.my_frame = RegisterFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=0, pady=0, sticky="w")
        

app = App()
app.mainloop()