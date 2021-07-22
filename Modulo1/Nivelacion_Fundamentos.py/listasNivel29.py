lista = []
# 0 1  2  3  4   son los índices
numeros = [58, 57, 25, 56, 37]
numeros[1]  # llamo a numernos
print(numeros[3])
print(numeros[3] >= numeros[2])

for numero in numeros:
    numero = numero ** 2
    print(numero, end=" ")

mensaje = 'Numeros: '
for numero in numeros:
    mensaje = mensaje + str(numero) + ":"

print(mensaje)
