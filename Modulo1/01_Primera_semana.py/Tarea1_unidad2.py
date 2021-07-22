"""
Elaborar un algoritmo que permita averiguar si una persona debe sacar céduda de ciudadanía.  Si la persona es mayor de  17 años, debe imprimir #debe sacar cédula de ciudadanía", en caso conrario, impirmir "No debe solicita cédula" """

print('\n')

edad = int(input("digite la edad:0"))

if edad > 17:
    print("Debe solicitar cédula de ciudadanía")
else:
    print("No debe solicitar cédula de ciudadanía")
print('\n')
