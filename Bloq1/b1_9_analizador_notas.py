"""
Este código hace que el usuario introduzca 3 numeros.
Pero a la hora de hacer el promedio daba error lógico porque faltaba un ()
ya que al no tenerlo, primero dividia la nota3/3. Se soluciono haciendo el array notas que contenga las 3 notas
y hacer la suma de eso antes que la division con ()
"""
nota1 = int(input('Dime la primera nota: '))
nota2 = int(input('Dime la segunda nota: '))
nota3 = int(input('Dime la tercera nota: '))

notas = [nota1, nota2, nota3]

resultado = sum(notas) / 3

print(f'El resultado es: {resultado}')