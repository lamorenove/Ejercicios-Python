
'''
Desarrolle un algoritmo que permita convertir
calificaciones numéricas a letras, según la
siguiente tabla: Se asume que la nota es un
numero entero y está comprendida entre 1 y 20.

A = 19 y 20,
B = 16, 17  y 18
C = 13, 14 y 15
D = 10, 11 y 12,
E =  1 hasta el  9.

'''
# Función que determina si la nota es A,B,C,D o E.

print("\n")

nota = int(input("Digitar la nota: "))

if (nota > 18):
    print("Tu nota es A")
else:
    if (nota > 15):
        print("Tu nota es B")
    else:
        if (nota > 12):
            print("Tu nota es C")
            if (nota > 9):
                print("Tu nota es D")
            else:
                print("Tu nota es E")
print('\n')


print("\n")
