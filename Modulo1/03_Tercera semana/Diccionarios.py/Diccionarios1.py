# Pasando información a través de diccionarios
'''
Los diccionarios ofrecen la posibilidad de empaquetar
o encapsular varias varibles para facilitar el envio de
parámetros.
'''
# Encapsulamiento con Diccionario
# Ejemplo2


def sumaVentas(dicVentas):
    sumatoria = 0
    sumatoria += dicVentas['venta1']
    sumatoria += dicVentas['venta2']
    sumatoria += dicVentas['venta3']
    suma = round(sumatoria, 2)
    return suma


# Creo el diccionario dicventas={}
dicventas = {
    "venta1": 100000,
    "venta2": 50000,
    "venta3": 200000
}
print("La suma de las ventas es:", sumaVentas(dicventas))
