import customtkinter as ctk
from PIL import Image
import sqlite3
import database
import global_vars
import game_handler

class TabView(ctk.CTkTabview):
    def __init__(self, master):
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
        if global_vars.usuarioAtual is None:
            print("Erro: Nenhum usuário está logado!")
            raise ValueError("Nenhum usuário está logado!")
        else:
             frame_biblioteca = FrameBiblioteca(tab_biblioteca, global_vars.usuarioAtual["id"])
             frame_biblioteca.pack(side='left', fill='both')
        
             frame_perfil = FramePerfil(tab_perfil)
             frame_perfil.pack()

             frame_loja = FrameLoja(tab_loja)
             frame_loja.pack(fill = 'both')

class FrameBiblioteca(ctk.CTkFrame):
    def __init__(self, master, _user_id):
        super().__init__(master)
        self.user_id = _user_id
        self.jogo_selecionado = None
        
        def atualizar_combobox(_resultados):
            jogos = [row[0] for row in _resultados]
            self.combobox.configure(values=jogos)

        def selecionarJogo(_nome):
            self.jogo_selecionado = database.get_gameInfo(_nome)
            get_img = database.get_gameImages(self.jogo_selecionado["name"])
            self.imagem_grande = ctk.CTkImage(dark_image=Image.open(get_img["Thumb"]), size=(1920/2.1, 1500/2.1))
            self.imagem_label_grande = ctk.CTkLabel(self, image=self.imagem_grande, text="")
            self.imagem_label_grande.grid(row = 0, column = 1)
            
            self.botao = ctk.CTkButton(self,text="JOGAR",font=('Poppins',16,'bold'), command= lambda:game_handler.gameHandler(self.jogo_selecionado))
            self.botao.place(x= 950,y=370)
            print(self.jogo_selecionado)

            self.game_desc = ctk.CTkLabel(self,bg_color='black',justify = 'left',font=("Poppins",14),text=self.jogo_selecionado["desc"])
            self.game_desc.place(x=280,y = 450)

            self.game_dev = ctk.CTkLabel(self,bg_color='black',justify = 'right',font=("Poppins",14),text=f"Desenvolvedor: {self.jogo_selecionado["developer"]}")
            self.game_dev.place(x=880,y = 450)


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
        self.combobox = ctk.CTkComboBox(master=self, values=[""], width=220,state="normal",font=('Poppins', 13,'bold'), command=selecionarJogo)
        self.combobox.grid(row=0, column=0, padx=15, pady=10,sticky = "n")
        procurar_jogos(None)

        self.combobox.set("")
        self.combobox.bind("<KeyRelease>",procurar_jogos)

        self.imagem_grande = ctk.CTkImage(dark_image=Image.open('sharpgear-ui\images\library_sharpgear.png'), size=(1920/2.1, 1500/2.1))
        self.imagem_label_grande = ctk.CTkLabel(self, image=self.imagem_grande, text="")
        self.imagem_label_grande.grid(row = 0, column = 1)

