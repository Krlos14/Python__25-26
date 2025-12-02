agenda = {}
for i in range (3):
    nombre =  input(f"¿Como te llamas?")
    tlf = input(f"¿Cual es tu numero?")
    agenda[nombre] = tlf

for nombre, tlf in agenda.items():
    print(f"{nombre} : {tlf}")

buscar = input("\nBuscar contacto: ")

if buscar in agenda:
    print(f"Teléfono: {agenda[buscar]}")
else:
    print("Contacto no encontrado")