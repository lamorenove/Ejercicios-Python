""" En una tienda de descuentos se efectúa una promoción en la cual se hace un descuento sobre
el valor de la compra total según el color de la bolita que el cliente saque al para en caja.

Si la bolita es blanca                  0% de descuento
Si la bolita es verde                   10% de descuento
Si la bolita es amarilla                25% de descuento
Si la bolita es azul                    50% de descuento
Si la bolita es roja                    100% de descuento

Escriba el valor total que el cliente debe pagar por su compra

ENTRADAS
Valor de la commpra
Color de la bolita

PROCESO


Inicio
 valorcompra: Entero
 color_bolita:(blanca, verde, amarilla, azul, roja)

 LEER valorcompra, descuento
 Si input("color de la bolita es: {blanco}") entonces
             descuento = valorcompra * 0%
     Si No
           Si ("color de la bolita es: {verde}") entonces
                         descuento = valorcompra * 10%
                    Si no
                           Si ("color de la bolita es: {amarilla}") entonces
                                       descuento = valorcompra * 25%
                                 Si no
                                   Si ("color de la bolita es: {azul}") entonces
                                                         descuento = valorcompra * 50%
                                                Si no
                                                    Si ("color de la bolita es: {roja}") entonces
                                                         descuento = valorcompra * 100%
                                     Fin Si
                                     Fin Si
                           Fin Si
               Fin Si
     Fin Si
     imprimir “El valor de la compra es:{] y el valor del descuento es{}.
Fin

SALIDAS

ValorCompra
Descuento

"""

# Aquí inicia la función

valor_compra = (int("El valor de compra es:  ")*descuento)


def descuento(valor_compra, descuento) -> str:
        descuento = (valor_compra * 0 %):
            if("color de la bolita es: {verde}"):
            else:
            descuento = (valor_compra * 10 %)
                    if("color de la bolita es: {amarilla}"):
                    else:
                descuento = (valor_compra * 25 %)
                    if("color de la bolita es: {azul}"):
                        else:
                    descuento = (valor_compra * 50 %)
                        if("color de la bolita es: {roja}"):
                            else:
                        descuento = (valor_compra * 100 %):
return "El valor de la compra es: %.0f" % and
    "El descuento es: %.0f"

Resultado = (valor_compra, descuento)
