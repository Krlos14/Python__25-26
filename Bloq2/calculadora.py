a = int(input("Introduce el numero primer numero"))
b = int(input("Introduce el segundo numero"))

def suma(a, b):
    """
    Esta funcion suma los dos valores dados por el u
    """
    total = a+b
    return  total

def resta(a, b):
    """
    Esta funcion resta los dos valores dados por el u
    """
    total = a-b
    return  total

def division(a, b):
    """
    Esta funcion divide los dos valores dados por el u
    """
    total = a/b
    return  total

def multiplicacion(a, b):
    """
    Esta funcion multiplica los dos valores dados por el u
    """
    total = a*b
    return  total

print(f"La suma es :", suma(a,b))
print(f"La resta es :", resta(a,b))
print(f"La division es :", division(a,b))
print(f"La multiplicacion es:", multiplicacion(a,b))
