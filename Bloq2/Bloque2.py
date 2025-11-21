nombre = input("¿Como te llamas?")


def saludo(n, a="Rodriguez"):
    print (n , a)

saludo(nombre, "Perro")


def menu_principal():
    print(f" 1) Jugar")
    print(f" 2) Configuracion")
    print(f" 3) Salir")

    opc = int(input("¿Que quieres hacer?"))

    match opc:
        case 1:
            print(f"Bienvenido el juego")
        case 2:
            print(f"Bienvenido a la configuracion")
        case 3:
            print(f"HASTA LA PROXIMA")
            exit()
        case _:
            print(f"Error ingrese un numero válido")

    print("Seguimos")
menu_principal()

