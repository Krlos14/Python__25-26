compras = []

for i in range(5):
    productos = input(f"Productos {i+1}:")
    compras.append(productos)

print(f"Lista de productos {compras}")

eliminar = input("¿Que producto deseas eliminar?:")
if eliminar in compras:
    compras.remove(eliminar)
else:
    print("Este productono existe")

compras.sort()
print(f"Lista ordenada {compras}")