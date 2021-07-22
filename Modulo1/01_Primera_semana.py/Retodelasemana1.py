'''
 Promedio de personas inscritas en la Academia de dibujo profesional Leonardo da Vinci al curso  de dibujo de lunes a viernes
 :Parámetros:

nro_inscritos:lunes(int),nro_inscritos_martes: (int), nro_inscritos_miercoles: (int), nro_inscritos_jueves: (int), nro_inscritos_viernes: (int)

 Retorno:

 String de la forma "El promedio de personas inscritas al curso de dibujo de lunes a viernes 
 
 es {promedioSuma}" pass

 '''

# Función que calcula el promedio del número de inscritos al curso de dibujo de lunes a viernes


def promedio_suma(inscritos_lunes: int, inscritos_martes: int, inscritos_miercoles: int, inscritos_jueves: int, inscritos_viernes: int) -> str:
    promedioSuma = (inscritos_lunes + inscritos_martes +
                    inscritos_miercoles + inscritos_jueves + inscritos_viernes)/5
    return "El promedio de personas inscritas al curso de dibujo de lunes a viernes es: %.0f" % promedioSuma

# Aquí inicia el programa y se definen las variables


nro_inscritos_lunes = int(
    input("Digite el número de inscritos del día lunes al curso de dibujo: "))
nro_inscritos_martes = int(
    input("Digite el número de inscritos del día martes al curso de dibujo: "))
nro_inscritos_miercoles = int(
    input("Digite el número de inscritos del día miercoles al curso de dibujo: "))
nro_inscritos_jueves = int(
    input("Digite el número de inscritos del día jueves al curso de dibujo: "))
nro_inscritos_viernes = int(
    input("Digite el número de inscritos del día viernes al curso de dibujo: "))

# Llamar la función que recibe las variables como parámetros

promedio = promedio_suma(nro_inscritos_lunes, nro_inscritos_martes,
                         nro_inscritos_miercoles, nro_inscritos_jueves, nro_inscritos_viernes)

print(promedio)
