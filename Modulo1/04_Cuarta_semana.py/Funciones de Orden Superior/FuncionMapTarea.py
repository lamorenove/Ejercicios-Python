"""problema # 1
Utilizar la funcion incorporada map() para crear una función que retorne una lista con la longitud de cada palabra (separadas por espacios)
de una frase. La función recibe una cadena de texto y retornará una lista"""
equipos = ["América", "Millonarios", "Tolima",
           "Cali", "Junior", "Antartida", "Anglos"]


def nombre_letra(l):
    return 'A' == l[0]


filtro_nombres = filter(nombre_letra, equipos)
print(list(filtro_nombres))
# ESTA FUNCION ME FILTRA LOS NOMBRES DE LOS EQUIPOS QUE EMPIEZAN CON la letra -A-

equipos = ["América", "Millonarios", "Tolima", "Cali", "Junior"]
# Esta funcion enumera los equipos de la lista
for pos, equipo in enumerate(equipos, 1):
    print(pos, equipo)
