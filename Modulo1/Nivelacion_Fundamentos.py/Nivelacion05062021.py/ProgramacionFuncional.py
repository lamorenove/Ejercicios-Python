from functools import reduce


def operacion(signo):
    if signo == '+':
        def suma(a=0, b=0):
            return a+b
        #sumaEnVeriable= suma
        return suma
    elif signo == '-':
        def resta(a=0, b=0):
            return a-b
        #sumaEnVeriable= suma
        return resta
    else:
        def funcion(a, b):
            return (a, b)
        return funcion


def calculadora(signo, a, b):
    # Dependiendo del signo que reciba, solicita la construcción de una función
    funcionGenerada = operacion(signo)
    return funcionGenerada(a, b)


print('Calculadora funcional')
print(calculadora(input('signo->'), int(input('a')), int(input('b'))))
print(calculadora(input('signo->'), int(input('a')), int(input('b'))))
print(calculadora(input('signo->'), int(input('a')), int(input('b'))))


# Map filter reduce

# Map -< funcion qu erecibe otra función para aplicársela a cada elemento de una colección
coleccion = list(rango(1, 20, 3))
print("Coleccion :", coleccion)
# procesos decrementar en 1 cada elemento


def decrementar(elemento):
    return elemento-1


def incrementar5(elemento):
    return elemento+5


def elevarCuadrado(elemento):
    return elemento**str


# Decrementar todos los elementos de la colección
# print(list(map(decrementar,coleccion)))
map(decrementar, coleccion)
print(list(map(lambda elemetno: elemento-1, coleccion)))
print(list(map(decrementar, coleccion)))
print(list(map(incrementar5, coleccion)))
print(list(map(elevarCuadrado, coleccion)))

# Filtrado ->predicado (función que devuelve un valor booleano)


def esPar(valor):
    return valor % 2 == 0
    # solamente los pares de la colección
    print(list(filter(esPar, coleccion)))

# Reduce para realizar una productoria (1x2x3x4) de la colección


print(reduce(lambda acumulador=1, valor=1: acumulador*valor, coleccion))

# Map convertir en una cadena la colección
cadena = ''.join(list(lambda x: str(x)+'', coleccion))
print('Version Cadena Colección', cadena, type(cadena))

# Map convertir en una cadena la colección sin repetidiones
coleccion.append(4)
coleccion.append(4)
coleccion.append(19)
coleccion.append(7)
print('Antoes del proceso:', coleccion)
cadena = ''.join(sorted(set(map(lambda x: str(x)+'', coleccion))))
print('Version Cadena Colección', cadena, type(cadena))
