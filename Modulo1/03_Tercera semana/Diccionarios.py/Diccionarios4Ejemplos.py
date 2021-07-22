'''
Un Diccionario en Python es un conjuntos no ordenado de
pares clave:valor.
Los Diccionarios se encuentran en otros lenguajes como
arreglos asociativo.
El Diccionario en Python es una estructura de datos, tipo de dato 
que nos permite almacenar valores, como enteros, cadenas y funciones,
entreo otros.
Los Diccionarios son contenedores, donde cada elemento
(item) que contiene representa la estructura llave:valor
Cada elemento del diccionario lo identificamos con una clave (key).
Los Diccionarios se indexan con claves, cadenas y numeros
pueden ser claves.
Con un par de llaves se crea un diccionario.
Una lista de pares clave:valor se añade al diccionario
separados por coma (,) entre las llaves
'''
movil = {"Jorge": 3120005412, "Martha": 3001234587}
print(movil)
# Añadir una clave y su valor al diccionario
movil['Pedro'] = 3136214512
print(movil)
# La sentencia (del) en el diccionario elimina una clave y su valor
movil = dict(Jorge=3120005412, Martha=3001234587)
print(movil)
del movil["Jorge"]
print(movil)
'''
El método sirve para extraer información del diccionario, recibe como parametro una representación de un diccionario y devulve un diccionario
'''
# Ejemplo 1
factura = dict(Nrofactura=8954, valor=150000, iva=True)
print(factura)
print(factura['valor'])
print(factura['iva'])
'''
Podemos obtener todas las llaves de nuestro diccionario utilizando el método keys{}
'''
# Ejemplo2
empleados = {'Sandra': 1, 'Teresa': 2, 'Juan': 2}
print(empleados.keys())
# Método items() devuelve una lista de clave:valor del diccionario
empleados = {'Sandra': 1, 'Teresa': 2, 'Juan': 2}
print(empleados.items())
# La funcion len() cuenta el número de llaves del diccionario
empleados = {'Sandra': 1, 'Teresa': 2, 'Juan': 2}
print(len(empleados))
