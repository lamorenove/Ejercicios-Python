# Función que realiza la suma de dos números

def sumar(a, b):

 s = a + b

 return s

# Aquí inicia aplicación

numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el primer número: "))

suma = sumar(numero1, numero2)

print("a + b =" ,suma)

def resta(a,b):
 r = a - b
 return r
 
# Aquí inicia aplicación
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el primer número: "))

restar = resta(numero1, numero2)

print("a - b =" ,restar)


def multiplicacion(a,b):
 m = a * b
 return m
 
# Aquí inicia aplicación
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el primer número: "))

multiplicar = multiplicacion(numero1, numero2)

print("a * b =" , multiplicar)

def division(a,b):
 m = a / b
 return m
 
# Aquí inicia aplicación
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el primer número: "))

dividir = division(numero1, numero2)

print("a / b =" , dividir)
