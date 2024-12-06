import customtkinter as ctk
from PIL import Image
import sqlite3
import webbrowser

class TabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master)

        self.configure(anchor = "w",fg_color = "transparent")

        # Criação das abas
        tab_biblioteca = self.add("ㅤBibliotecaㅤ")
        tab_loja = self.add("ㅤLojaㅤ")
        tab_perfil = self.add("ㅤPerfilㅤ")
        
        import global_vars
        
        for tab_button in self._segmented_button._buttons_dict.values():
            tab_button.grid_configure(padx=20)
            tab_button.configure(font=("Poppins", 16, "bold"))  # Alterando a fonte

        # Inicialização dos frames dentro de cada aba
        if global_vars.usuarioAtual is None:
            print("Erro: Nenhum usuário está logado!")
            raise ValueError("Nenhum usuário está logado!")
        else:
             frame_biblioteca = FrameBiblioteca(tab_biblioteca, global_vars.usuarioAtual["id"])
             frame_biblioteca.pack(side='left', fill='y')
        
             frame_perfil = FramePerfil(tab_perfil, global_vars.usuarioAtual["user"])
             frame_perfil.pack()

             frame_loja = FrameLoja(tab_loja,global_vars.usuarioAtual["id"])
             frame_loja.pack(fill = 'x')

class FrameBiblioteca(ctk.CTkFrame):
    def __init__(self, master, _user_id):
        super().__init__(master)
        self.user_id = _user_id
        self.jogo_selecionado = None
        
        def atualizar_combobox(_resultados):
            jogos = [row[0] for row in _resultados]
            self.combobox.configure(values=jogos)

        def selecionarJogo(_nome):
            conn = sqlite3.connect("sharpgear-ui/database/sharp_database.db")
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            try: 
                cursor.execute("""
                               SELECT *
                               FROM games
                               WHERE name = ?
                               """,(_nome,))
                
                result = cursor.fetchone()
                
                if result:
                    self.jogo_selecionado = dict(result)
                    print(self.jogo_selecionado)
                else:
                    print(f"Jogo não encontrado {_nome}")
            except sqlite3.Error as e:
                print("Erro ao buscar jogos na biblioteca:", e)
            finally:
                conn.close()

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

        def iniciarJogo():
            if self.jogo_selecionado:
                webbrowser.open(self.jogo_selecionado["gameURL"], new=1)

        # Combobox para busca de jogos
        self.combobox = ctk.CTkComboBox(master=self, values=[], width=220,state="normal",font=('Poppins', 13,'bold'), command=selecionarJogo)
        self.combobox.grid(row=0, column=0, padx=15, pady=10,sticky = "n")

        self.combobox.set("")
        self.combobox.bind("<KeyRelease>",procurar_jogos)

        #Imagem do jogo
        self.imagem_grande = ctk.CTkImage(dark_image=Image.open("sharpgear-ui\images\library_survnlive.png"), size=(960, 750))
        self.imagem_label_grande = ctk.CTkLabel(self, image=self.imagem_grande, text="")
        self.imagem_label_grande.grid(row = 0, column = 1)

        self.botao = ctk.CTkButton(self,text="JOGAR",font=('Poppins',16,'bold'), command=iniciarJogo)
        self.botao.place(x= 950,y=400)

class FrameLoja(ctk.CTkFrame):
    def __init__(self,master, _user):
        super().__init__(master)

        self.label = ctk.CTkLabel(self,text="Destaque e Recomendados:")
        self.label.place(x= 40, y = 50)

        ##SURV N LIVE
        
        #Imagem do jogo
        self.imagem_grande = ctk.CTkImage(dark_image=Image.open("sharpgear-ui\images\splash_survnlive.png"), size=(384, 216))
        self.imagem_label_grande = ctk.CTkLabel(self, image=self.imagem_grande, text="")
        self.imagem_label_grande.grid(row = 1,column = 1)

        self.snl_frame = ctk.CTkFrame(self)
        self.snl_frame.grid(row =0, column = 2)

        self.label = ctk.CTkLabel(self.snl_frame,text="Surv N Live",font=("Poppins",15,"bold"))
        self.label.grid(row = 0,column = 0,sticky = 'n')

class FramePerfil(ctk.CTkFrame):
    def __init__(self, master, _user):
        super().__init__(master)

        # Exibe o nome do usuário no frame de perfil
        self.label = ctk.CTkLabel(self, text=_user)
        self.label.grid(row=0, column=0)
