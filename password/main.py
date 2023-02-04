import hashlib

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in "!@#$%^&*" for char in password):
        return False
    return True

while True:
    password = input("Choisissez un mot de passe: ")
    if validate_password(password):
        break
    else:
        print("Le mot de passe ne respecte pas les exigences de sécurité suivante (au moins 8 caractères, une lettre majuscule, une lettre minuscule, moins un chiffre, un caractère spécial (!, @, #, $, %, ^, &, *)")
