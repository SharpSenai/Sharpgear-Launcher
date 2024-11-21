import customtkinter
class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


        # create tabs
        self.add("tab 1")
        self.add("tab 2")
        self.add("tab 3")
        self.add("tab 4")


        # add widgets on tabs
        self.label = customtkinter.CTkLabel(master=self.tab("tab 1"),anchor='e')
        self.label.grid(row=0, column=0, padx=20, pady=10)

        self.label = customtkinter.CTkLabel(master=self.tab("tab 2"),text="SSSA")
        self.label.grid(row=0, column=0, padx=20, pady=10)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0,sticky = 's', column=0, padx=0, pady=0,)


app = App()
app.mainloop()