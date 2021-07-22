"""
Un operario registra la producción de muebles de oficina que logra de lunes a sábado.  Elaborar un algoritmo que nos diga si el operario recibe incentivos o no, sabiendo que el promedio de producción mínima es de 20 unidades a la semana.  Tambien debe impirmir la producción semanal de muebles.
"""

print('\n')

Promedio_produccion = int(
    input("digite el número de muebles producidos de lunea a sábado: "))

if Promedio_produccion > 20:
    print("El operario recibe incentivos")
else:
    print("El operario no recibe incentivos")
print('\n')

print("La producción semanal de muebles es de: ", Promedio_produccion)
