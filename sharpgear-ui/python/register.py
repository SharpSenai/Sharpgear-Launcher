import customtkinter as ctk
import sqlite3
from tab_view import TabView
from PIL import Image

def add_usuario(master):
    connection = sqlite3.connect('sharpgear-ui\\database\\sharp_database.db')
    cursor = connection.cursor()
    
    nome = master.ent_nome.get()
    user = master.ent_user.get()
    email = master.ent_email.get()
    senha = master.ent_senha.get()
    nasc = master.ent_nasc.get()

    print(nome, user, email, senha, nasc)
    print("❤")
    try: 
        cursor.execute('INSERT INTO users (nome, user, email, senha, nasc) VALUES (?, ?, ?, ?, ?)', (nome, user, email, senha, nasc))
        connection.commit()
        master.destroy()  # Fecha a janela de registro
        print("😜")

        abrir_janela_principal(user)  # Chama a função para abrir a janela principal
    except sqlite3.IntegrityError:
        print("Erro ao inserir usuário no banco de dados.")
    finally:
        connection.close()

def verificar_usuario(master):
    connection = sqlite3.connect('sharpgear-ui\\database\\sharp_database.db')
    cursor = connection.cursor()

    nomeEmail = master.ent_email.get()
    senha = master.ent_senha.get()
    print(nomeEmail, senha)

    try:
        cursor.execute('SELECT id, user FROM users WHERE (user = ? OR email = ?) AND senha = ?',(nomeEmail,nomeEmail,senha))
        resultado = cursor.fetchone()
        print(resultado[0], resultado[1])
        
        if resultado:
            abrir_janela_principal(resultado[0])
        else:
            print("Login de usuario errado !!")

    except sqlite3.Error as E:
        print(f"Deu erro! {E}")

def abrir_janela_principal(nome_usuario):
    print("🎶")
    janela_principal = ctk.CTkToplevel()
    janela_principal.title('Sharpgear Launcher - Principal')
    janela_principal.geometry('1280x720')

    janela_principal.focus_force()
    janela_principal.attributes("-topmost", True)
    #janela_principal.attributes("-topmost", False)  # Remove o comportamento "sempre no topo" após abrir

    laura = TabView(janela_principal,nome_usuario)
    laura.pack(side = 'left',fill = 'y')
    '''
    mainframe = BibliotecaFrame(janela_principal,nome_usuario)
    mainframe.pack(side = "left",fill = 'y')
    '''
    


    janela_principal.mainloop()
    
class RegisterFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Labels
        self.label = ctk.CTkLabel(self, text='SEJA BEM VINDO!', font=('Codec Cold Trial', 25, 'bold'))
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky='w')
        self.label = ctk.CTkLabel(self, text='Crie sua conta na Sharpgear Launcher', font=('Codec Pro', 15, 'bold'))
        self.label.grid(row=1, column=0, padx=20, sticky='w')
        self.label = ctk.CTkLabel(self, text='Ou Entre em sua Conta')
        self.label.grid(row=2, column=0, padx=20, sticky='w')
        self.label = ctk.CTkLabel(self, text='Ao Cadastrar na Sharpgear Launcher você concorda com os nossos termos de uso.')
        self.label.grid(row=8, column=0, padx=20, sticky='w')

        # Entradas
        self.ent_nome = ctk.CTkEntry(self, placeholder_text='Nome Completo')
        self.ent_nome.grid(row=3, column=0, padx=20, pady=10, sticky='w')
        self.ent_user = ctk.CTkEntry(self, placeholder_text='Usuário')
        self.ent_user.grid(row=4, column=0, padx=20, pady=10, sticky='w')
        self.ent_email = ctk.CTkEntry(self, placeholder_text='Email')
        self.ent_email.grid(row=5, column=0, padx=20, pady=10, sticky='w')
        self.ent_senha = ctk.CTkEntry(self, placeholder_text='Senha', show='*')
        self.ent_senha.grid(row=6, column=0, padx=20, pady=10, sticky='w')
        self.ent_nasc = ctk.CTkEntry(self, placeholder_text='Data de Nascimento')
        self.ent_nasc.grid(row=7, column=0, padx=20, pady=10, sticky='w')
        
        # Botão para registrar o usuário
        self.btn_cadastrar = ctk.CTkButton(self, text='Cadastrar', command=lambda: add_usuario(self))
        self.btn_cadastrar.grid(row=9, column=0, padx=20, pady=10, sticky='w')

class RegisterWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title('Sharpgear Launcher - Registro')
        self.geometry('960x540')
        self.resizable(False, False)
        self.register_frame = RegisterFrame(self)
        self.register_frame.pack(side='left', fill='y')