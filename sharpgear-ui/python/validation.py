import re 

def validate_username(username):
    return re.match(r'^[a-zA-Z0-9_]{3,15}$', username)

def validate_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

def validate_password(password):
    return re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$', password)

def validate_persona(persona):
    return re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?: [A-Za-zÀ-ÖØ-öø-ÿ]+)*$", persona)
    
def validate_birthday(birthday):
    return re.match(r"^(0[1-9]|[12][0-9]|3[01])([ /]?)(0[1-9]|1[0-2])\2(\d{4})$", birthday)