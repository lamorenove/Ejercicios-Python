'''
CONDicional doble

Estructura Algorítmica de la condicional doble

Si <condición> entonces
             Acción(es)
            sino
                Accion(es)
Fin - Si

Determinar si un alumino aprueba o reprueba una
asignatura, aprueba si el promedio de 
tres calififcaciones es mayor o igual a 3,
en caso contrario reprueba.
'''

calificacion1 = float(input("Digite Calificación 1: "))
calificacion2 = float(input("Digite Calificación 2: "))
calificacion3 = float(input("Digite Calificación 3: "))

promedio = (calificacion1+calificacion2+calificacion3)/3

if promedio >= 3:
    print("El alumno aprobó")
else:
    print("El alumno reprobó")
