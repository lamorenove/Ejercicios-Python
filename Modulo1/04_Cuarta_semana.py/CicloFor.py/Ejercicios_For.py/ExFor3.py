"""3. Leer 4 números. Imprimir la sumatoria y su promedio."""

total = 0
contar = 0

for i in range(4):
    nuevoNumero = int(input("Introduce un número: "))
    total += nuevoNumero
    contar = contar + 1

promedio = round(total/contar, 2)

print("El total es: ", total, "y el promedio es: ", promedio)
