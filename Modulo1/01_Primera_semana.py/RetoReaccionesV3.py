"""Descripción: En un famoso laboratorio químico se realizan una serie de experimentos para los que se requiere analizar, en tiempo real, un conjunto de reacciones.  No obstante, la naturaleza volátild de algunas de estas hace que, una vez dadas, se cuente solamente con un corto intervalo de tiempo durante el cual es posible extraer información útil antes de que esta se disipe.  Debido a esto, es indispensable qué, idependientemente de cuando inicie cada una de las reacciones individuales, todas debe finalizar al mismo tiempo.  Afortunadamente, el laboratorio conoce una aproximación muy precisa de la duración de cada una de sus reacciones.Considerando el contexto anterior, el laboratorio le ha solicitado que diseñe una solución informática que les facilite ralizar la programación de sus experimentos.  Para esto:
Escriba una función que reciba como parámetros: el código alfanumérico que identifica la reacción, así como la hora y minuto en la que esta debe finalizar, además de la duración esperada de la misma (en minutos, horas y segundos) y retorne un mensaje, indicándole a los técnicos en qué momento deben iniciar la reacción para que esté lista exactamente cuando es requerida.
Note que:  El laboratorio cierra a la media noche (23:59) y todos los experimentos se realizan antes del cierre, a partir de reacciones que iniciaron el mismo día operacional.
Las especificaciones técnicas del requerimiento se enuncian a continuación:

Entradas:
Nombre              Tipo Descripción
codigo              str  Código alfanumérico que identifica la reacción.
hora_terminación    int  Hora requerida para la finalización de la reacción.
minuto_terminación  int  Minuto requerido para la finalización de la reacción.
duración_horas      int  Estimación de  las horas que dura la reacción.
duración_minutos    int  Estimación de  los minutos que dura la reacción.
duración_segundos   int  Estimación de  las segundos que dura la reacción.

Salida:
Tipo del retorno    Descripción
str                 Texto con la siguiente estructura: "La reacción {codigo} debe iniciarse a las {hh} horas, {mm} minutos con {ss} segundos para que esteé lista en el momento requerido"
"""

# Esqueleto


def inicio_reaccion(codigo: str, hora_terminacion: int, minuto_terminacion: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int) -> str:
    MAX = 60

    segundos = duracion_segundos - MAX
    if segundos < 0:
        segundos = abs(segundos)

    if segundos + duracion_segundos > MAX:
        segundos -= 1

    minutos = duracion_minutos - minuto_terminacion
    horas = duracion_horas - hora_terminacion

    if minutos > 0 and minutos <= MAX:
        minutos = MAX - minutos
    else:
        minutos = abs(minutos) - 1

    if minutos + duracion_minutos > MAX:
        horas += 1
        if minutos % 2 == 0 and duracion_minutos % 2 == 0:
            minutos -= 1

    if horas < 0:
        horas = abs(horas)

    if minutos % 10 == 0:
        pass
    else:
        minutos = f'0{minutos:02}'
    if segundos % 10 == 0:
        pass
    else:
        segundos = f'0{segundos:02}'

    return f'La reacción {codigo} debe iniciarse a las {horas} horas, {minutos} minutos con {segundos} segundos para que esté lista en el momento requerido'


# Pruebas
print(inicio_reaccion('HHA01', 16, 30, 4, 11, 23))
print(inicio_reaccion('ER723', 16, 30, 7, 24, 23))
print(inicio_reaccion('ER723', 16, 30, 8, 45, 15))
