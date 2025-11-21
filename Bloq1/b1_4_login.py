usuario_correcto = "admin"
contrasena_correcta = "1234"

user = input("Nombre de usuario: ")
contrasena = input("Contraseña: ")


if usuario_correcto == user and contrasena_correcta == contrasena:
    print("Acceso concedido")
else:
    print("Acceso denegado")
