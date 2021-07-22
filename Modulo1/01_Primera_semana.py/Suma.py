# Algoritmo de la suma de dos números
''' Se desea la suma de dos numeros enteros y presentar en pantalla su resultado.

ENTRADAS : Num1, Num2

PROCESO : LA SUMA DE LOS NÚMEROS --> SUMA = Num1 + Num2

SALIDAS:  LA SUMA DE LOS NÚMEROS -->

INICIO
    Num1, Num2, Suma: Enteros
    ESCRIBA "Diga dos números:"
    LEA Num1, Num2
    ESCRIBA "La suma de los dos números es:", suma
FIN
'''

# Suma de dos Números

num1 = int(input("Diga el primer número:"))
num2 = int(input("Diga el degundo número:"))

# Guarda el resultado de la suma de dos números
suma = num1 + num2

print("La suma de dos números es:", suma)

# Función para crear una suma de dos números


def suma(nota1: int, nota2: int) -> int:
    resultado = nota1 + nota2
    return resultado


print(suma(10, 20))
