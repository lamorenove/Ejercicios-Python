"""En una Universidad existen tres programas académicos, que son: Licenciatura Matemáticas, Tecnología en Electrónica y Tecnología de Sistemas, los cuales tienen un costo de inscripción de $120.000 para Tecnología Electrónica, $150.000 para Matemáticas y $110.000 para Tecnología de Sistemas, Se desea conocer el numero de inscritos en cada programa y el total recaudado por concepto de inscripción en cada programa.
Se debe procesar n cantidad de inscritos con la siguiente información:
1. Código del programa
2. Valor Inscripción

Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
1. cod_programa: “01 - Licenciatura Matemáticas” o “02 - Tecnología en Electrónica” o “03 - Tecnología de Sistemas”
2. valor_inscripcion: int

EJEMPLO diccionario
datos: list = [
    {
        "cod_progrma": "01",
        "valor_inscripcion": 120000
    },
    {
        "cod_progrma": "02",
        "valor_inscripcion": 150000
    },
{
        "cod_progrma": "03",
        "valor_inscripcion": 110000
    },

]


La respuesta debe retornar un diccionario con la siguiente información:

1. Total inscriptos por programa
2. Recaudo_total por programa"""


def consolidar_matriculas(datos: list) -> dict:
    # Tipo Matrículas
    matricula_lic_mat: str = "Matrícula Licenciatura Matemáticas"
    matricula_tec_elect: str = "Matrícula Tecnología Electrónica"
    matricula_tecn_sist: str = "Matrícula Tecnología Sistemas"

    # Inscritos por carrera
contmatematicas = 0
contelectronica = 0
contsistemas = 0

# Variable que guarda el total de matriculas
total_matriculas = 0
# total Matrículas Licenciatura Matemáticas
total_matr_lic_matematicas = 0
# total Matrículas Tecnología Electrónica
total_matr_tec_electronica = 0
# total Matrículas Tecnología Sistemas
total_matr_tec_sistemas = 0

# Iterar los datos a procesar
for item in datos:
        # Variable guarda el total de matriculas
        total_matriculas += item['total_matrícula']
        # obtiene total venta por tipo de venta
        if item['carrera'] == matricula_lic_mat:
            # Total matrículas licenciatura matemáticas
            total_matr_lic_matematicas += item['total_matrícula']
        elif item['carrera'] == matricula_tec_elect:
            # Total matrículas tecnología electrónica
            total_matr_tec_electronica += item['total_matrícula']
        elif item['carrera'] == matricula_tecn_sist:
            # Total matrículas tecnología sistemas
            total_matr_tec_sistemas += item['total_matrícula']
            # Diccionario guarda total de venta por tipo y contador por tipo de venta
    resultado: dict = {
        "total_matrículas": total_matriculas,
        "total_matrículas_Lic_Matemáticas": total_matr_lic_matematicas,
        "total_matrículas_Tec_Electrónica": total_matr_lic_matematicas,
        "total_matrículas_Lic_Matemáticas": total_matr_lic_matematicas,
    }
    return resultado


datos: list = [
    {
        "carrera": "Matrícula Licenciatura Matemáticas",
        "total_matrícula": 120000
    },
    {
        "carrera": "Matrícula Tecnología Electrónica",
        "total_matrícula": 150000
    },
    {
        "carrera": "Matrícula Tecnología Sistemas",
        "total_matrícula": 110000
    }
]
pass

print(consolidar_matriculas(datos))
