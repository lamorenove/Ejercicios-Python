"""Rango:
[0-3) rendimiento bajo
(3-4] rendimiento medio
[4-5] rendimiento alto
"""

rendimiento = (bajo or medio or bajo)


def notas(nota1, nota2, nota3):  # comentario
    promedio = round((nota1 + nota2 + nota3)/3, 2)
    maximo = max(nota1, nota2, nota3)
    minimo = min(nota1, nota2, nota3)
    if promedio >= 0 and promedio < 3:
        rendimiento = "bajo"
    else:
        if promedio >= 3 and promedio < 4:
        rendimiento = "medio"
        else:
            if promedio >= 4 and promedio < 5:
            rendimiento = "alto"

    return f'El estudiante tiene una nota promedio de {promedio}, su mayor nota fue {maximo} y su menor nota fue {minimo} y su rendimiento fue {rendimiento}'


print(notas(3.5, 4, 4.6))
print(notas(4, 5, 5))
print(3, 2, 1)

print("Ingresa tu apellido")
apellido = input()

var1 = 0
var2 = 0.0
print(type(var1), type(var2))
