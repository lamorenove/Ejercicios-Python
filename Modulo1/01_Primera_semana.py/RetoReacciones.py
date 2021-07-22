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
    MAX_SECONDS = 60

    segundos = MAX_SECONDS - duracion_segundos
    minutos = minuto_terminacion - duracion_minutos - 1
    horas = hora_terminacion - duracion_horas
    if segundos % 2 != 0:
        segundos = f'0{segundos}'
    if minutos % 2 != 0:
        minutos = f'0{minutos}'
    return f'La reacción {codigo} debe iniciarse a las {horas} horas, {minutos} con minutos con {segundos} segundos para que esté lista en el momento requerido'


# Pruebas
print(inicio_reaccion('HHA01', 16, 30, 4, 11, 23))
print(inicio_reaccion('ER723', 16, 30, 7, 24, 23))
