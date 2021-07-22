"""1. Introducir 10 números y sumar solo los números pares. Imprimir la sumatoria"""

total = 0

for i in range(10):
    nuevoNumero = int(input("Inroduce un numero: "))
    if nuevoNumero % 2 == 0:
        total += 1
print("Has introducido", total, "pares")