class FrameLoja(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        class FrameJogoLoja(ctk.CTkFrame):
            def __init__(self, parent,_titulo, _desc, _splash, _shot0, _shot1, _price):
                super().__init__(parent)

                def adquirir_jogo():
                    self.btt_adquirir.configure(state = "disabled",text = "Adquirido")
                    database.add_jogo_biblioteca(global_vars.usuarioAtual["user"],_titulo)
                
                # Configuração do frame principal
                self.main_frame = ctk.CTkFrame(self)
                self.main_frame.grid(row=0, column=0)
                
                # Imagem do jogo
                self.imagem_grande = ctk.CTkImage(dark_image=Image.open(_splash), size=(1920/4, 1080/4))
                self.imagem_label_grande = ctk.CTkLabel(self.main_frame, image=self.imagem_grande, text="")
                self.imagem_label_grande.grid(row=0, column=0,padx = 10)

                # Frame lateral
                self.side_frame = ctk.CTkFrame(self.main_frame)
                self.side_frame.grid(row=0, column=1)

                # Título
                self.label_titulo = ctk.CTkLabel(self.side_frame, justify='left', font=("Poppins", 17, "bold"), text=_titulo)
                self.label_titulo.grid(row=0, column=0, sticky='w', padx=20, pady=10)

                # Screenshots do Jogo
                self.screenshot_1 = ctk.CTkImage(dark_image=Image.open(_shot0), size=(1920/14, 1080/14))
                self.label_screenshot_1 = ctk.CTkLabel(self.side_frame, justify='left', image=self.screenshot_1, text="")
                self.label_screenshot_1.grid(row=1, column=0, sticky='w', padx=20)

                self.screenshot_2 = ctk.CTkImage(dark_image=Image.open(_shot1), size=(1920/14, 1080/14))
                self.label_screenshot_2 = ctk.CTkLabel(self.side_frame, image=self.screenshot_2, text="")
                self.label_screenshot_2.grid(row=1, column=0, sticky='e', padx=40)

                # Descrição
                self.label_descricao = ctk.CTkLabel(
                    self.side_frame,
                    font=("Poppins", 12, "bold"),
                    justify='left',
                    text=_desc
                )
                self.label_descricao.grid(row=2, column=0, sticky='w', padx=20, pady=10)

                # Botão de Adquirir
                self.btt_adquirir = ctk.CTkButton(self.side_frame, font=("Poppins", 12, "bold"), text="Adquirir",command=adquirir_jogo)
                self.btt_adquirir.grid(row=3, column=0, sticky='w', padx=20, pady=5)

                # Preço e status
                self.label_preco = ctk.CTkLabel(
                    self.side_frame,
                    font=("Poppins", 15, "bold"),
                    justify='left',
                    text="Gratuito            ̶{}̶".format(_price)
                )
                self.label_preco.grid(row=3, column=0, sticky='e', padx=20, pady=10)

        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.configure(width = 1280,height = 720)
        self.scroll_frame.pack(fill = 'both')

        self.label = ctk.CTkLabel(self.scroll_frame,text="Originais Sharpgear:", font=("Poppins", 20,"bold"))
        self.label.pack(anchor = 'w',padx = 150,pady = 10)

        game_info = database.get_gameInfo("Surv N Live")
        get_images = database.get_gameImages("Surv N Live")

        self.snl_frame = FrameJogoLoja(self.scroll_frame,game_info["name"],
                                       game_info["desc"],
                                        get_images["Capa"],
                                        get_images["Screenshot0"],
                                        get_images["Screenshot1"],
                                        "R$20"
                                        )
        
        self.snl_frame.pack()

        game_info = database.get_gameInfo("Hell-O World")
        get_images = database.get_gameImages("Hell-O World")

        self.hw_frame = FrameJogoLoja(self.scroll_frame,game_info["name"],
                                       game_info["desc"],
                                        get_images["Capa"],
                                        get_images["Screenshot0"],
                                        get_images["Screenshot1"],
                                        ""
                                        )
        
        self.hw_frame.pack(pady = 50)

class FramePerfil(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        class FrameUserInfo(ctk.CTkFrame):
            def __init__(self, parent):
                super().__init__(parent)

                font_titulo = ("Poppins", 18, "bold")  # Fonte maior para título
                font_padrao = ("Poppins", 16, "bold")         # Fonte padrão para informações

                # Configuração do frame principal
                self.main_frame = ctk.CTkFrame(self)
                self.main_frame.pack()
                
                # Imagem do jogo
                self.imagem_grande = ctk.CTkImage(dark_image=Image.open("sharpgear-ui\images\sg_pfp_ph.png"), size=(200,200))
                self.imagem_label_grande = ctk.CTkLabel(self.main_frame, image=self.imagem_grande, text="")
                self.imagem_label_grande.grid(row=0, column=0,padx = 10)

                # Frame lateral
                self.side_frame = ctk.CTkFrame(self.main_frame)
                self.side_frame.grid(row=0, column=1)

                self.username = ctk.CTkLabel(self.side_frame, text=f"Usuário: {global_vars.usuarioAtual["user"]}", font=font_titulo)
                self.username.grid(row = 0, column = 0,pady = 10, padx = 10, sticky = 'w')

                self.nome = ctk.CTkLabel(self.side_frame, text=f"Nome: {global_vars.usuarioAtual["nome"]}", font=font_padrao)
                self.nome.grid(row=1, column=0,pady = 3, padx = 10, sticky = 'w')

                self.email = ctk.CTkLabel(self.side_frame, text=f"Email: {global_vars.usuarioAtual["email"]}", font=font_padrao)
                self.email.grid(row=2, column=0,pady = 3, padx = 10, sticky = 'w')

                self.nasc = ctk.CTkLabel(self.side_frame, text=f"Data de Nascimento: {global_vars.usuarioAtual["nasc"]}", font=font_padrao)
                self.nasc.grid(row=3, column=0,pady = 3, padx = 10, sticky = 'w')

        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.configure(width = 1280,height = 720)
        self.scroll_frame.pack(fill = 'both')
        
        user_profile = FrameUserInfo(self.scroll_frame)
        user_profile.pack(pady = 20)

        #
        '''
        # Exibe o nome do usuário no frame de perfil
        

'''