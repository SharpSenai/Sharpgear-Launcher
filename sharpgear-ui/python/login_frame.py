import customtkinter as ctk
from register import verificar_usuario

class LoginFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,)
        
        def fazer_login(_self):
            verificar_usuario(_self)
            
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
        self.label.bind("<Button-1>", command=lambda _: master.abrir_registro())
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
        self.btn_cadastrar = ctk.CTkButton(self, text='Entrar',command = lambda: fazer_login(self),font=("Poppins", 13, "bold"))
        self.btn_cadastrar.grid(row= 9,column = 0,padx = 20, pady = 10, sticky = 'ew',)
