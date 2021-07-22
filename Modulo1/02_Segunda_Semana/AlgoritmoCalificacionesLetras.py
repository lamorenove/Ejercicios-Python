
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


def nota(nota: int):
    if (nota == 19 or nota == 20):
        print("Tu nota es A")
    if (nota == 16 or nota == 17 or nota == 18):
        print("Tu nota es B")
    if (nota == 13 or nota == 14 or nota == 15):
        print("Tu nota es C")
    if (nota == 10 or nota == 11 or nota == 12):
        print("Tu nota es D")
    if (nota >= 1 and nota <= 9):
        print("Tu nota es E")


nota(int(input("Digite la nota: ")))
