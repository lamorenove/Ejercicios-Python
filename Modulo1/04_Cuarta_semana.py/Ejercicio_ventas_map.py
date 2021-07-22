'''1.	Una empresa recibe la información correspondiente a las ventas en pesos Colombianos 
de cada vendedor en el primer trimestre del año, 
se desea conocer el promedio de ventas en el trimestre por cada vendedor
 y el promedio general de ventas en el mismo periodo 

Vendedor	        Enero ($)	    Febrero ($)	    Marzo ($)
Pedro López 	    2000000	        1000000	        5000000
Martha Jaramillo	1500000	        10000000	    600000
Sandra Peña	        500000          800000          3000000
Hugo Marín          400000          200000          100000

Imprimir por pantalla la información de la siguiente manera:

Vendedor: Pedro López
Ventas Enero: $ 0000000
Ventas Febrero: $ 0000000
Ventas Marzo: $ 0000000
Promedio de ventas en el trimestre $ 0000000
============================================
Vendedor: Martha Jaramillo
Ventas Enero: $ 0000000
Ventas Febrero: $ 0000000
Ventas Marzo: $ 0000000
Promedio de ventas en el trimestre $ 0000000
============================================
'''
import locale
from statistics import mean


def promedio(a, b, c):
    return round(mean([a, b, c]), 1)


vendedores = ['Pedro López', 'Martha Jaramillo', 'Sandra Peña', 'Hugo Marín']

ventas_enero = [2000000, 1500000, 500000, 400000]
ventas_febrero = [1000000, 10000000, 800000, 200000]
ventas_marzo = [5000000, 600000, 3000000, 100000]
'''
Uso map para invocar la función promedio a cada elemento de las listas
'''
# Promedio de los dos periodos de cada asignatura
promedioVentasTrimestre = list(
    map(promedio, ventas_enero, ventas_febrero, ventas_marzo))

promedio_final = mean(promedioVentasTrimestre)
for x in range(0, len(vendedores)):
    print("\n vendedores: {}".format(vendedores[x]))
    print("\n{} {}".format('Enero:'.ljust(14), ventas_enero[x]))
    print("{} {}".format('Febrero:'.ljust(14), ventas_febrero[x]))
    print("{} {}".format('Marzo:'.ljust(14), ventas_marzo[x]))
    print("{} {}".format('Promedio Ventas Trimestre :'.ljust(
        14), promedioVentasTrimestre[x]))

print("\nPromedio Final : {}".format(promedioVentasTrimestre))
