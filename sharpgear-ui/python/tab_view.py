import customtkinter as ctk
from PIL import Image
import sqlite3
imagem_snl = ctk.CTkImage(dark_image=Image.open("sharpgear-ui\images\snl_image_placeholder.png"), size=(700, 700))

class TabView(ctk.CTkTabview):
    def __init__(self,master,_user_id):
        super().__init__(master)

        tab_biblioteca = self.add("Biblioteca")
        tab_loja = self.add("Loja")
        tab_perfil = self.add("Perfil")

        frame_biblioteca = FrameBiblioteca(tab_biblioteca,_user_id)
        frame_biblioteca.pack(side = 'left', fill = 'y')

        frame_perfil = FramePerfil(tab_perfil,_user_id)
        frame_perfil.pack()

class FrameBiblioteca(ctk.CTkFrame):
    def __init__(self, master,_user_id):
        super().__init__(master)
        self.user_id = _user_id
        self.carrinho = []

        def atualizar_combobox(_resultados):
            jogos = [row[0] for row in _resultados]
            self.combobox.configure(values=jogos)

        def procurar_jogos(event=None):
            consulta = self.combobox.get()
            conn = sqlite3.connect('sharpgear-ui\\database\\sharp_database.db')
            cursor = conn.cursor()

            cursor.execute('''
                           SELECT games.name 
                           FROM bibliotecas
                           INNER JOIN games ON bibliotecas.game_Id = games.id
                           WHERE bibliotecas.user_id = ? AND games.name LIKE ?
                           
                           ''', (self.user_id, consulta + '%'))
            resultados = cursor.fetchall()

            atualizar_combobox(resultados)
            conn.close()
        self.combobox = ctk.CTkComboBox(master=self,values=[],width=220)
        self.combobox.set("🔍")    
        self.combobox.grid(row = 0, column = 0,padx = 15, pady = 10)

        self.combobox.bind("<KeyRelease>",procurar_jogos)

        self.label = ctk.CTkLabel(self,text="TEST")
        self.label.grid(row = 0, column = 1)

class FramePerfil(ctk.CTkFrame):
    def __init__(self, master,_user):
        super().__init__(master)

        self.label = ctk.CTkLabel(self,text=_user)
        self.label.grid(row = 0, column = 0)

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
