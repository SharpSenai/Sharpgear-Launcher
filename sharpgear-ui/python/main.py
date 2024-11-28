import customtkinter as ctk
from register import RegisterWindow
from login_frame import LoginFrame
from PIL import Image

ctk.set_appearance_mode('Dark')
ctk.set_widget_scaling(1.1)

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('0x0')
        LoginWindow()

class LoginWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        print("Janela login aberta")
        self.title('Sharpgear Launcher - Login')
        self.geometry('960x540')
        self.resizable(False, False)
        self._set_scaling(5, 1.5)

        # Frame Principal.
        self.login_frame = LoginFrame(master=self)
        self.login_frame.pack(side="left", fill="y")

        # Logo Sharpgear Grande
        self.imagem_grande = ctk.CTkImage(dark_image=Image.open("sharpgear-ui\\images\\gEar alpha3.png"), size=(700, 700))
        self.imagem_label_grande = ctk.CTkLabel(self, image=self.imagem_grande, text="")
        self.imagem_label_grande.place(x=490, y=-50)

    def abrir_registro(self):
        self.withdraw()  # Oculta a janela de login
        RegisterWindow(self)  # Passa a própria janela como master

app = Main()
app.mainloop()