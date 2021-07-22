'''
Crear un programa en Python que muestre en pantalla el  desempeño
académico de un alumno en dos asignaturas (Español y Matemática)
al finalizar el segundo periodo del año lectivo 2021. Se aprueba la 
asignatura si se obtiene una calificación mayor o igual a 3. Se
debe calcular e imprimir la calificación final de cada asignatura y el 
mensaje si aprobo o reprobo. Además el promedio general y el mensaje 
si va aprobando o reprobando el año escolar.

OBSERVACION: Se debe utilizar la función map, list y mean para resolver el problema
'''
'''
mean() La función se puede usar para calcular la media / promedio de una lista de 
números dada. Devuelve la media del conjunto de datos pasado como parámetros.
La media aritmética es la suma de datos dividida por el número de puntos de datos.

EL Módulo statistics biene con la función mean
'''




import locale
import locale
from statistics import mean
def promedio(a, b, c, d):
    return round(mean([a, b, c, d]), 1)


asignaturas = ['Español', 'Matemática',
               'Ciencias Naturales', 'Ciencias Sociales', 'Informática']

nota_minima = 3
notas_primer_periodo = [4, 3, 4, 3, 5]
notas_segundo_periodo = [2, 5, 3, 4, 3]
notas_tercer_periodo = [2, 5, 5, 2, 3]
notas_cuarto_periodo = [2, 5, 2, 1, 2]
'''
Uso map para invocar la función promedio a cada elemento
de las listas
'''
# Promedio de los 2 periodos en cada Asignatura
promedioNotasAsignatura = list(
    map(promedio, notas_primer_periodo, notas_segundo_periodo, notas_tercer_periodo, notas_cuarto_periodo))

# Promedio final
promedio_final = mean(promedioNotasAsignatura)

for x in range(0, len(asignaturas)):
    print("/nAsignatura:{}".format(asignaturas[x]))
    print("/n{} {}".format('Nota1 :' .ljust(14), notas_primer_periodo[x]))
    print("{} {}".format('Nota2 :' .ljust(14), notas_segundo_periodo[x]))
    print("{} {}".format('Nota3 :' .ljust(14), notas_tercer_periodo[x]))
    print("{} {}".format('Nota4 :' .ljust(14), notas_cuarto_periodo[x]))
    print("{} {}".format('Nota Final :' .ljust(
        14), promedioNotasAsignatura[x]))
    print("Estado: {}".format(
        'Aprueba la Asignatura' if promedioNotasAsignatura[x] >= nota_minima
        else 'Va reprobando la asignatura'))

    print("\n{}".format(' '.ljust(30, '=')))

print("\nPromedio Final : {}".format(promedio_final))
print("Estado Final: {}".format(
    "\x1b[1;32m"+'Aprobando' if promedio_final >= nota_minima else 'Reprobando'))
