"""6. Crear un programa que reciba por teclado la edad de 10 personas e imprima por pantalla cuantos son mayores de edad y menores de edad hay en el grupo."""

print("\n")
cantidad = int(input("Ingrese la cantidad de personas: "))

mayor_edad = 0
menor_edad = 0

for i in range(10):
    edad = int(input("Ingrese la edad: "))
    if edad >= 18:
        mayor_edad = mayor_edad + 1
    else:
        menor_edad = menor_edad + 1
print("las personas encuestadas mayor de edad son ", mayor_edad,
      "Las personas encuestadas menor de edad son ", menor_edad)
print("\n")
