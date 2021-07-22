# Reto 01 Fundamentos de programación
"""Luis carlos Pérez es un joven de 19 años que empezó a jugar cuando tenía tan solo 15 años. 
Hoy 4 años después está cumpliendo lo que para muchos no ha dejado de ser un sueño: ganarse la vida jugando videojuegos. 
Su talento y la pasión que siente por este deporte electónico lo ha llevado a convertirse en uno de
los gamers profesionales del país.

Últimamente Luis se ha preguntado por qué demora tanto en descargar sus arhcivos, por esto él
decide hacer un algoritmo en Python que le diga cuánto tiempo demora la descarga de su archivo 
teniendo en cuenta el peso del archivo, unidad del archivo y la velocidad de su internet.
Escriba una función que reciba como parámetros:  El peso del archivo a descargar, la velocidad del internet
y la unidad de tamaño del archivo donde la velocidad del internet está en Mbps y el tipo de tamaño del archivo 
se podrá escoger por un menú que otorgue las siguientes opciones (1:MB,2:GB,3:TB).
La cadena debe tener la siguiente estructura: "Tardaría {Tiempo} para descargar un archivo de {PesoArchivo} {TipoUT}".

Tenga en cuenta.

El tiempo se dará máximo en días y mínimo en segundos.
1 Mbps equivale a 0.125 MB por segundo.

Ejemplo:

PesoArchivo         VelocidadIn         TipoUT              Return

100                 1                   1                   Tardaría 13 minutos 20 segundos
                                                            para descargar un archivo
                                                            de 100 MB

1000009             10000               2                   Tardaría 9 días 6 horas 13 minutos
                                                            y 27 segundos para descargar
                                                            un archivo de 1000009 MB

100000              3545                3                   Tardaría 2680 días 17 horas
                                                            38 minutos 38 segundos para
                                                            descargar un archivo de 100000 MB.
"""

# R E T O  # 1  F U N D A M E N T O S  D E  P R O G R A M A C I O N


def Dar_tiempo(PesoArchivo: float, VelocidadIn: float, TipoUT: int) -> str:
    if TipoUT == 1:
        TipoUT = 'MB'
        Peso = PesoArchivo
    elif TipoUT == 2:
        TipoUT = 'GB'
        Peso = PesoArchivo*1000
    elif TipoUT == 3:
        TipoUt = 'TB'
        Peso = PesoArchivo*1000009

    tiempo = Peso/(0.125*VelocidadIn)

    dias = int(tiempo//86400)
    horas = int((tiempo-84600*dias)//3600)
    minutos = int((tiempo-(3600*horas+86400*dias))//60)
    segundos = int(tiempo-(86400*dias+3600*horas+60*minutos))
    cadena = 'Tardaría ' + str(dias) + 'dias' + ' ' + str(horas) + 'horas' + \
        ' ' + str(minutos) + 'minutos' + ' ' + str(segundos) + 'segundos' + ' ' + 'para descargar un archivo de ' + \
        str(PesoArchivo) + str(TipoUT)
    cadena1 = 'Tardaría ' + str(horas) + 'horas' + ' ' + \
        str(minutos) + 'minutos' + ' ' + str(segundos) + 'segundos' + ' ' + 'para descargar un archivo de ' + \
        str(PesoArchivo) + str(TipoUT)
    cadena2 = 'Tardaría ' + str(minutos) + 'minutos' + \
        ' ' + str(segundos) + 'segundos' + ' ' + 'para descargar un archivo de ' + \
        str(PesoArchivo) + str(TipoUT)
    cadena3 = 'Tardaría ' + ' ' + \
        str(segundos) + 'segundos' + ' ' + 'para descargar un archivo de ' + \
        str(PesoArchivo) + str(TipoUT)
    if dias == 0 & horas == 0:
        return cadena2
    elif dias == 0:
        return cadena1
    elif dias == 0 & horas == 0 & minutos == 0:
        return cadena3
    else:
        return cadena


print(Dar_tiempo(PesoArchivo=1000009, VelocidadIn=10000, TipoUT=2))
