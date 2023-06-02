#Importación de librerías
import mysql.connector
import json

#Importación de las funciones creadas por nosotros
from functions import login, add_user, integer, letters

#Parámetros para conectarme a mi base de datos
SERVER = "localhost"
USER = "informatica1"
PASSWORD = "bio123"
DB = "informatica1"
#Se hace el llamado
connection = mysql.connector.connect(user=USER , password=PASSWORD , host=SERVER , database=DB)
#Se hace la conexión
cursor = connection.cursor()


#Abrir el archivo JSON
with open("Trabajo_Final - Valentina Marquez y\login.json", "r") as f:
    data = json.load(f)
    users = data["users"]

while True:
    #Pedir al usuario que ingrese su nombre de usuario y contraseña
    print("\n")
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    #Validar el inicio de sesión
    if login(username, password, users):
        print("\n")
        print("Inicio de sesión exitoso. Bienvenido")
        break
    else:
        print("\n")
        print("Nombre de usuario o contraseña incorrectos")

                    


while True:
    #Menú principal
    print("\n")
    main = input("""
    Gestionar la información de:
    1. Medicamentos.
    2. Proveedores.
    3. Ubicaciones.
    4. Usuarios.
    5. Salir. 
    > """)

    if main == "1":
    #Menú medicamentos
        while True: 
            print("\n")
            medicinemenu = input("""
            Escoja la opción que desea realizar:
            1. Ingresar un nuevo medicamento.
            2. Actualizar la información de un medicamento.
            3. Buscar medicamentos.
            4. Ver la información de todos los medicamentos almacenados.
            5. Eliminar un medicamento.
            6. Volver al menú principal.
            > """)

            if medicinemenu == "1":
            #Ingresar un nuevo medicamento

                #Se piden los datos que vamos a almacenar
                print("\n")
                lote = integer(input("Lote: "))
                name = letters("Nombre del medicamento: ")
                distributor = letters("Distribuidor: ")
                stock = integer(input("Cantidad en bodega: "))
                date = input("Fecha de llegada (AAAA-MM-DD): ")
                price = integer(input("Precio de venta: "))

                #Se ingresa en la base de datos
                medicine = "insert  into medicine(id, lote, name, distributor, stock, date, price) values (%s,%s,%s,%s,%s,%s,%s)"
    
                cursor.execute(medicine,(None, lote, name, distributor, stock, date, price))
                #Se confirman los cambios en la base de datos con commit
                connection.commit()


                #Mostrar el código, nombre y apellidos del proveedor responsable
                showprovider = f"select provider.code, provider.name, provider.lastname from provider"
                cursor.execute(showprovider)
                results = cursor.fetchall()

                #Mostrar los responsables existentes
                print("\n")
                print("Responsables disponibles:")
                for i, result in enumerate(results):
                    print(f"{i+1}) {result[0]} - {result[1]} {result[2]}", end =  "\n" )
                #Se le pide al usuario que escoja
                print("\n")
                choose = integer(input("Digite el código del responsable elegido: "))

                getresponsible = f"select name, lastname from provider where code = '{choose}'"
                cursor.execute(getresponsible)

                #Obtención del resultado
                result = cursor.fetchone()

                #Impresión del resultado
                if result:
                    print("\n")
                    print(f"El responsable seleccionado fue: {result[0]} {result[1]}")
                else:
                    print("\n")
                    print("El código ingresado no es válido.")

                #Mostrar el código y el nombre de la ubicación
                showlocation = f"select location.code, location.name from location"
                cursor.execute(showlocation)
                resultss = cursor.fetchall()
                
                print("\n")
                print("Ubicaciones disponibles:")
                #Mostrar ubicaciones existentes
                for i, resultt in enumerate(resultss):
                    print(f"{i+1}) {resultt[0]} - {resultt[1]}", end =  "\n" )
                #Se le pide al usuario que escoja
                print("\n")
                choosee = input("Digite el código de la ubicación elegida: ")
                
                getlocation = f"select name from location where code = '{choosee}'"
                cursor.execute(getlocation)

                #Obtención del resultado
                resultt = cursor.fetchone()

                #Impresión del resultado
                if resultt:
                    print("\n")
                    print(f"La ubicación seleccionada fue: {resultt[0]}")
                else:
                    print("\n")
                    print("El código ingresado no es válido.")


                print("\n")
                print("Datos guardados con éxito")

            elif medicinemenu == "2":
            #Actualizar medicamento
                print("\n")
                lote = integer(input("Digite el lote del medicamento que quiere modificar: "))
                while True:
                    print("\n")
                    column = input("""
                    Escoja el área que quiere cambiar:
                    1. Nombre
                    2. Distribuidor
                    3. Stock
                    4. Precio
                    > """)

                    if column == '1':
                        change = letters("Ingrese el nombre nuevo: ")
                    elif column == '2':
                        change = letters("Ingrese el distribuidor nuevo: ")
                    elif column == '3':
                        change = integer(input("Digite la cantidad nueva: "))
                    elif column == '4':
                        change = integer(input("Digite el precio nuevo: "))
                    else:
                        print("Error. Escoja una opción válida")
                        #Se repite si el usuario escoje otra opción fuera de las que hay
                        continue

                    if column == '1':
                        search = f"update medicine set name = '{change}' where lote = '{lote}'"
                    elif column == '2':
                        search = f"update medicine set distributor ='{change}' where lote = '{lote}'"
                    elif column == '3':
                        search = f"update medicine set stock = '{change}' where lote = '{lote}'"
                    elif column == '4':
                        search = f"update medicine set price = {change} where lote = '{lote}'"
                    
                    print("\n")
                    print("Medicamento actualizado correctamente")
                    #Se rompe el ciclo si todo se hace bien y se guarda la información en la base de datos
                    break

                cursor.execute(search)
                connection.commit()
            
            elif medicinemenu == "3":
            #Buscar medicamentos
                print("\n")
                lote = input("Digite el lote del medicamento que está buscando: ")
                search = f"select * from medicine where medicine.lote = '{lote}' "
                cursor.execute(search)
                ressults = cursor.fetchall()
                if ressults:
                    print("\n")
                    i = ressults[0]
                    print(f"""Información del medicamento que se está buscando:
                    Código: {i[1]}
                    Nombre: {i[2]}
                    Distribuidor: {i[3]}
                    Fecha: {i[5]}
                    Precio: {i[4]} """)
                else:
                    print("\n")
                    print("El código ingresado no es válido")

            elif medicinemenu == "4":
            #Ver toda la información guardada

                info = "select * from medicine"
                cursor.execute(info)
                result = cursor.fetchall()
                #For para que recorra toda la tabla y saque toda la info ordenada
                for i in result:
                    print(f"""
                        Lote: {i[1]}
                        Nombre: {i[2]}
                        Distribuidor: {i[3]} 
                        Cantidad: {i[4]}
                        Fecha: {i[5]} 
                        Precio: {i[6]} """)

            elif medicinemenu == "5":
            #Eliminar medicamento
                print("\n")
            #Se pide el código correspondiente al medicamento que se quiere eliminar
                lote = integer(input("\Digite el lote del medicamento que quiere eliminar: "))
            #Se elimina de la database
                delete = f"select * from medicine where lote = '{lote}'"
                cursor.execute(delete)
                result = cursor.fetchone()

            #Validar de existencia del medicamento
                #Si existe que lo elimine
                if result is not None:
                    delete = f"delete from medicine where lote = '{lote}'"
                    cursor.execute(delete)
                    connection.commit()

                    print("\n")
                    print("El medicamento ha sido borrado.")
                #Si no existe le dirá al usuario que no se encuentra    
                else:
                    print("\n")
                    print("El medicamento no está en nuestra base de datos")
            
            elif medicinemenu == "6":
                #Volver al menú principal
                break
            else:
                print("\n")
                print("Error. Escoja una opción válida.")
    elif main == "2":
    #Menú proveedores
        while True:
            print("\n")
            providermenu = input("""
            Escoja la opción que desea realizar:
            1. Ingresar un nuevo proveedor.
            2. Actualizar la información de un proveedor.
            3. Buscar proveedores.
            4. Ver la información de todos los proveedores almacenados.
            5. Eliminar un proveedor.
            6. Volver al menú principal.
            > """)
            
            if providermenu == "1":
            #Se piden los datos que vamos a almacenar
                #Ingresar un nuevo proveedor
                print("\n")
                code = integer(input("Código: "))
                name = letters("Nombre: ")
                lastname = letters("Apellido: ")
                id = integer(input("Documento de identidad: "))
                company = letters("Entidad/Compañía: ")


            #Se ingresa en la base de datos
                provider = "insert into provider(id, code, name, lastname, identify, company) values (%s,%s,%s,%s,%s,%s)"
    
                cursor.execute(provider,(None, code, name, lastname, id, company))
            #Se confirman los cambios en la base de datos con commit
                connection.commit()
                print("\n")
                print("Datos guardados con éxito")
                
            elif providermenu == "2":
            #Actualizar proveedor
                print("\n")
                code = integer(input("Digite el código del proveedor que quiere modificar: "))
                while True:
                    column = input("""
                    Escoja el área que quiere cambiar:
                    1. Nombre
                    2. Apellido
                    3. Documento de identidad
                    4. Entidad/Compañía
                    > """)

                    print("\n")
                    if column == '1':
                        change = letters("Ingrese el nombre nuevo: ")
                    elif column == '2':
                        change = letters("Ingrese el apellido nuevo: ")
                    elif column == '3':
                        change = integer(input("Digite el documento de identidad nuevo: "))
                    elif column == '4':
                        change = letters("Ingrese la entidad o compañía nueva: ")
                    else:
                        print("Error. Escoja una opción válida")
                        #Se repite si el usuario escoje otra opción fuera de las que hay
                        continue

                    if column == '1':
                        search = f"update provider set name = '{change}' where code = '{code}'"
                    elif column == '2':
                        search = f"update provider set lastname ='{change}' where code = '{code}'"
                    elif column == '3':
                        search = f"update provider set identify = '{change}' where code = '{code}'"
                    elif column == '4':
                        search = f"update provider company  = {change} where code = '{code}'"

                    print("Proveedor actualizado correctamente")
                    #Se rompe el ciclo si todo se hace bien y se guarda la información en la base de datos
                    break

                cursor.execute(search)
                connection.commit()

            elif providermenu == "3":
            #Buscar proveedor
                print("\n")
                code = input("Digite el código del proveedor que está buscando: ")
                search = f"select * from provider where provider.code = '{code}' "
                cursor.execute(search)
                results = cursor.fetchall()
                if results:
                    print("\n")
                    i = results[0]
                    print(f"""Información del proveedor que se está buscando:
                    Código: {i[1]}
                    Nombres: {i[2]}
                    Apellidos: {i[3]} 
                    Documento de identidad: {i[4]}
                    Compañía/Entidad: {i[5]}""")
                else:
                    print("\n")
                    print("El código ingresado no es válido")
                
                
            elif providermenu == "4":
            #Ver toda la información guardada
                print("\n")
                info = "select * from provider"
                cursor.execute(info)
                result = cursor.fetchall()
                #For para que recorra toda la tabla y saque toda la info ordenada
                for i in result:
                    print(f"""
                        Código: {i[1]}
                        Nombres: {i[2]}
                        Apellidos: {i[3]} 
                        Documento de identidad: {i[4]}
                        Compañía/Entidad: {i[5]} """)

            elif providermenu == "5":
            #Eliminar medicamento
                print("\n")
                #Se pide el código correspondiente al medicamento que se quiere eliminar
                code = integer(input("Digite el código del proveedor que quiere eliminar: "))
                #Se elimina de la database
                delete = f"select * from provider where code = '{code}'"
                cursor.execute(delete)
                result = cursor.fetchone()

            #Validar de existencia del proveedor
                #Si existe que lo elimine
                if result is not None:
                    delete = f"delete from provider where code = '{code}'"
                    cursor.execute(delete)
                    connection.commit()

                    print("\n")
                    print("El proveedor ha sido borrado.")
                #Si no existe le dirá al usuario que no se encuentra    
                else:
                    print("\n")
                    print("El proveedor no está en nuestra base de datos")

            elif providermenu == "6":
                #Volver al menú principal
                break
            else:
                print("\n")
                print("Error. Escoja una opción válida.")
    elif main == "3":

    #Menú ubicaciones
        while True:
            print("\n")
            locationmenu = input("""
            Escoja la opción que desea realizar:
            1. Ingresar una nueva ubicación.
            2. Actualizar la información de una ubicación.
            3. Buscar ubicaciones.
            4. Ver la información de todas las ubicaciones almacenadas.
            5. Eliminar una ubicación.
            6. Volver al menú principal.
            > """)

            if locationmenu == "1":
            #Se piden los datos que vamos a almacenar
                print("\n")
                code = input("Código: ")
                name = letters("Nombre de la ubicación: ")
                number = integer(input("Teléfono: "))
                #Se ingresa en la base de datos
                location = "insert into location(id, code, name, number) values (%s,%s,%s,%s)"
    
                cursor.execute(location,(None, code, name, number))
                #Se confirman los cambios en la base de datos con commit
                connection.commit()

                print("\n")
                print("Datos guardados con éxito")

            elif locationmenu == "2":
            #Actualizar ubicación
                print("\n")
                code = input("Ingrese el código de la ubicación que quiere modificar: ")
                while True:
                    column = input("""
                    Escoja el área que quiere cambiar:
                    1. Nombre
                    2. Teléfono
                    > """)

                    if column == '1':
                        change = letters('Ingrese el nombre nuevo: ')
                    elif column == '2':
                        change = integer(input('Digite el teléfono nuevo: '))
                    else:
                        print("Error. Escoja una opción válida")
                        #Se repite si el usuario escoje otra opción fuera de las que hay
                        continue

                    if column == '1':
                        search = f"update location set name = '{change}' where code = '{code}'"
                    elif column == '2':
                        search = f"update location set number = '{change}' where code = '{code}'"

                    print("\n")
                    print("Ubicación actualizada correctamente")
                    #Se rompe el ciclo si todo se hace bien y se guarda la información en la base de datos
                    break

                cursor.execute(search)
                connection.commit()

            elif locationmenu == "3":
            #Buscar ubicación
                print("\n")
                code = input("Digite el código de la ubicación  que está buscando: ")
                search = f"select * from location where location.code = '{code}' "
                cursor.execute(search)
                results = cursor.fetchall()
                if results:
                    i = results[0]
                    print(f"""Información de la ubicación que se está buscando:
                    Código: {i[1]}
                    Ubicación: {i[2]}
                    Teléfono: {i[3]} """)
                else:
                    print("\n")
                    print("El código ingresado no es válido")
                
            elif locationmenu == "4":
            #Ver toda la información guardada
                print("\n")
                info = "select * from location"
                cursor.execute(info)
                result = cursor.fetchall()
                #For para que recorra toda la tabla y saque toda la info ordenada
                for i in result:
                    print("\n")
                    print(f"""
                        Código: {i[1]}
                        Ubicación: {i[2]}
                        Teléfono: {i[3]} """)

            elif locationmenu == "5":
            #Eliminar ubicación
                print("\n")
                #Se pide el código correspondiente a la ubicación que se quiere eliminar
                code = input("Ingrese el código de la ubicación que quiere eliminar: ")
                #Se elimina de la database
                delete = f"select * from location where code = '{code}'"
                cursor.execute(delete)
                result = cursor.fetchone()

            #Validar de existencia de la ubicación
                #Si existe que lo elimine
                if result is not None:
                    delete = f"delete from location where code = '{code}'"
                    cursor.execute(delete)
                    connection.commit()
                    print("\n")
                    print("La ubicación ha sido borrada.")
                #Si no existe le dirá al usuario que no se encuentra    
                else:
                    print("\n")
                    print("La ubicación no está en nuestra base de datos")
            
            elif locationmenu == "6":
                #Volver al menú principal
                break
            else:
                print("\n")
                print("Error. Escoja una opción válida.")

    elif main == "4":
        #Menú usuarios
        while True:
            print("\n")
            usermenu = input("""Escoja la opción que desea realizar:
            1. Agregar un nuevo usuario
            2. Mostrar los usuarios existentes
            3. Volver al menú principal
            > """)

            if usermenu == "1":
                #Pedir al usuario que ingrese un nuevo usuario
                print("\n")
                new_username = input("Ingrese el nombre de usuario del nuevo usuario: ")
                new_password = input("Ingrese la contraseña del nuevo usuario: ")

                #Agregar el nuevo usuario
                users = add_user(new_username, new_password, users)

                #Guardar los cambios en el archivo JSON
                with open("Trabajo_final/login.json", "w") as f:
                    data["users"] = users
                    json.dump(data, f)

            elif usermenu == "2":
                #Mostrar los usuarios
                print("\n")
                print("Usuarios:")
                for user in users:
                    print("\n")
                    print(user["username"])

            elif usermenu == "3":
                #Volver al menú principal
                break
            else:
                print("\n")
                print("Error. Escoja una opción válida.")

    elif main == "5":
        #Salir
        print("\n")
        print("Adiós")
        break
    else:
        print("\n")
        print("Error. Escoja una opción válida.")
