'''
problema #2
Crear una función que tome una lista de digitos y devuelva al número que corresponden. Por ejemplo [1,2,3] corresponde al número (123).
Utilizar la función reduce
'''
from functools import reduce
lista = ["1", "2", "3", "50", "60", "70"]


def funcion_concaten(concaten=0, elemento=0):
    return concaten + elemento


resultado = reduce(lambda acumulador="",
                   elemento="": acumulador + "-" + elemento, lista)

print(resultado)
