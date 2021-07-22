"""
Diseñar un algoritmo que imprima el número del
artículo, código, precio y precio con descuento.  
Si el artículo tiene código 01, el descuento es
del 10%, Si el artículo es diferente 
el descuento es del 20% (solo existen dos artículos).

ALGORITMO
Inicio
    precio, precio_desc: Real
    LEER nom_articulo, codigo, precio
    Si codigo = 01 entonces
            precio_desc = precio-precio*010
        Si No
            precio_desc = precio-precio*0,20
    Fin Si
    Imprimir nom_articulo,codigo,
                        precio, precio_desc
Fin

"""
cod_articulo = input("Digite código del artículo: ")
nom_articulo = input("Digite nombre del artículo: ")
precio = float(input("Digite el precio del artículo: "))

if cod_articulo == "01":
    precio_desc = precio-precio*0.10
else:
    precio_desc = precio-precio*0.20

print('\n')
print("Código Artículo: ", cod_articulo)
print("Código Artículo: ", nom_articulo)
print("Precio Artículo : ", precio)
print("Precio con descuento: ", precio_desc)
print('\n')
