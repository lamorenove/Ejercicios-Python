"""
4. Leer 10 números e imprimir la sumatoria de los pares, impares y la suma total de los 10 números. 
"""
sumap = 0
sumai = 0
sumat = 0
for i in range(10):
    numero = int(input("Introduzca numero: "))
    sumat += numero
    if numero % 2 == 0:
        sumap += numero
    else:
        sumai += numero
print("la sumatoria de los numeros pares es:", sumap)
print("la sumatoria de los numeros impares es:", sumai)
print("la sumatoria de los numeros es:", sumat)
