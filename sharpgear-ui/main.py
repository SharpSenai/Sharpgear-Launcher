import customtkinter as ctk

ctk.set_appearance_mode('Dark')

root = None

def LoginWindow():
    app.destroy()

class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("tab 1")
        self.add("tab 2")
        # add widgets on tabs
        self.label = ctk.CTkLabel(master=self.tab("tab 1"))
        self.label.grid(row=0, column=0, padx=20, pady=10)

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title('Sharpgear Launcher')
        self.geometry('1280x720')

        from register import RegisterFrame

app = App()
root = app
root.mainloop()
