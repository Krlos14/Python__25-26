"""
Esto en una app que va a pedir un número y te va a mostrar su tabla de multiplicar entera.
La tabla sera del 1-10
"""

numero = int(input("¿Que número quieres usar? "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")