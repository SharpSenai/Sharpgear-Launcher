import customtkinter as ctk
from PIL import Image

class TabView(ctk.CTkTabview):
    def __init__(self,master):
        super().__init__(master)

        tab_biblioteca = self.add("Biblioteca")
        tab_loja = self.add("Loja")
        tab_perfil = self.add("Perfil")

        left_frame = LeftFrame(tab_biblioteca)
        left_frame.pack(side = 'left', fill = 'y')

class LeftFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        
        #region ~~BIBLIOTECA
        self.entry = ctk.CTkEntry(self,placeholder_text="🔍")
        self.entry.pack(padx = 20,fill = 'x')
        
        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)

        self.combobox = ctk.CTkComboBox(master=self,values=["hell-o word", "xvideo"],
                                        command=combobox_callback, width=220)
        self.combobox.set("my games ")    
        self.combobox.pack(padx = 25, pady = 30)

    

class UpperFrame(ctk.CTkFrame):
    def __init__(self,master,nome_user):
        super().__init__(master)
        
        # Exibindo o nome do usuário no canto superior direito
        self.label_nome = ctk.CTkLabel(self, text=nome_user, font=('Codec Cold Trial', 15, 'bold'))
        self.label_nome.grid(row=0, column=8, padx=500, pady=4)

        self.btt_biblioteca = ctk.CTkButton(self, text="BIBLIOTECA")
        self.btt_biblioteca.grid(row=0, column=1, padx=50, pady=20)

        self.btt_loja = ctk.CTkButton(self, text="LOJA")
        self.btt_loja.grid(row=0, column=2, padx=50, pady=20)

        self.btt_perfil = ctk.CTkButton(self, text=nome_user)
        self.btt_perfil.grid(row=0, column=3, padx=50, pady=20)
