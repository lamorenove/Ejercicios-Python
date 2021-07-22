def contador_suma(conPar, conImpar, sumPar, sumImpar):
    j = 1
    while j <= numero:
        num = int(input("Ingrese un número mayor a cero: "))
        if num <= 0:
            print(
                "Recuerda ingresar un número mayor que cero, este no se tendrá en cuenta")
        else:
            if (num % 2 == 0):
                conPar += 1
                sumPar = sumPar + num
            else:
                conImpar += 1
                sumImpar = sumImpar + num
            j += 1
    return f'La cantidad de números pares son: {conPar} \nLa cantidad de números Impares son: {conImpar}\nLa sumatoria de los números pares es: {sumPar}\nLa sumatoria de los números Impares es: {sumImpar}'


print("\n")
numero = int(input("¿Cuántos números desea ingresar?: "))
conPar, conImpar, sumPar, sumImpar = 0, 0, 0, 0
print(contador_suma(conPar, conImpar, sumPar, sumImpar))
print("\n")
