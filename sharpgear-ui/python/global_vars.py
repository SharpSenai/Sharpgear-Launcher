# Biblioteca feita só para guardar váriaveis globais
# Para que outros scripts possam interagir e etc...
usuarioAtual = None

""" 
Exemplo de uso:
    import globalVars
    print(globalVars.usuarioAtual) 
    -> {'id': 8, 'nome': 'zé', 'user': 'xpotatox', 'email': 'xpx@gmail.com', 'senha': 'ffsffsdf', 'nasc': '08022008'}

    print(globalVars.usuarioAtual["id"])
    -> 8
    
    print(globalVars.usuarioAtual["user"])
    -> xpotatox
    
    print(globalVars.usuarioAtual["email"])
    -> xpx@gmail.com
    
Como funciona:
    Na função "verificar_usuario" no register.py apartir linha 49 eu fiz que a variável se tornasse global aqui do globalVars.py,
    usei a classe "currentUser" de database.py pra guardar as informações pelo __init__, usando do metodo .getInfo() para armazenar
    na variavel usuarioAtual deste script. 
"""