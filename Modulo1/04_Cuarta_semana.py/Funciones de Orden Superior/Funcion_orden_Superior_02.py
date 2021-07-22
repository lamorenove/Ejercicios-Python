# Funciones de orden superior

'''
Creamos la función crear_funcion.

Esta función tiene la capacidad
de crear nuevas funciones a
partir del valor del parámetro.
'''
# Envoltura de funciones


def crear_funcion(operador):
    if operador == '+':
        def suma(valor1=0, valor2=0):
            return valor1 + valor2
        return suma

# Función de orden superior suma


def operacion(funcion, valor1=0, valor2=0):
    return funcion(valor1, valor2)


funcion_suma = crear_funcion('+')
resultado = operacion(funcion_suma, 30, 10)

print(resultado)

# Función de orden superior resta


def crear_funcion(operador):
    if operador == '-':
        def resta(valor1=0, valor2=0):
            return valor1 - valor2
        return resta


def operacion(funcion, valor1=0, valor2=0):
    return funcion(valor1, valor2)


funcion_resta = crear_funcion('-')
resultado = operacion(funcion_resta, 30, 10)

print(resultado)

# Función de orden superior multiplicación


def crear_funcion(operador):
    if operador == '*':
        def multiplicacion(valor1=0, valor2=0):
            return valor1 * valor2
        return multiplicacion


def operacion(funcion, valor1=0, valor2=0):
    return funcion(valor1, valor2)


funcion_multimplicacion = crear_funcion('*')
resultado = operacion(funcion_multimplicacion, 30, 10)

print(resultado)

# Función de orden superior division


def crear_funcion(operador):
    if operador == '/':
        def division(valor1=0, valor2=0):
            return valor1 / valor2
        return division


def operacion(funcion, valor1=0, valor2=0):
    return funcion(valor1, valor2)


funcion_division = crear_funcion('/')
resultado = operacion(funcion_division, 30, 10)
print(resultado)
