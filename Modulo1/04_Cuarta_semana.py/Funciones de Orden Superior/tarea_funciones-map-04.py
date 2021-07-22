'''
1.	Crear una función que determine el equipo de futbol, cuyo nombre 

inicie con la letra “T”, utilizar la función map para iterar en la lista equipos.

equipos = ["América", "Millonarios", "Tolima", "Cali", "Junior"]

	Generar una lista de resultado que indique con true los nombres que inicien con 
    la letra “T” y false para los que no cumplan la condición. 
    La lista generada es la siguiente:

[False, False, True, False, False]

'''
equipos = ["América", "Millonarios", "Tolima", "Cali", "Junior"]


def Equipo_letra(letra):
    if 'T' == letra[0]:  # significa que la letra cuyo índice es 0 es T
        return True
    else:
        return False


resultado = list(map(Equipo_letra, equipos))

print(resultado)


equipos = ["América", "Millonarios", "Tolima",
           "Cali", "Junior", "Antártida", "Anglos"]


def nombre_letra(l):
    return 'A' == l[0]


filtro_nombres = filter(nombre_letra, equipos)
print(list(filtro_nombres))

# Esta función me filtra los nombres de los equipos que empiezan con la letra A.

equipos = ["América", "Millonarios", "Tolima", "Cali", "Junior"]
# esta función enumera los equipos de la lista.
for por, equipo in enumerate(equipos, 1):
    print(equipos, equipo)
