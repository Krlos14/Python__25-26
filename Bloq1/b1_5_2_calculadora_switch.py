from unittest import case

num1 = int(input("Ingresa un numero1: "))
num2 = int(input("Ingresa un numero2: "))

print(f"----------------")
print(f"Sumar 1.")
print(f"Resta 2.")
print(f"Multiplicacion 3.")
print(f"Division 4.")
opc = int(input("Ingresa una operacion: "))
match opc:
    case 1:
        resultado = num1 + num2
        print(f"El resultado es: {resultado}")
    case 2:
        resultado = num1 - num2
        print(f"El resultado es: {resultado}")
    case 3:
        resultado = num1 * num2
        print(f"El resultado es: {resultado}")
    case 4:
        resultado = num1 / num2
        print(f"El resultado es: {resultado}")
    case _:
        print("Operacion no reconocida")