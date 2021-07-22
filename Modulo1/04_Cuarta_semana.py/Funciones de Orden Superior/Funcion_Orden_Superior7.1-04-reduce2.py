# Concatenar todos los elementos de la lista

from functools import reduce

# función reduce es necesario importarla para poder usarla

lista = ['Python', 'Java', 'Ruby', 'Elixir']

resultado = reduce(lambda acumulado='',
                   elemento='': acumulador + " - " + elemento, lista)

print(resultado)
