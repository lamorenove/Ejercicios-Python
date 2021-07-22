'''
Una EPS desea conocer el numero personas atendidas en su programa de vacunación contra el COVID 19, la información debe ir discriminada de la siguiente manera: Número total de personas atendidas, número total de mujeres atendidas, número total de hombres atendidos, personas atendidas entre los rangos de edades de 40 a 49, 50 a 59, 60 a 69, 70 a 79 y mayores de 80.
La ciudad cuenta con 8 comunas, se desea conocer también el número de personas atendidas por comuna y las personas que en los últimos 3 meses tuvieron COVID 19.
Se debe procesar n cantidad de datos de personas con la siguiente información:
1. Edad
2. Sexo
3. Comuna
4. Covid_antes_SN
Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
1. Edad: int
2. Sexo: f/m
3. Comuna: Puede ser de la 01 a la 08
4. Covid_antes: puede ser afirmativo o negativo (s/n)
Ejemplo Datos
datos: list = [
    {
        "edad": 40
        "sexo": f
        "comuna": 04
        "covid_antes": n
    },
]
La respuesta debe retornar un diccionario con la siguiente información:
# total de personas atendidas
# total de mujeres atendidas
# total de hombres atendidos
# total de personas atendidas con edades entre los 40 y 49 años.
# total de personas atendidas con edades entre los 50 y 59 años.
# total de personas atendidas con edades entre los 60 y 69 años.
# total de personas atendidas con edades entre los 70 y 79 años.
# total de personas atendidas mayores de 80 años.
'''
import pprint


def EPS_COVID(datos: list) -> dict:
    Total_atendidos = 0
    Mujeres: str = "f"
    Hombres: str = "m"
    Total_mujeres = 0
    Total_hombres = 0
    Total_cuarenta_cuarentaynueve = 0
    Total_cincuenta_cincuentaynueve = 0
    Total_sesenta_sesentaynueve = 0
    Total_sententa_setentaynueve = 0
    Total_mayores_ochenta = 0

    for item in datos:
        Total_atendidos += 1
        if item['sexo'] == Mujeres:
            Total_mujeres += 1
        elif item['sexo'] == Hombres:
            Total_hombres += 1

        if item['edad'] >= 40 and item['edad'] < 50:
            Total_cuarenta_cuarentaynueve += 1
        elif item['edad'] >= 50 and item['edad'] < 60:
            Total_cincuenta_cincuentaynueve += 1
        elif item['edad'] >= 60 and item['edad'] < 70:
            Total_sesenta_sesentaynueve += 1
        elif item['edad'] >= 70 and item['edad'] < 80:
            Total_sententa_setentaynueve += 1
        elif item['edad'] >= 80:
            Total_mayores_ochenta += 1

    resultado: dict = {
        "Total_personas_atendidas": Total_atendidos,
        "Total_mujeres_atendidas": Total_mujeres,
        "Total_hombres_atendidos": Total_hombres,
        "Total-de_personas_atendidas_con_edades_entre_los_40_y_49_años": Total_cuarenta_cuarentaynueve,
        "Total-de_personas_atendidas_con_edades_entre_los_50_y_59_años": Total_cincuenta_cincuentaynueve,
        "Total-de_personas_atendidas_con_edades_entre_los_60_y_69_años": Total_sententa_setentaynueve,
        "Total-de_personas_atendidas_con_edades_entre_los_70_y_79_años": Total_sesenta_sesentaynueve,
        "Total-de_personas_atendidas_mayores_80": Total_mayores_ochenta
    }
    return resultado


datos: list = [
    {
        "sexo": "f",
        "edad": 40,
        "comuna": "04",
        "covid_antes": "n"
    },
    {
        "sexo": "f",
        "edad": 49,
        "comuna": "05",
        "covid_antes": "n"
    },
    {
        "sexo": "m",
        "edad": 51,
        "comuna": "06",
        "covid_antes": "s"
    },
    {
    },
    {
        "sexo": "f",
        "edad": 62,
        "comuna": "07",
        "covid_antes": "s"
    },
    {
        "sexo": "m",
        "edad": 80,
        "comuna": "04",
        "covid_antes": "n"
    },
    {
        "sexo": "m",
        "edad": 62,
        "comuna": "05",
        "covid_antes": "s"
    },
    {
        "sexo": "m",
        "edad": 72,
        "comuna": "06",
        "covid_antes": "n"
    }
]
pprint.pprint(EPS_COVID(datos))
