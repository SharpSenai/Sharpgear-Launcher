import customtkinter as ctk
from login_register import LoginFrame,RegisterFrame
from PIL import Image,ImageTk

ctk.set_widget_scaling(1.1)
ctk.set_default_color_theme("ctkthemebuilder/ctk_theme_builder/user_themes/sharpgear.json")
ctk.set_appearance_mode("Dark")

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('0x0')
        icon = ImageTk.PhotoImage(Image.open("sharpgear-ui\images\sg_logo.png"))
        self.iconphoto(True,icon)
        self.iconify() 
        LoginWindow()

class Login_Register_Tabview(ctk.CTkTabview):
    def __init__(self,master):
        super().__init__(master)
    
        self.configure(anchor = 'w',height = 540)

        tab_login = self.add("Login")
        tab_register = self.add("Register")

        frame_login = LoginFrame(tab_login)
        frame_login.pack()

        frame_register = RegisterFrame(tab_register)
        frame_register.pack()

class LoginWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        print("Janela login aberta")
        self.title('Sharpgear Launcher - Login')
        self.geometry('960x540')
        self.resizable(False, False)

        self.attributes("-topmost", False)  # Remove o comportamento "sempre no topo" após abrir
        # Frame Principal.
        #self.login_frame = LoginFrame(self)
        #self.login_frame.pack(side="left", fill="y")

        self.tabview = Login_Register_Tabview(self)
        self.tabview.place(x = 0,y = -40)

        # Logo Sharpgear Grande
        self.imagem_grande = ctk.CTkImage(dark_image=Image.open("sharpgear-ui\images\gear_darkgray.png"), size=(700, 700))
        self.imagem_label_grande = ctk.CTkLabel(self, image=self.imagem_grande, text="")
        self.imagem_label_grande.place(x=450, y=-70)

app = Main()
app.mainloop()