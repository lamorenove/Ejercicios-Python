# Ordenar palabras de más a menos
txt = "but soft what light in yonder window breaks"
palabras = txt.split()
print(palabras)


l = list()
'''
El bucle construye una lista de tuplas, donde cada tupla es una 
palabra precedida por su longitud.
'''
for subcadena in palabras:
    l.append((len(subcadena), subcadena))
print(l)
'''
La función sort compara el primer elemento, la longitud, primero, y 
sólo considera el segundo elemento para romper los empates. 
El argumento de la palabra clave reverse=True le dice a sort que 
vaya en orden decreciente.
'''
l.sort(reverse=True)
print(l)

# Asignación de tupla
m = ['Mango', 'Piña']
x, y = m
print(x)
print(y)

# Acceder a los valores de la Tupla
m = ['Carro', 'Moto']
x = m[0]
y = m[1]
print(x)
print(y)

# Se puede hacer esto tambien
m = ['Televisor', 'Avión']
(x, y) = m
print(x)
print(y)


# El valor de retorno de la división es una lista con dos elementos
addr = 'hugo@python.org'
usuario, dominio = addr.split('@')
print(usuario)
print(dominio)

'''
Diccionarios y tupla
Los diccionarios tienen un método llamado elementos que devuelve 
una lista de tuplas, en la que cada tupla es un par clave-valor:
'''
diccionario = {'c': 10, 'a': 1, 'b': 22}
tupla = list(diccionario.items())
print(tupla)

# La nueva lista está ordenada en orden alfabético ascendente por el valor clave.
tupla.sort()
print(tupla)
