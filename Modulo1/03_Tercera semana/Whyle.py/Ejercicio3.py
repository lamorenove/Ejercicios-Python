'''
Realizar un algoritmo para sumar consecutivamente y cuando la suma sea 
superior a 100 deje de pedir números y 
muestre el total.
'''
suma = 0
numero = 0


while suma <= 100:
    numero = int(input("Digite un número: "))
    suma = suma + numero

print(("El total de la suma es: "), round(suma))
'''
Desarrolle un algoritmo que funcione como caja registradora. Que pare cuando el código del artículo se igual a *. 
Que lea código del articulo,nombre y 
Precio. Debe calcular subtotal,iva(15%) y total factura.
'''
# programa principal

codigo = 0
while codigo != "*":

    codigo = input("Ingrese el código: ")
    if codigo != "*":
        nombre = input("Nombre del artículo: ")
        precio = float(input("Precio del artículo: "))
        print(codigo)
        print(nombre)
        print(precio)
        subtotal = float(precio/1.15)
        iva = subtotal * 0.15
        Total_factura = subtotal + iva
        print("El subtotal es: ", subtotal, "El IVA es: ", iva,
              "El total de la factura es: ", Total_factura)
