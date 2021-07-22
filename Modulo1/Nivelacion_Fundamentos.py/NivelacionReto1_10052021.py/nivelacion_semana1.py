# primer programa nivelación semana 1
#
# variagles y tipos de datos


primer_nombre = "Francisco"  # string - cadena de caracteres
segundo_nombre = "Carlos"
primer_apellido = "Tórres"
edad = 25  # integer -int  es un entero
# siempre que se usen comillas le estamos indicando a Python una cadena de caracteres

documento = "100022152"
nota1 = 3.5
nota2 = 4.5
nota3 = 4.8
nota4 = 3.5

#nota1 = (input("Ingrese la primera nota: "))
#nota2 = (input("Ingrese la segunta nota: "))
#nota3 = (input("Ingrese la tercera nota: "))
#nota4 = (input("Ingrese la cuarta nota: "))


# operadores aritméticos


# + sumar
resultado = 10 + 3
print(resultado)

# - restar
resultado = 10 - 3
print(resultado)

# * multiplicar
resultado = 10 * 3
print(resultado)

# / dividir
resultado = 10/3
print(resultado)

# // división entera

resultado = 10//3
print(resultado)
#  % modulo devuelve el residuo de la división

resultado = 10 % 3
print(resultado)
# ** elevar a una potencia

resultado = 10 ** 3
print(resultado)

# ojo con la jerarquía de los operadores * / + r PEMDAS -- parentesis , exponentes, multiplicación, división, adición, sustracción.
resultado = (3 + 4 + 3 + 5) / 4
print(resultado, '\n')


# print promedio
promedio = (round(float(nota1) + float(nota2) +
            float(nota3) + float(nota4)) / 4, 2)

print(promedio, '\n')
print(type(documento), '\n')
print(primer_nombre, '\n')
print(type(primer_nombre), '\n')
print(type(edad), '\n')
print(nota1, nota2, nota3, nota4, '\n')
nombre_completo = primer_nombre + " " + segundo_nombre + " " + primer_apellido
print(nombre_completo, '\n')
print("edad del estudiante = ", edad, "hola", '\n')
print("documento del estudiante" + documento, '\n')


# condicionales
"""
if condicion:
    print("este código se ejecuta si es verdadera")
else:
    print("este código se ejecuta si es falsa")
"""

# operadores relacionales
if nota1 != 4:
    print("imprimir algo", '\n')

if nota1 == 3:
    print("imprimir algo", '\n')

# operadores
# != diferente
# == igual igual
# > mayor que
# < menor que
# >= mayor o igual

if nota1 >= 3:
    print("imprimir algo", '\n')

# <= menor o igual
# and y
# or o
# & y
# if = si
# else = entonces
# elif = suma si y entonces

# así funcionan las condicionales

if nota1 == 3.1:
    print("imprimir algo", '\n')
elif nota2 == 4:
    print("soy 4", '\n')
elif 3 < nota2 and 5 > nota2:
    print("si", '\n')
else:
    print("no era igual", '\n')
