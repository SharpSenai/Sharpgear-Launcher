import re
from datetime import datetime, timedelta

# Valida senha
def is_valid_password(password: str) -> bool:
    """
    Valida se a senha tem pelo menos 8 caracteres,
    pelo menos uma letra maiúscula, uma minúscula e um caractere especial.
    """
    
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$'
    return bool(re.match(pattern, password))

# Valida email
def is_valid_email(email: str) -> bool:
    """
    Valida se o email segue o formato padrão: nome@dominio.com
    """
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Valida nome
def is_valid_name(name: str) -> bool:
    """
    Valida se o nome contém apenas letras e espaços.
    """
    
    pattern = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$'
    return bool(re.match(pattern, name))

# Valida nome de usuário
def is_valid_username(username: str) -> bool:
    """
    Valida se o nome de usuário tem entre 3 e 12 caracteres.
    """
    
    pattern = r'^[a-zA-Z0-9_]{3,12}$'
    return bool(re.match(pattern, username))

# Valida data de nascimento
def is_valid_date_of_birth(date_of_birth: str) -> bool:
    """
    Valida se a data está no formato DD/MM/YY e é uma data válida.
    """
    
    try:
        birth_date = datetime.strptime(date_of_birth, "%d/%m/%Y")
        
        today = datetime.today()
        min_date = today - timedelta(days=13 * 365.25)
        
        if birth_date > min_date or birth_date > today:
            return False
        
        return True
    except ValueError:
        return False