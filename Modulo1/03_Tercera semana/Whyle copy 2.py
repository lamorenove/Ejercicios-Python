'''
Diseñe un algoritmo que permita contar los números pares 
existentes en una serie de 1 a n, siendo n un número digitado
por un usuario

Entrada : n
Salida  : cantidad de números pares entre 1 y n
Proceso :
i = 1
cp = 0
mientras (i <= n) haga
   si ((i % 2 ) == 0
   cp += 1
   fin si
   i += 1
fin mientras
'''

n = int(input("Ingrese un numero: "))
i = 1
cp = 0

while(i <= n):
    if(i % 2 == 0):
        cp += 1

    i += 1

print(cp)
