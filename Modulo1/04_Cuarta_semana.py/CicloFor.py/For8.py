total = 0

for i in range(5):
    nuevoNumero = int(input("Inroduce un numero: "))
    if nuevoNumero == 0:
        total += 1
print("Has introducido", total, "ceros")
