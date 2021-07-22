lista = []
# 0 1  2  3  4   son los índices
numeros = [58, 57, 25, 56, 37]
numeros[1]  # llamo a numernos
mayor = 0

for numero in numeros:
    if numero > mayor:
        mayor = numero
print(mayor)
