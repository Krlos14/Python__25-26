nombre = str(input("¿como te llamas?"))
edad = int(input("¿Cuantos años tienes?"))


def registrar_usuario(nombre, edad, ciudad= "Madrid"):
    """
    Esta funcion muestra el nombre, edada y ciudad del usuario introducido
    y por defecto la ciudad es Madrid
    """
    print(f"Usuario: {nombre} | Edad: {edad} | Ciudad: {ciudad}")

registrar_usuario(nombre, edad)

nombre = str(input("¿como te llamas?"))
edad = int(input("¿Cuantos años tienes?"))
ciudad = str(input("¿Donde vives?"))

registrar_usuario(nombre, edad, ciudad)

