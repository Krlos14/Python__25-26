contador =int(0)

def incrementar():
    """
    En esta funcion se sumara el valor + 1 al contador
    """
    global contador
    contador += 1

def descrementar():
    """
    En esta funcion se sumara el valor - 1 al contador
    """
    global contador
    contador -= 1

def mostrar_contador():
    """
    Esto muestra el estado del contador
    """
    global contador
    print(f"El contador esta en el valor:", contador)

incrementar()
incrementar()
descrementar()
mostrar_contador()