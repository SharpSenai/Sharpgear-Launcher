import customtkinter as ctk
from register import abrir_janela_registro  # Agora apenas a função que inicia o registro é importada

ctk.set_appearance_mode("Dark")

# Função para abrir a janela principal
def abrir_janela_principal():
    janela_principal = ctk.CTk()
    janela_principal.title("Sharpgear Launcher")
    janela_principal.geometry("1280x720")

    label = ctk.CTkLabel(janela_principal, text="Bem-vindo ao Sharpgear Launcher!")
    label.pack(pady=20)

    janela_principal.mainloop()

# Classe da Janela Inicial de Login
class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sharpgear Launcher")
        self.geometry("800x500")

        label = ctk.CTkLabel(self, text="Bem-vindo! Clique para registrar.")
        label.pack(pady=20)

        # Botão para abrir a janela de registro
        botao_registrar = ctk.CTkButton(self, text="Registrar", command=self.abrir_e_fechar)
        botao_registrar.pack(pady=20)

    def abrir_e_fechar(self):
        self.destroy()  # Fecha a janela de login
        abrir_janela_registro(abrir_janela_principal)  # Passa a função como argumento

# Inicia o programa com a janela de login
if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
