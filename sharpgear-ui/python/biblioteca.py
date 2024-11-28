
import customtkinter as ctk
import sqlite3
import os
from datetime import datetime
from database import bancodepica

# Função para configurar o banco de dados

# Classe principal do frame
bancodepica.configurar_banco()

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)

        # Frame superior
        self.upper_frame = UpperFrame(self, user)
        self.upper_frame.pack()

        # Frame lateral
        self.left_frame = LeftFrame(self)
        self.left_frame.pack(side="left", fill="y")


class UpperFrame(ctk.CTkFrame):
    def __init__(self, master, user):
        super().__init__(master)

        # Exibindo o nome do usuário no canto superior direito
        self.label_nome = ctk.CTkLabel(self, text=user, font=('Codec Cold Trial', 15, 'bold'))
        self.label_nome.grid(row=0, column=8, padx=500, pady=4)

        self.btt_biblioteca = ctk.CTkButton(self, text="BIBLIOTECA")
        self.btt_biblioteca.grid(row=0, column=1, padx=50, pady=20)

        self.btt_loja = ctk.CTkButton(self, text="LOJA")
        self.btt_loja.grid(row=0, column=2, padx=50, pady=20)

        # Botão de perfil com evento para abrir nova janela
        self.btt_perfil = ctk.CTkButton(self, text="Perfil", command=lambda: self.abrir_perfil(user))
        self.btt_perfil.grid(row=0, column=3, padx=50, pady=20)

    def abrir_perfil(self, nome_user):
        # Nova janela de perfil
        perfil_window = ctk.CTkToplevel(self)
        perfil_window.title("Perfil do Usuário")
        perfil_window.geometry("400x300")

        # Banco de dados - Carregar informações do perfil
        database = bancodepica.configurar_banco()
        try:
            connection = sqlite3.connect(database)
            cursor = connection.cursor()

            # Consulta
            cursor.execute(
                "SELECT nome, user, email, senha, nasc FROM users WHERE user = ?",
                (nome_user,)
            )
            dados = cursor.fetchone()
            connection.close()
        except Exception as e:
            dados = None
            print("Erro ao acessar o banco de dados:", e)

        # Exibir informações do perfil
        if dados:
            nome, user, email, senha, nasc = dados

            ctk.CTkLabel(perfil_window, text=f"Nome: {nome}", font=("Arial", 18)).pack(pady=10)
            ctk.CTkLabel(perfil_window, text=f"User: {user}", font=("Arial", 16)).pack(pady=10)
            ctk.CTkLabel(perfil_window, text=f"email: {email}", font=("Arial", 16)).pack(pady=10)
            ctk.CTkLabel(perfil_window, text=f"Senha: {senha}", font=("Arial", 16)).pack(pady=10)
            ctk.CTkLabel(perfil_window, text=f"nasc: {nasc}", font=("Arial", 16)).pack(pady=10)
            print(perfil_window)
        else:
            ctk.CTkLabel(perfil_window, text="Usuário não encontrado ou erro no banco de dados.", font=("Arial", 16)).pack(pady=10)

        # Botão para fechar a janela
        ctk.CTkButton(perfil_window, text="Fechar", command=perfil_window.destroy).pack(pady=20)

class LeftFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.entry = ctk.CTkEntry(self, placeholder_text="🔍")
        self.entry.pack(padx=20, fill='x')


# Janela Principal
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sharpgear Launcher - Registro")
        self.geometry("800x600")
        self.resizable(False, False)

        # Nome do usuário para exemplo
        nome_usuario = "UsuarioTeste"
        self.main_frame = MainFrame(self, nome_usuario)
        self.main_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Configuração de aparência
    ctk.set_default_color_theme("blue")  # Configuração de tema
    app = App()
    app.mainloop()