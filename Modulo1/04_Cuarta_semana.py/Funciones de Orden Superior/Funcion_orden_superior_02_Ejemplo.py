def crear_funcion(operador):
    if operador == "-":
        def resta(valor1=0, valor2=0):
            return valor1 - valor2
        return resta
    elif operador == "*":
        def multiplicacion(valor1=0, valor2=0):
            return valor1 * valor2
        return multiplicacion
    elif operador == "/":
        def division(valor1=0, valor2=0):
            return valor1 / valor2
        return division


funcion_resta = crear_funcion("-")
resultado = operacion(funcion_resta, 30, 10)
funcion_multiplicacion = crear_funcion("*")
resultado = operacion(funcion_multiplicacion, 30, 10)
funcion_division = crear_funcion("/")
resultado = operacion(funcion_division, 30, 10)

print(resultado)
