# Leer dos números y decir si son iguales o no


# Esta función sirve para comparar dos números y decir si son iguales o no

def comparar_numeros(numero1: float, numero2: float):
    if(numero1 == numero2):
        print("Si son iguales")
    else:
        print("No son iguales")


# La aplicación inicia aquí

a = float(input("Digite Número 1: "))
b = float(input("Digite Número 2: "))

comparar_numeros(a, b)
