'''Se necesita obtener el promedio de tres notas parciales de la asignatura de Inglés.  Muestre por pantalla el promedio de dichas calificaciones.

Entradas: nota1, nota2, nota3
Proceso: Promedio = (nota1 + nota2 + nota3)/3
Salida: Promedio.

Algoritmo

Inicio

 Leer Nota1
 Leer Nota2
 Leer Nota3

 Promedio = (Nota1 + Nota2 + Nota3)/3
 Escribir promedio

Fin
'''

def calcular_promedio_notas(Nota1,Nota2,Nota3):
    promedio = (Nota1 + Nota2 + Nota3)/3
    return promedio

print ('\n')

Nota1 = float(input("Digite la primera nota: "))
Nota2 = float(input("Digite la segunda nota: "))
Nota3 = float(input("Digite la tercera nota: "))

promedio = calcular_promedio_notas(Nota1,Nota2,Nota3)
print("El promedio de la nota de inglés es: %.2f" % promedio)
print ('\n')