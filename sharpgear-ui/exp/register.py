import customtkinter as ctk
import sqlite3

# Conectar ao banco de dados
def add_usuario(ent_nome, ent_user, ent_email, ent_senha, ent_nasc):
    connection = sqlite3.connect("sharp_database.db")
    cursor = connection.cursor()
    
    nome = ent_nome.get()
    user = ent_user.get()
    email = ent_email.get()
    senha = ent_senha.get()
    nasc = ent_nasc.get()

    try:
        cursor.execute(
            "INSERT INTO users (nome, user, email, senha, nasc) VALUES (?, ?, ?, ?, ?)",
            (nome, user, email, senha, nasc),
        )
        connection.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        connection.close()

# Função para abrir a janela de registro e aceitar a função de abrir a janela principal como argumento
def abrir_janela_registro(funcao_abrir_principal):
    janela_registro = RegisterWindow(funcao_abrir_principal)
    janela_registro.mainloop()

# Classe da Janela de Registro
class RegisterWindow(ctk.CTkFrame):
    def __init__(self, funcao_abrir_principal):
        super().__init__()
        self.title("Sharpgear Launcher")
        self.geometry("960x540")
        self.funcao_abrir_principal = funcao_abrir_principal

        #region ~~~~Labels~~~~
        #"Seja Bem-Vindo"
        self.label = ctk.CTkLabel(self,text='SEJA BEM VINDO!',font=('Codec Cold Trial',25,'bold'))
        self.label.grid(row=0, column=0, padx=20,pady=20,sticky = 'w')
        #"Crie sua conta[...]"
        self.label = ctk.CTkLabel(self,text='Crie sua conta na Sharpgear Launcher',font=('Codec Pro',15,'bold'))
        self.label.grid(row=1, column=0, padx=20,sticky = 'w')
        #"Ou ..."
        self.label = ctk.CTkLabel(self, text='Ou ')
        self.label.grid(row=2, column=0, padx=20,sticky = 'w')
        #"{Entre}"
        self.label = ctk.CTkLabel(self, text='Entre em sua conta' , cursor="hand2",font=("Arial", 12, "bold" , 'underline'))
        self.label.grid(row=2, column=0, padx=40,sticky = 'w')
        #self.label.bind("<Button-1>", lambda e: taquipariu())

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
    
        # Botão de Registrar
        self.botao_registrar = ctk.CTkButton(
            self, text="Cadastrar", command=self.registrar_e_fechar
        )
        self.botao_registrar.grid(row=9, column=0, padx=20, pady=10,sticky='w')

    def registrar_e_fechar(self):
        add_usuario(self.ent_nome, self.ent_user, self.ent_email, self.ent_senha, self.ent_nasc)  # Adiciona o usuário ao banco de dados
        self.destroy()  # Fecha a janela de registro
        self.funcao_abrir_principal()  # Abre a janela principal passada como argumento
