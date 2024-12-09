import customtkinter as ctk
import sqlite3
from PIL import Image
from home import TabView

def abrir_janela_principal():
    print("Janela Principal ~~")
    janela_principal = ctk.CTkToplevel()
    janela_principal.title('Sharpgear Launcher - Principal')
    janela_principal.geometry('1280x720')
    janela_principal.resizable(False, False)

    janela_principal.focus_force()
    janela_principal.attributes("-topmost", True)
    janela_principal.attributes("-topmost", False)  # Remove o comportamento "sempre no topo" após abrir

    laura = TabView(janela_principal)
    laura.pack(side = 'left',fill = 'y')

    # Foto do Perfil
    janela_principal.imagem_grande = ctk.CTkImage(dark_image=Image.open("sharpgear-ui\images\sg_pfp_ph.png"), size=(30, 30))
    janela_principal.imagem_label_grande = ctk.CTkLabel(janela_principal, image=janela_principal.imagem_grande, text="", cursor="hand2")
    janela_principal.imagem_label_grande.bind("<Button-1>", command=lambda _: laura.set("ㅤPerfilㅤ"))
    janela_principal.imagem_label_grande.place(x=1120, y=13)
    
    # Logo Sharpgear Grande
    janela_principal.imagem_label_grande = ctk.CTkLabel(janela_principal,font=("Poppins", 28,"bold"), text="SHARPGEAR.LAUNCHER")
    janela_principal.imagem_label_grande.place(x=760, y=5)

    janela_principal.mainloop()

def verificar_usuario(master):
    connection = sqlite3.connect('sharpgear-ui\\database\\sharp_database.db')
    cursor = connection.cursor()

    nomeEmail = master.ent_email.get()
    senha = master.ent_senha.get()
    print(nomeEmail, senha)

    try:
        cursor.execute('SELECT id, user FROM users WHERE (user = ? OR email = ?) AND senha = ?',(nomeEmail,nomeEmail,senha))
        resultado = cursor.fetchone()

        if resultado:
            print(resultado[0], resultado[1])
            import global_vars  # Certifique-se de usar o módulo completo
            from database import currentUser
            global_vars.usuarioAtual = currentUser(resultado[0]).getInfo()     
            global_vars.usuarioAtual = currentUser(resultado[0]).getInfo()     
            print(f"User logado: {global_vars.usuarioAtual}")

            #tecnica proibida vv
            master.master.master.master.destroy()
            abrir_janela_principal()  # Chama função para abrir janela principal
        else:
            print("Login de usuário errado!!")

    except sqlite3.Error as E:
        print(f"Deu erro! {E}")
    finally:
        connection.close()


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

        master.destroy()
        print("-add_user")

        master.master.master.master.tabview.set("Login")
        #abrir_janela_principal(user)  # Chama a função para abrir a janela principal
    except sqlite3.IntegrityError:
        print("Erro ao inserir usuário no banco de dados.")
    finally:
        connection.close()

class RegisterFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        def login_goto():
            #soluções q até eu Deus duvida q cheguei vv
            self.master.master.master.tabview.set("Login")

        # Labels
        self.label = ctk.CTkLabel(self, text='SEJA BEM VINDO!', font=('Poppins', 25, 'bold'))
        self.label.grid(row=0, column=0, padx=20, pady=20, sticky='w')
        self.label = ctk.CTkLabel(self, text='Crie sua conta na Sharpgear Launcher', font=('Poppins', 15, 'bold'))
        self.label.grid(row=1, column=0, padx=20, sticky='w')
        self.label = ctk.CTkLabel(self, text='Ou Entre em sua Conta', font=('Poppins', 12, 'bold', 'underline'), cursor="hand2",)
        self.label.bind("<Button-1>", command=lambda _: login_goto())

        self.label.grid(row=2, column=0, padx=20, sticky='w')
        self.label = ctk.CTkLabel(self, text='Ao Cadastrar na Sharpgear Launcher você concorda\ncom os nossos termos de uso.', font=('Poppins', 12, 'bold'))
        self.label.grid(row=8, column=0, padx=20, sticky='w')

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

class LoginFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,)

        def register_goto():
            #soluções q até eu Deus duvida q cheguei vv
            self.master.master.master.tabview.set("Register")
            
        #region ~~~~Labels~~~~
        #"Seja Bem-Vindo"
        self.label = ctk.CTkLabel(self,text='SEJA BEM VINDO!',font=('Poppins',25,'bold'))
        self.label.grid(row=0, column=0, padx=20,pady=20,sticky = 'w')
        #"Crie sua conta[...]"
        self.label = ctk.CTkLabel(self,text='Entre em sua conta da Sharpgear Launcher',font=('Poppins',15,'bold'))
        self.label.grid(row=1, column=0, padx=20,sticky = 'w')
        #"Ou Entre[...]"
        self.label = ctk.CTkLabel(self,text='Ou')
        self.label.grid(row=2, column=0, padx=20,sticky = 'w')

        self.label = ctk.CTkLabel(self, text='Registre em sua conta Sharpgear', cursor="hand2", font=("Poppins", 12, "bold", 'underline'))
        self.label.grid(row=2, column=0, padx=40, sticky='w')
        self.label.bind("<Button-1>", command=lambda _: register_goto())
        #"Ao Cadastrar[...]"
        self.label = ctk.CTkLabel(self,text='Esqueceu sua senha? Redefina sua Senha',font=("Poppins", 12, "bold", 'underline'))
        self.label.grid(row=8, column=0, padx=20,sticky = 'w')
        #endregion
        #region ~~~~Entradas~~~~
        #Email
        self.ent_email = ctk.CTkEntry(self,placeholder_text='Usuário ou Email',font=("Poppins", 13, "bold"))
        self.ent_email.grid(row= 5,column = 0,padx = 20, pady = 10, sticky = 'ew')
        #Senha
        self.ent_senha = ctk.CTkEntry(self,placeholder_text='Senha',show = '*',font=("Poppins", 13, "bold"))
        self.ent_senha.grid(row= 6,column = 0,padx = 20, pady = 10, sticky = 'ew')
        #endregion
        
        # Botão para Entrar
        self.btn_cadastrar = ctk.CTkButton(self, text='Entrar',command = lambda: verificar_usuario(self),font=("Poppins", 13, "bold"))
        self.btn_cadastrar.grid(row= 9,column = 0,padx = 20, pady = 10, sticky = 'ew',)
