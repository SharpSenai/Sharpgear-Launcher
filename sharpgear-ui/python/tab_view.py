import customtkinter as ctk
from PIL import Image
import sqlite3

class TabView(ctk.CTkTabview):
    def __init__(self, master, _user_id):
        super().__init__(master)

        self.configure(anchor = "w",fg_color = "transparent")

        # Criação das abas
        tab_biblioteca = self.add("ㅤBibliotecaㅤ")
        tab_loja = self.add("ㅤLojaㅤ")
        tab_perfil = self.add("ㅤPerfilㅤ")

        for tab_button in self._segmented_button._buttons_dict.values():
            tab_button.grid_configure(padx=20)
            tab_button.configure(font=("Poppins", 16, "bold"))  # Alterando a fonte


        # Inicialização dos frames dentro de cada aba
        frame_biblioteca = FrameBiblioteca(tab_biblioteca, _user_id)
        frame_biblioteca.pack(side='left', fill='y')

        frame_perfil = FramePerfil(tab_perfil, _user_id)
        frame_perfil.pack()


class FrameBiblioteca(ctk.CTkFrame):
    def __init__(self, master, _user_id):
        super().__init__(master)
        self.user_id = _user_id

        def atualizar_combobox(_resultados):
            jogos = [row[0] for row in _resultados]
            self.combobox.configure(values=jogos)

        def procurar_jogos(event=None):
            consulta = self.combobox.get()  # Texto digitado na combobox
            conn = sqlite3.connect("sharpgear-ui/database/sharp_database.db")
            cursor = conn.cursor()

            try:
                # Query para buscar jogos da biblioteca do usuário
                cursor.execute("""
                    SELECT g.name
                    FROM bibliotecas b
                    INNER JOIN games g ON b.game_id = g.id
                    WHERE b.user_id = ? AND g.name LIKE ?
                """, (self.user_id, consulta + '%'))
                resultados = cursor.fetchall()
                print('wa')
                atualizar_combobox(resultados)  # Atualiza a combobox com os resultados
            except sqlite3.Error as e:
                print("Erro ao buscar jogos na biblioteca:", e)
            finally:
                conn.close()


        # Combobox para busca de jogos
        self.combobox = ctk.CTkComboBox(master=self, values=[], width=220,state="normal",font=('Poppins', 13,'bold'))
        self.combobox.grid(row=0, column=0, padx=15, pady=10,sticky = "n")

        self.combobox.set("")
        self.combobox.bind("<KeyRelease>",procurar_jogos)

        #Imagem do jogo
        self.imagem_grande = ctk.CTkImage(dark_image=Image.open("sharpgear-ui\\images\\snl_image_placeholder.png"), size=(960, 750))
        self.imagem_label_grande = ctk.CTkLabel(self, image=self.imagem_grande, text="")
        self.imagem_label_grande.grid(row = 0, column = 1)

        self.botao = ctk.CTkButton(self,text="JOGAR",font=('Poppins',16,'bold'))
        self.botao.place(x= 950,y=400)

class FramePerfil(ctk.CTkFrame):
    def __init__(self, master, _user):
        super().__init__(master)

        # Exibe o nome do usuário no frame de perfil
        self.label = ctk.CTkLabel(self, text=_user)
        self.label.grid(row=0, column=0)


class UpperFrame(ctk.CTkFrame):
    def __init__(self, master, nome_user):
        super().__init__(master)

        # Exibindo o nome do usuário no canto superior direito
        self.label_nome = ctk.CTkLabel(self, text=nome_user, font=('Codec Cold Trial', 15, 'bold'))
        self.label_nome.grid(row=0, column=8, padx=500, pady=4)

        # Botões no frame superior
        self.btt_biblioteca = ctk.CTkButton(self, text="BIBLIOTECA")
        self.btt_biblioteca.grid(row=0, column=1, padx=50, pady=20)

        self.btt_loja = ctk.CTkButton(self, text="LOJA")
        self.btt_loja.grid(row=0, column=2, padx=50, pady=20)

        self.btt_perfil = ctk.CTkButton(self, text=nome_user)
        self.btt_perfil.grid(row=0, column=3, padx=50, pady=20)
