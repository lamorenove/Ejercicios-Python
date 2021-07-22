# Leer 2 números diferentes e indicar cuál es mayor
#
def cual_es_mayor(a, b):
    if (a > b) :
       return a
    else:
       return b

     #La aplicación inicia aquí
a=int(input("Digite Número 1: "))
b=int(input("Digite Número 2: "))

respuesta = cual_es_mayor(a, b)

print("El numero mayor es: ", respuesta)
