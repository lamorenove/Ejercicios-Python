'''Un operario registra la producción de muebles de oficina que logra de lunes a sábado, 
elaborar un algoritmo que nos diga si el operario recibe incentivos o no, 
sabiendo que el promedio de producción mínima es de 20 unidades a la semana. 
También debe imprimir la producción semanal de muebles.
'''

print("\n")


def promedio_produccion(lunes, martes, miercoles, jueves, viernes, sabado):
    promedio = (lunes + martes + miercoles + jueves + viernes + sabado)/6
    return promedio


lunes = int(input("Digite la produccion del lunes: "))
martes = int(input("Digite la produccion del martes: "))
miercoles = int(input("Digite la produccion del miercoles: "))
jueves = int(input("Digite la produccion del jueves: "))
viernes = int(input("Digite la produccion del viernes: "))
sabado = int(input("Digite la produccion del sabado: "))
promedio = promedio_produccion(
    lunes, martes, miercoles, jueves, viernes, sabado)
print("\n")
if promedio >= 20:
    print("recibe incentivo")
else:
    print("No recibe incentivo")

print("\n")
print("El promedio de produccion del empleado es: %.2f" % promedio)
print("\n")
