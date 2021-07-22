'''
TUPLAS
* Una tupla es una secuencia de valores muy parecida a una lista
* Los valores almacenados en una tupla pueden ser de cualquier 
  tipo, y están indexados por números enteros.
* La diferencia importante es que las tuplas son inmutables.
* Una Tupla es una lista de valores separada por por comas
'''
t = 'a', 'b', 'c,', 'd', 'e'
print(t)  # Imprimir tupla
t = '1', '2', '3,', '4', '5'
print(t)  # Imprimir tupla
t = '3', 'a', '8,', '7', '2', 'Hola'
print(t)  # Imprimir tupla
t = 'esto es una cadena', 'b', 'c', 'd,', '7', '2', 'Hola'
print(t)  # Imprimir tupla
"""
Si el argumento es una secuencia (cadena, lista o tupla) 
el resultado de la llamada a la tupla es una tupla con los 
elementos de la secuencia.
"""
t = tuple("lupines")
print(t)  # Resultado: ('l', 'u', 'p', 'i', 'n', 'e', 's'),
