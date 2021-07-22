# Función filter()

def multiplo_cinco(numero):
    if numero % 5 == 0:
        return True


numeros = [2, 5, 10, 23, 50, 33]

resultado = list(filter(multiplo_cinco, numeros))
print(resultado)
