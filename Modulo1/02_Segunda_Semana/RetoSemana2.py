# Descripción del problema
"""
Una empresa decide incentivar a sus trabajadores respartiendo parte de
su utilidad lograda en el año 2020.  Para el cálculo de la bonificación
que deber recibir el empleado, se tiene en cuenta su antigüedad en la empresa
y un porcentaje de su salario de acuerdo con la siguiente tabla:

Tiempo                          Bonificación
Menos de 1 año                  5% del salario mensual
1 año o más y menos de 2 años   7% del salario mensual
2 año o más y menos de 5 años   10% del salario mensual
5 año o más y menos de 7 años   15% del salario mensual
Más de 7 años                   20% del salario mensual

Se requiere programar dos funciones, una función que reciba la información encapsulada del empleado en un diccionario
y otra que retorne a partir de un diccionario de respuesta el mensaje de la forma
"{NombreEmpleado}" - Bonificiación: Tiene una bonificación equiavalente al 7% de su salario mensual.",
la bonificación otorgada al empleado se determina de acuerdo al arbol de decisiones que muestra la figura 1.
"""

# El esqueleto de la primera función reportarBonificacion:


def reportarBonificacion(dicReporte: dict) -> dict:
    return dicReporte['empleado']+" - "+"Bonificación: "+str(dicReporte['bonificacion'])


def generarReporteBonificacion(dicEmpleado: dict) -> dict:
    if dicEmpleado['antiguedad'] < 1:
        boni = "Tiene una Bonificación equivalente al 5 por ciento de su salario mensual"
    else:
        if (dicEmpleado['antiguedad'] >= 1) and (dicEmpleado['antiguedad'] < 2):
            boni = "Tiene una Bonificación equivalente al 7 por ciento de su salario mensual"
        else:
            if (dicEmpleado['antiguedad'] >= 2) and (dicEmpleado['antiguedad'] < 5):
                boni = "Tiene una Bonificación equivalente al 10 por ciento de su salario mensual"
            else:
                if (dicEmpleado['antiguedad'] >= 5) and (dicEmpleado['antiguedad'] < 10):
                    boni = "Tiene una Bonificación equivalente al 15 por ciento de su salario mensual"
                else:
                    boni = "Tiene una Bonificación equivalente al 20 por ciento de su salario mensual"
    reporteBonificacion = {
        "bonificacion": boni,
        "empleado": dicEmpleado["empleado"]
    }
    return reporteBonificacion


dicEmpleado = {
    "id_empleado": "id_001",
    "empleado": "Sandra Peña",
    "antiguedad": 1,
}
print(reportarBonificacion(generarReporteBonificacion(dicEmpleado)))
