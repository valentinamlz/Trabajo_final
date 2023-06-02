import re as r

#Función para validar el inicio de sesión
def login(username, password, users):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

#Función para agregar un nuevo usuario
def add_user(username, password, users):
    new_user = {"username": username, "password": password}
    users.append(new_user)
    return users

#Función para validar que el usuario ingrese únicamente números
def integer(val):
    while True:
        try: 
            val = int(val)
            return val
        except ValueError:
            return integer(input("Error, digite un valor numérico: ")) 

#Función para validar que el usario ingrese únicamente letras
def letters(letter=""):
    value = input(letter)
    next = r.match("^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]+$", value)
    if next:
        return value
    else:
        print("\n")
        print("Error, escriba solo letras")
        return letters(letter)
    