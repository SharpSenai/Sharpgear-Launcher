import customtkinter as ctk
import sqlite3
from tab_view import TabView  # Certifique-se de que está correto
import os


def destroy_window(window):
    """
    Função para fechar uma janela específica.
    """
    if window is not None:
        window.destroy()  # Fecha a janela especificada
        print("Janela destruída.")


def add_usuario(master):
    """
    Função para adicionar um novo usuário ao banco de dados.
    """
    connection = sqlite3.connect('sharpgear-ui\\database\\sharp_database.db')
    cursor = connection.cursor()

    nome = master.ent_nome.get()
    user = master.ent_user.get()
    email = master.ent_email.get()
    senha = master.ent_senha.get()
    nasc = master.ent_nasc.get()

    print(f"Tentando registrar: {nome}, {user}, {email}, {senha}, {nasc}")

    try:
        cursor.execute(
            'INSERT INTO users (nome, user, email, senha, nasc) VALUES (?, ?, ?, ?, ?)',
            (nome, user, email, senha, nasc)
        )
        connection.commit()

        print("Usuário registrado com sucesso!")
        destroy_window(master)  # Fecha a janela de registro

        # Reabre a janela de login importando-a dinamicamente
        from main import LoginWindow
        LoginWindow()
    except sqlite3.IntegrityError:
        print("Erro: Nome de usuário ou email já cadastrado!")
    finally:
        connection.close()


def verificar_usuario(master):
    """
    Função para verificar o login do usuário.
    """
    connection = sqlite3.connect('sharpgear-ui\\database\\sharp_database.db')
    cursor = connection.cursor()

    nomeEmail = master.ent_email.get()
    senha = master.ent_senha.get()
    print(f"Login tentando com: {nomeEmail}, senha: {senha}")

    try:
        cursor.execute(
            'SELECT id, user FROM users WHERE (user = ? OR email = ?) AND senha = ?',
            (nomeEmail, nomeEmail, senha)
        )
        resultado = cursor.fetchone()

        if resultado:
            print(f"Login bem-sucedido! ID: {resultado[0]}, Usuário: {resultado[1]}")

            abrir_janela_principal()  # Chama a janela principal
        else:
            print("Credenciais inválidas. Tente novamente.")
    except sqlite3.Error as E:
        print(f"Erro ao verificar usuário: {E}")
    finally:
        connection.close()


def abrir_janela_principal():
    """
    Abre a janela principal após o login bem-sucedido.
    """
    print("Abrindo janela principal...")
    janela_principal = ctk.CTkToplevel()
    janela_principal.title('Sharpgear Launcher - Principal')
    janela_principal.geometry('1280x720')

    laura = TabView(janela_principal)
    laura.pack(side='left', fill='y')

    janela_principal.mainloop()


class RegisterFrame(ctk.CTkFrame):
    """
    Frame para o formulário de registro.
    """
    def __init__(self, master):
        super().__init__(master)

        # Labels
        self.label = ctk.CTkLabel(self, text='SEJA BEM-VINDO!', font=('Poppins', 25, 'bold'))
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky='w')

        self.label = ctk.CTkLabel(self, text='Crie sua conta na Sharpgear Launcher', font=('Poppins', 15, 'bold'))
        self.label.grid(row=1, column=0, padx=20, sticky='w')

        # Entradas
        self.ent_nome = ctk.CTkEntry(self, placeholder_text='Nome Completo')
        self.ent_nome.grid(row=3, column=0, padx=20, pady=10, sticky='ew')
        self.ent_user = ctk.CTkEntry(self, placeholder_text='Usuário')
        self.ent_user.grid(row=4, column=0, padx=20, pady=10, sticky='ew')
        self.ent_email = ctk.CTkEntry(self, placeholder_text='Email')
        self.ent_email.grid(row=5, column=0, padx=20, pady=10, sticky='ew')
        self.ent_senha = ctk.CTkEntry(self, placeholder_text='Senha', show='*')
        self.ent_senha.grid(row=6, column=0, padx=20, pady=10, sticky='ew')
        self.ent_nasc = ctk.CTkEntry(self, placeholder_text='Data de Nascimento')
        self.ent_nasc.grid(row=7, column=0, padx=20, pady=10, sticky='ew')

        # Botão para registrar o usuário
        self.btn_cadastrar = ctk.CTkButton(self, text='Cadastrar', command=lambda: add_usuario(self))
        self.btn_cadastrar.grid(row=9, column=0, padx=20, pady=10, sticky='eew')


class RegisterWindow(ctk.CTkToplevel):
    """
    Janela de registro.
    """
    def __init__(self, master):
        super().__init__(master)
        self.title('Sharpgear Launcher - Registro')
        self.geometry('960x540')
        self.resizable(False, False)
        self.register_frame = RegisterFrame(self)
        self.register_frame.pack(side='left', fill='y')
