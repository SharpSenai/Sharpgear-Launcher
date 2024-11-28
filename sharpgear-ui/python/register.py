import customtkinter as ctk
import sqlite3

def add_usuario(master):
    connection = sqlite3.connect('sharpgear-ui\database\sharp_database.db')
    cursor = connection.cursor()
    
    nome = master.ent_nome.get()
    user = master.ent_user.get()
    email = master.ent_email.get()
    senha = master.ent_senha.get()
    nasc = master.ent_nasc.get()

    try: 
        cursor.execute('INSERT INTO users (nome, user, email, senha, nasc) VALUES (?, ?, ?, ?, ?)', (nome, user, email, senha, nasc))
        connection.commit()
        master.destroy()  # Fecha a janela de registro
        abrir_janela_principal()  # Chama a função para abrir a janela principal
    except sqlite3.IntegrityError:
        print("Erro ao inserir usuário no banco de dados.")
    finally:
        connection.close()

def abrir_janela_principal():
    janela_principal = ctk.CTk()
    janela_principal.title('Sharpgear Launcher - Principal')
    janela_principal.geometry('1280x720')

    label = ctk.CTkLabel(janela_principal, text='Bem-vindo ao Sharpgear Launcher!', font=('Codec Cold Trial', 25, 'bold'))
    label.pack(pady=20)

    janela_principal.mainloop()

class RegisterFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        #region ~~~~Labels~~~~
        #"Seja Bem-Vindo"
        self.label = ctk.CTkLabel(self,text='SEJA BEM VINDO!',font=('Codec Cold Trial',25,'bold'))
        self.label.grid(row=0, column=0, padx=20,pady=20,sticky = 'w')
        #"Crie sua conta[...]"
        self.label = ctk.CTkLabel(self,text='Crie sua conta na Sharpgear Launcher',font=('Codec Pro',15,'bold'))
        self.label.grid(row=1, column=0, padx=20,sticky = 'w')
        #"Ou Entre[...]"
        self.label = ctk.CTkLabel(self,text='Ou Entre em sua Conta')
        self.label.grid(row=2, column=0, padx=20,sticky = 'w')
        #"Ao Cadastrar[...]"
        self.label = ctk.CTkLabel(self,text='Ao Cadastrar na Sharpgear Launcher você concorda com os nossos termos de uso.')
        self.label.grid(row=8, column=0, padx=20,sticky = 'w')
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
        
        # Botão para registrar o usuário
        self.btn_cadastrar = ctk.CTkButton(self, text='Cadastrar', command=lambda: add_usuario(self))
        self.btn_cadastrar.grid(row= 9,column = 0,padx = 20, pady = 10, sticky = 'w')


class RegisterWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title('Sharpgear Launcher - Registro')
        self.geometry('960x540')
        self.resizable(False, False)
        
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