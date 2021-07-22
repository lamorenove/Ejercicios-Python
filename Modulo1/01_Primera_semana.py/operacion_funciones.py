# Función que realiza la suma de dos números

def suma(a, b):
    suma = a + b
    return suma


def resta(a, b):
    resta = a - b
    return resta

# Aquí inicia la aplicación


numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))

sumar = suma(numero1, numero2)

print("a + b =", sumar)


# Aquí inicia la aplicación


numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))

restar = resta(numero1, numero2)

print("a - b =", restar)
