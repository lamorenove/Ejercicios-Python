def asignacion_becas(dicReporte: dict) -> dict:
    return dicReporte['estudiante']+" - "+"Tipo Beca: "+(dicReporte['tipo beca'])
# función para definir beca de estudio


def definir_beca(datos_estudiante: dict) -> dict:
    if(datos_estudiante['promedio'] >= 3.5) and (datos_estudiante['estrato'] <= 2):
        beca = "La beca incluye sostenimiento económico y el pago del 100 por ciento de los costos académicos"
    else:
        if(datos_estudiante['promedio'] == 3.5 and (datos_estudiante['estrato'] == 3)):
            beca = "La beca de estudio cubre el 40 por ciento de los costos académicos"
        else:
            if(datos_estudiante['promedio'] >= 4) and (datos_estudiante['estrato'] == 3):
                beca = "La beca de estudio cubre el 70 por ciento de los costos académicos"
            else:
                if(datos_estudiante['promedio'] >= 4) and (datos_estudiante['estrato'] == 4):
                    beca = "La beca de estudio cubre el 30 por ciento de los costos académicos"
                else:
                    beca = "No se otorga la beca"
    diccionario_respuesta = {
        'estudiante': datos_estudiante['estudiante'],
        'tipo beca': beca
    }
    return diccionario_respuesta


# prueba 1
datos_estudiante = {
    "id_estudiante": "t001",
    "estudiante": "Sonia Perez",
    "promedio": 3.5,
    "estrato": 2
}
print(asignacion_becas(definir_beca(datos_estudiante)))
