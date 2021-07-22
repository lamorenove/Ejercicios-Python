"""
Un operario registra la producción de muebles de oficina que logra de lunes a sábado.  Elaborar un algoritmo que nos diga si el operario recibe incentivos o no, sabiendo que el promedio de producción mínima es de 20 unidades a la semana.  Tambien debe impirmir la producción semanal de muebles.
"""

print('\n')


def promedio_produccion(lunes, martes, miercoles, jueves, viernse, sabado):
    promedio = (lunes + martes + miercoles + jueves + viernse + sabado)/6
    return promedio


lunes = int(input("Digite el número de muebles producidos el lunes: "))
martes = int(input("Digite el número de muebles producidos el martes: "))
miercoles = int(input("Digite el número de muebles producidos el miércoles: "))
jueves = int(input("Digite el número de muebles producidos el jueves: "))
viernes = int(input("Digite el número de muebles producidos el viernes: "))
sabado = int(input("Digite el número de muebles producidos el sabado: "))

promedio = promedio_produccion(
    lunes, martes, miercoles, jueves, viernes, sabado)
print('\n')

if promedio > 20:
    print("El operario recibe incentivos")
else:
    print("El operario no recibe incentivos")

print('\n')
print("La producción promedio semanal de muebles es de:%.2f ", promedio)
print('\n')
