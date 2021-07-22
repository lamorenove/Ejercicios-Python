"""
La función map nos permite aplicar una 
función sobre cada uno de los elementos de 
una colección(listas,tuplas,etc,...).
Haremos uso de esta función siempre que 
tengamos la necesidad de transformar el 
valor de cada elemento en otro.
"""


def doblar(numero):
    return numero*2


numeros = [2, 5, 10, 23, 50, 33]

resultado = list(map(doblar, numeros))
print(resultado)
