def validar_password(password):

    tiene_numero = False
    tiene_mayuscula = False
    tiene_minuscula = False

    # regla 1: longitud mínima
    if len(password) < 8:
        return False

    # recorrer cada caracter
    for caracter in password:
        if caracter.isdigit():
            tiene_numero = True
        elif caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True

    # validar todas las reglas
    if tiene_numero and tiene_mayuscula and tiene_minuscula:
        return True
    else:
        return False


print(validar_password(""))          # False
print(validar_password("12345678"))  # False
print(validar_password("abcdefgh"))  # False
print(validar_password("ABCDEFGH"))  # False
print(validar_password("Abcdefgh"))  # False
print(validar_password("Abcdefg1"))  # True
print(validar_password("Hola1234"))  # True