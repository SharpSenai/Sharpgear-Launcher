import customtkinter as ctk
from register import RegisterWindow
from login_frame import LoginFrame

ctk.set_appearance_mode('Dark')

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        print("Janela login aberta")
        self.title('Sharpgear Launcher - Login')
        self.geometry('960x540')
        self.resizable(False, False)

        #Frame Principal.
        self.login_frame = LoginFrame(master=self)
        self.login_frame.pack(side = "left",fill = "y")

    def abrir_registro(self):
        self.withdraw()  # Oculta a janela de login
        RegisterWindow(self)  # Passa a própria janela como master

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
