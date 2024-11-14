import customtkinter as ctk
<<<<<<< Updated upstream

class LoginFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,)
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
        self.btn_cadastrar = ctk.CTkButton(self, text='Entrar')
        self.btn_cadastrar.grid(row= 9,column = 0,padx = 20, pady = 10, sticky = 'w')
=======
from register import abrir_janela_principal

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # ~~~~ Labels ~~~~
        # "Seja Bem-Vindo"
        self.label_bem_vindo = ctk.CTkLabel(self, text='SEJA BEM VINDO!', font=('Codec Cold Trial', 25, 'bold'))
        self.label_bem_vindo.grid(row=0, column=0, padx=20, pady=20, sticky='w')
        
        # "Entre em sua conta[...]"
        self.label_entrada = ctk.CTkLabel(self, text='Entre em sua conta da Sharpgear Launcher', font=('Codec Pro', 15, 'bold'))
        self.label_entrada.grid(row=1, column=0, padx=20, sticky='w')
        
        # "Ou Entre[...]"
        self.label_ou = ctk.CTkLabel(self, text='Ou')
        self.label_ou.grid(row=2, column=0, padx=20, sticky='w')
        
        # "Registre em sua conta Sharpgear"
        self.label_registro = ctk.CTkLabel(self, text='Registre em sua conta Sharpgear', cursor="hand2", font=("Arial", 12, "bold", 'underline'))
        self.label_registro.grid(row=2, column=0, padx=40, sticky='w')
        self.label_registro.bind("<Button-1>", lambda event: master.abrir_registro())
        
        # "Esqueceu sua senha? Redefina sua Senha"
        self.label_esqueci_senha = ctk.CTkLabel(self, text='Esqueceu sua senha? Redefina sua Senha')
        self.label_esqueci_senha.grid(row=8, column=0, padx=20, sticky='w')
        
        # ~~~~ Entradas ~~~~
        # Email
        self.ent_email = ctk.CTkEntry(self, placeholder_text='Usuário ou Email')
        self.ent_email.grid(row=5, column=0, padx=30, pady=30, sticky='w')
        
        # Senha
        self.ent_senha = ctk.CTkEntry(self, placeholder_text='Senha', show='*')
        self.ent_senha.grid(row=6, column=0, padx=30, pady=30, sticky='w')
        
        # Botão para Entrar
        self.btn_entrar = ctk.CTkButton(self, text='Entrar', command=abrir_janela_principal)
        self.btn_entrar.grid(row=9, column=0, padx=20, pady=10, sticky='w')
>>>>>>> Stashed changes
