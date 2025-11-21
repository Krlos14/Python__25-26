num1 = int(input("Ingresa un numero 1: "))
num2 = int(input("Ingresa un numero 2: "))


print(f"Suma(s), Resta(r), Multiplicacion(m), Division(d)")
opcion = input("Que quieres hacer: ")

if opcion == "s":
    resultado = num1 + num2
    print(f"El resultado es: {resultado}")
elif opcion == "r":
    resultado = num1 - num2
    print(f"El resultado es: {resultado}")
elif opcion == "m":
    resultado = num1 * num2
    print(f"El resultado es: {resultado}")
elif opcion == "d":
    resultado = num1 / num2
    print(f"El resultado es: {resultado}")