'''
FUNCIONES PARA COLECCIONES DE DATOS
Python Ofrece unas funciones , muy versatiles para trabajar con grandes 
colecciones de datos, estas son funciones de orden superior.

Las funciones más utilizadas de este tipo, para realizar operaciones sobre
listas principalmente, sin utilizar ciclos, al estilo del paradigma funcional,
son las siguientes:

* Map
* Reduce
* Filter
* Zip
--------------------------------------------------------------------------
Algo interesante de las funciones en Python es que estas pueden ser
asignadas a variables.

Las funciones pueden ser utilizadas como argumento de otras funciones

Las funciones pueden retornar otras funciones.
---------------------------------------------------------------------------
'''

# Funciones de orden superior


def suma(val1, val2):
    return(val1+val2)

# Esta es la función de orden superior


def operacion(funcion, val1, val2):
    print(funcion(val1, val2))

# Variable suma


def suma(val1, val2):
    return (val1+val2)


variable_suma = suma

resultado = operacion(variable_suma, 10, 5)
print(resultado)

# Variable resta


def resta(val1, val2):
    return (val1-val2)


variable_resta = resta

resultado = operacion(variable_resta, 10, 5)
print(resultado)

# Variable multiplicación


def multiplicacion(val1, val2):
    return (val1*val2)


variable_multiplicacion = multiplicacion

resultado = operacion(variable_multiplicacion, 10, 5)
print(resultado)


# Variable división

def division(val1, val2):
    return (val1/val2)


variable_division = division

resultado = operacion(variable_division, 10, 5)
print(resultado)
