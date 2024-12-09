import subprocess
import webbrowser

def openExe(_path):
    print("É executável")
    try:
        subprocess.run(_path, check=True)
    except FileNotFoundError:
        print("Jogo não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")
        
def openBrowser(_path):
    print("É web")
    webbrowser.open(_path, new=1, autoraise=True)

def gameHandler(gameInfo):
    if gameInfo["isExe"] == 0:
        openBrowser(gameInfo["gameURL"])
    elif gameInfo["isExe"] == 1:
        openExe(gameInfo["gameURL"])
    else:
        print("Jogo não especificado.")
        print(gameInfo)