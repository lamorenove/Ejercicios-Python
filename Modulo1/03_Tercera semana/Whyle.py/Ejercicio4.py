'''
Algoritmo que permita obtener el promedio de la cantidad de números
que el usuario desea digitar, preguntando además, si desea continuar o no
'''
print("\n")
continuar = 'si'
suma, contador = 0, 0
while continuar == 'si':
    numero = int(input("Ingrese un número: "))
    suma = suma + numero
    contador += 1
    consulta = input("¿desea continuar?: ")
    continuar = consulta.lower()
promedio = round(suma/contador)
print("El promedio de los números ingresados es: ", promedio)
print("\n")
