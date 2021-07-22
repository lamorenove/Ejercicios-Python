"""
Calcular la utilidad que un trabajador recibe en el
reparto anual de utilidades si este se le asigna como
un porcentaje de su salario mensual que depende de su
antigüedad en la empresa de acuerdo con la siguiente
Tabla:
------------------------------------------------------------
Tiempo                                    Utilidad
------------------------------------------------------------
Menos de 1 año                         5% del salario
1 año o más y menos de 2 años           7% del salario
2 años o más y menos de 5 años         10% del salario
5 años o más y menos de 10 años       15% del salario
10 años o más                         20% del salario
-----------------------------------------------------------

ALGORITMO
Inicio
 sm, antig: Entero
 LEER sm, antig
 Si antig < 1  entonces
             util = sm * 0.05
     Si No
           Si(antg >= 1) and (antig < 2) entonces
                         util = sm * 0.07
                    Si no
                           Si(antig >= 2) and (antig < 5) entonces
                                       util = sm * 0.10
                                 Si no
                                   Si(antig >= 5) and (antig < 10) entonces
                                                         util = sm * 0.15
                                                Si no
                                                         util = sm * 0.20
                                     Fin Si
                           Fin Si
               Fin Si
     Fin Si
     imprimir “La utilidad es: ”, util
Fin
"""


def utilidad(dicUtilidad: dict) -> dict:
    return dicUtilidad['trabajador']+" - "+"reparto utilidad: "+(dicUtilidad['reparto utilidad'])
# función para definir el reparto de utilidad


def definir_utilidad(datos_trabajador: dict) -> dict:
    if(datos_trabajador['antiguedad'] < 1):
        utilidad = "El reparto de utilidad es del 5 por ciento del salario"
    else:
        if(datos_trabajador['antiguedad'] >= 1 and (datos_trabajador['antiguedad'] < 2)):
            utilidad = "El reparto de utilidad es del 7 por ciento del salario"
        else:
            if(datos_trabajador['antiguedad'] >= 2) and (datos_trabajador['antiguedad'] < 5):
                utilidad = "El reparto de utilidad es del 10 por ciento del salario"
            else:
                if(datos_trabajador['antiguedad'] >= 5) and (datos_trabajador['antiguedad'] < 10):
                    utilidad = "El reparto de utilidad es del 15 por ciento del salario"
                else:
                    utilidad = "El reparto de utilidad es del 20 por ciento del salario"
    diccionario_respuesta = {
        'trabajador': datos_trabajador['trabajador'],
        'reparto utilidad': utilidad
    }
    return diccionario_respuesta


# prueba 1
datos_trabajador = {
    "ID_trabajador": "001",
    "trabajador": "Jhon Perez",
    "antiguedad": 5,
    "salario": 1000000
}
print(utilidad(definir_utilidad(datos_trabajador)))
