def inscripcionuniversidad(datos: list) -> dict:
    # Tipo programas académicos
    contmatematicas = 0
    contelectronica = 0
    contsistemas = 0
    # Variable que guarda el total recaudado por programa académico
    valormatematicas = 0
    valorelectronica = 0
    valorsistemas = 0

    # Iterar los datos a procesar
    for item in datos:
        if item['cod_programa'] == "01":
            contmatematicas += 1
            valormatematicas += item['valor_inscripcion']
        elif item['cod_programa'] == "02":
            contelectronica += 1
            valorelectronica += item['valor_inscripcion']
        elif item['cod_programa'] == "03":
            contsistemas += 1
            valorsistemas += item['valor_inscripcion']
    # Diccionario guarda cantidad de inscritos y total de recaudo por programa académico
    resultado: dict = {
        "licenciatura_matematicas": contmatematicas, "total_licenciatura_matematicas": valormatematicas,
        "tecnologia_electronica": contelectronica, "total_tecnologia_electronica": valorelectronica,
        "tecnologia_sistemas": contsistemas, "total_tecnologia_sistemas": valorsistemas,

    }
    return resultado


datos: list = [
    {"cod_programa": "01", "valor_inscripcion": 120000},
    {"cod_programa": "02", "valor_inscripcion": 150000},
    {"cod_programa": "03", "valor_inscripcion": 110000},
    {"cod_programa": "02", "valor_inscripcion": 110000},
    {"cod_programa": "02", "valor_inscripcion": 110000},
    {"cod_programa": "03", "valor_inscripcion": 110000},
    {"cod_programa": "02", "valor_inscripcion": 110000},
    {"cod_programa": "01", "valor_inscripcion": 120000},
    {"cod_programa": "03", "valor_inscripcion": 110000},
    {"cod_programa": "01", "valor_inscripcion": 120000},

]

print(inscripcionuniversidad(datos))
