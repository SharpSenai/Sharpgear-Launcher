import customtkinter as ctk

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #Labels
        self.label = ctk.CTkLabel(self,text='SEJA BEM VINDO!',font=('Codec Cold Trial',50,'bold'))
        self.label.grid(row=0, column=0, padx=20,sticky = 'w')

        self.label = ctk.CTkLabel(self,text='Faça login na sua conta\nSharpgear Launcher',font=('Codec Pro',20,'bold'))
        self.label.grid(row=1, column=0, padx=20,sticky = 'w')

        self.label = ctk.CTkLabel(self,text='Não possui uma conta? Cadastrar')
        self.label.grid(row=2, column=0, padx=20,sticky = 'w')

        self.label = ctk.CTkLabel(self,text='Esqueceu a senha? Redefina sua Senha')
        self.label.grid(row=5, column=0, padx=20,sticky = 'w')

        #Entradas
        self.ent_user = ctk.CTkEntry(self,placeholder_text='Usuário ou Email')
        self.ent_user.grid(row= 3,column = 0,padx = 20, sticky = 'w')

        self.ent_senha = ctk.CTkEntry(self,placeholder_text='Usuário ou Email')
        self.ent_senha.grid(row= 4,column = 0,padx = 20, pady = 10, sticky = 'w')

        #Botões
        self.btt_login = ctk.CTkButton(self,text='ENTRAR')
        self.btt_login.grid(row = 6, column = 0,padx = 20, sticky='w')




class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Sharpgear Launcher')
        self.geometry('960x540')


        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=0, pady=0, sticky="w")



app = App()
app.mainloop()