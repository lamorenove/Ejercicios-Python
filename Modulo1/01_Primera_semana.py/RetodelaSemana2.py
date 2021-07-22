"""Usted trabaja en una entidad financiera que cuenta con la siguiente información en base a la que ralizan evaluación de nuevas solicitudes de crédito:

Nombre           Abreviación  Tipo       Descripción
Id_prestamo       N/A          str        código único alfanumérico que identifica el prestamo
casado            N/A          str        aplicante es casado (si/no)
dependientes      N/A          str/int    cantidad de personas dependientets del aplicante (0/1/2/'3+')
educacion         N/A          str        nivel de educación de la persona (Graduado / No Graduado)
independiete      N/A          str        aplicante es independiente (si/no)
ingreso_deudor    i_d          float      ingreso del aplicante
ingreso_codeudor  i_c          float      ingreso del codeudor
cantidad_prestamo c_p          float      Cantidad de crédito solicitada
plazo_prestamo    p_p          int        Plazo del crédito
historia_credito  n/A          int        Aplicante cuenta con historia creditica favorable (1/0)
tipo_propiedad    N/A          str        Urbana /  Rural / Semi Urbana

Recientemente, su empleador adquirió un modelo basado en árboles de decisión par apoder resalizar más fácilmente una primera revisión de estas solicitudes.    Este se muestra a continuación:
"""

informacion = {
    'Id_prestamo': 'RETOS2_001',
    'casado': 'No',
    'dependientes': 1,
    'educacion': 'Graduado',
    'Independiente': 'Si',
    'i_d': 4692,
    'i_c': 0,
    'c_p': 106,
    'p_p': 360,
    'historia_credito': 1,
    'tipo_propiedad': 'rural'
}


def prestamo(informacion: dict) -> dict:
    if informacion['historia_credito'] == 1:
        elif(informacion['i_c'] > 0) ^ (informacion['i_d'] / 9 > informacion['c_p']) ^ (informacion['dependientes'] > 2) ^ (informacion['independientes'] == 'si'):
            (informacion['i_c'] / 12) > informacion['c_p']
            informacion['c_p'] < 200


if informacion['historia_credito'] == 0:
    elif(informacion['independiente'] == 'si') ^ (informacion['casado'] == 'si') ^ (informacion['dependientes'] > 1):
        else:
            (informacion['i_c'] / 12) > informacion['c_p']
        informacion['c_p'] < 200
