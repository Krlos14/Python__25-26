usuario = None
password = None

while True:
    print("\n¿Qué quieres hacer?")
    print("[1] Registrarse  [2] Iniciar sesión  [3] Salir")
    opcion = input("Selecciona una opción: ")

    # REGISTRARSE
    if opcion == "1":
        while True:
            email = input("Introduce tu email: ")

            # Validaciones básicas del email
            if len(email) < 3:
                print("Email demasiado corto.")
                continue
            if "@" not in email:
                print("El email debe contener '@'.")
                continue
            if not (email.endswith(".com") or email.endswith(".es") or email.endswith(".net")):
                print("El email debe terminar en .com, .es o .net.")
                continue

            contraseña = input("Introduce tu contraseña: ")

            # Validaciones básicas de contraseña
            if len(contraseña) < 8:
                print("La contraseña debe tener al menos 8 caracteres.")
                continue

            tiene_mayus = False
            tiene_numero = False
            tiene_simbolo = False

            for c in contraseña:
                if c.isupper():
                    tiene_mayus = True
                if c.isdigit():
                    tiene_numero = True
                if c in "!@#$%&*?":
                    tiene_simbolo = True

            if not tiene_mayus or not tiene_numero or not tiene_simbolo:
                print("La contraseña debe tener al menos una letra mayúscula, un número y un símbolo (!@#$%&*?).")
                continue

            usuario = email
            password = contraseña
            print("Usuario registrado correctamente.")
            break

    # INICIAR SESIÓN
    elif opcion == "2":
        if usuario is None:
            print("No hay usuarios registrados. Por favor, regístrate primero.")
            continue

        email_login = input("Introduce tu usuario: ")
        if email_login != usuario:
            print("Usuario no encontrado.")
            continue

        intentos = 3
        while intentos > 0:
            pwd = input("Introduce tu contraseña: ")
            if pwd == password:
                print("Acceso concedido. Bienvenido.")
                break
            else:
                intentos -= 1
                print("Contraseña incorrecta. Intentos restantes:", intentos)

        if intentos == 0:
            print("Demasiados intentos fallidos. Volviendo al menú.")

    # SALIR
    elif opcion == "3":
        print("Fin del programa.")
        break

    else:
        print("Opción no válida.")