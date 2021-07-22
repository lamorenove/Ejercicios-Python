# Problema #1
"""
Utilizar la función incorporada map() para crear una función 
que retorne una lista con la
longitud de cadad palabra(separadas por espacios) de una frase.  
La función recibe una cadena de texto y retornará una lista.
"""
numero = ["l", " ", "o", " ", "v", " ", "e"]


def cadena(numero):
    return "love"


resultado = list(map(cadena, numero))  # mpa transforma o iterar cada número
print(resultado)

cadena = ["Colombia empató el partido"]
separador = " - "
separado_por_espacios = cadena.split(separador, maximo_numero_de_separaciones)
print("Separado por espacios es:", separado_por_espacios)
