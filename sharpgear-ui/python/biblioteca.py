import customtkinter as ctk

class BibliotecaFrame(ctk.CTkFrame):
    def __init__(self,master,nome_user):
        super().__init__(master)

        self.luquinhasdeladinho = BibliotecaLeftBar(self)
        self.luquinhasdeladinho.pack(side = "left", fill = "y")

class BibliotecaLeftBar(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.entry = ctk.CTkEntry(self,placeholder_text="🔍")
        self.entry.pack(padx = 20,fill = 'x')