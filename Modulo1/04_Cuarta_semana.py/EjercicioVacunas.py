"""La Secretaría de Salud municipal desea conocer el número de adultos vacunad@s de acuerdo al siguiente esquema:
 
 
Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
1.	Cod_tipo_vacuna: str
2.	edad: int
3.	sexo: str         (f/m)
4.	gestante str   (s/n)
5.	viajero: str     (s/n)
Ejemplo Datos
datos: list = [
    {
        "cod_tipo_vacuna": 01
        "edad": 4
        "sexo": f
        "gestante": s
        "viajero ": s
 
    },
    
    {
        "cod_tipo_vacuna": 02
        "edad": 4
        "sexo": f
        "gestante": s
        "viajero ": s
    },
]


La respuesta debe retornar un diccionario con la siguiente información:
# Vacunas aplicadas contra el VPH
# Vacunas aplicadas contra el Td -Toxoide Diftérico
# Vacunas aplicadas contra el DPTa – Difteria, Tétanos, Tosferina Aceluar.
# Vacunas aplicadas contra la Fiebre Amarilla.
# Vacunas aplicadas contra la Influenza Estacional.
# Vacunas aplicadas contra Neumo 23 Adultos.
# Vacunas aplicadas a mujeres Gestantes
# de viajeros vacunad@s"""


import pprint
Vacunas_VPH = '01'
Vacunas_Td = '02'
Vacunas_DTPa = '03'
Vacunas_FiebreAmarilla = '04'
Vacunas_Influenza = '05'
Vacunas_Neumo23 = '06'


def VAC_APLIC(datos: list) -> dict:
    Total_vacunas_VPH = 0
    Total_vacunas_Td = 0
    Total_vacunas_DTPa = 0
    Total_vacunas_FiebreAmarilla = 0
    Total_vacunas_Influenza = 0
    Total_vacunas_Neumo23 = 0
    Total_vacunas_MujeresGestantes = 0
    Total_viajeros_vacunados = 0
    Total_vacunados = 0
    Mujeres: str = "f"
    Hombres: str = "m"
    Total_mujeres = 0
    Total_hombres = 0
    Total_nueve_veinte = 0
    Total_diez_cuarentaynueve = 0
    Total_hasta_cincuentaynueve = 0
    Total_mayores_sesenta = 0

    for item in datos:
        Total_vacunados += 1
        if item['sexo'] == Mujeres:
            Total_mujeres += 1
        elif item['sexo'] == Hombres:
            Total_hombres += 1

        if item['edad'] >= 9 and item['edad'] <= 20 and item['sexo'] == 'f':
            Total_vacunas_VPH += 1
        if item['edad'] >= 10 and item['edad'] <= 49 and item['sexo'] == 'f':
            Total_vacunas_Td += 1
        if item['gestante'] == 's':
            Total_vacunas_MujeresGestantes += 1
            Total_vacunas_DTPa += 1
            Total_vacunas_Influenza += 1
        if item['viajero'] == 's':
            Total_vacunas_FiebreAmarilla += 1
        elif item['edad'] >= 60:
            Total_vacunas_Influenza += 1
            Total_vacunas_Neumo23 += 1

    resultado: dict = {
        "Total_vacunas_aplicadas_contra_el_VPH": Total_vacunas_VPH,
        "Total_vacunas_aplicadas_contra_el_Td": Total_vacunas_Td,
        "Total_vacunas_aplicadas_contra_el_DTPa": Total_vacunas_DTPa,
        "Total_vacunas_aplicadas_contra_la_Fiebre_Amarilla": Total_vacunas_FiebreAmarilla,
        "Total_vacunas_aplicadas_contra_la_Influenza_Estacional": Total_vacunas_Influenza,
        "Total_vacunas_aplicadas_contra_la_Neumo": Total_vacunas_Neumo23,
        "Total_vacunas_aplicadas_mujeres_gestantes": Total_vacunas_MujeresGestantes,
        "Total_vacunas_aplicadas_viajeros_vacunados": Total_viajeros_vacunados,
    }
    return resultado


datos: list = [
    {
        "cod_tipo_vacuna": '01',
        "edad": 4,
        "sexo": "f",
        "gestante": 's',
        "viajero": 'n'
    },
    {
        "cod_tipo_vacuna": '02',
        "edad": 60,
        "sexo": "m",
        "gestante": 'n',
        "viajero": 'n'
    },
    {
        "cod_tipo_vacuna": '03',
        "edad": 35,
        "sexo": "f",
        "gestante": 's',
        "viajero": 'n'
    },
    {
        "cod_tipo_vacuna": '02',
        "edad": 45,
        "sexo": "f",
        "gestante": 'n',
        "viajero": 'n'
    },
    {
        "cod_tipo_vacuna": '04',
        "edad": 15,
        "sexo": "m",
        "gestante": 'n',
        "viajero": 's'
    },
    {
        "cod_tipo_vacuna": '05',
        "edad": 80,
        "sexo": "m",
        "gestante": 'n',
        "viajero": 's'
    }
]
pprint.pprint(VAC_APLIC(datos))
