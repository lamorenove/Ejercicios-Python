# Descripción del problema Reto #3

"""Una ferretería desea conocer el total de las ventas en general y el consolidado 
de ventas de contado y crédito, se debe procesar n cantidad de facturas con la siguiente información:

1. Tipo venta
2. Valor factura

Escriba una función que reciba como parámetros una lista de diccionarios que contengan
la siguiente información:

1. tipo_venta:"credito" o "contado"
2. valor_factura:int

La respuesta debe retornar un diccionario con la siguiente estructura:

{total_ventas:int, total_ventas_contado:int, total_ventas_credito:int}

Ejemplo:

Factura 1                       Factura 2                           Factura 3                       Return
{                                {                                {                                {
    "tipo_venta": "credito",        "tipo_venta": "contado",        "tipo_venta": "credito",        "total_ventas": 205000,
     "total_factura":85000           "total_factura":100000           "total_factura":20000          "total_ventas_contado":100000
}                                }                                   }                              "total_ventas_credito":105000
                                                                                                    } 

ENTRADAS:

Nombre               Tipo                       Estructura                                  Descripción
datos               list                [{"tipo_venta": str("contado" o "credito),      La lista contiene n cantidad de 
                                        "total_factura": int                            diccionarios con la información 
                                        }]                                              de las ventas realizadas 
                                                                                        soportadas con las facturas.


SALIDAS:

Tipo del Retorno                        Estructura                                      Descripción
dict                                   {                                                El diccionario contiene el
                                        "total_ventas":int,                             total de ventas en general,
                                        "total_ventas_contado": int                     total de ventas a credito y 
                                        "total_ventas_credito": int                     total de ventas a contado 
                                        }                                               

Esqueleto

def consolidar_ventas(datos: list) -> dict:
    pass
"""


def consolidar_ventas(datos: list) -> dict:
    venta_credito: str = "credito"
    venta_contado: str = "contado"
    total_ventas = 0
    total_ventas_credito = 0
    total_ventas_contado = 0

    for item in datos:
        total_ventas += item['total_factura']
        if item['tipo_venta'] == venta_contado:
            total_ventas_contado += item['total_factura']
        elif item['tipo_venta'] == venta_credito:
            total_ventas_credito += item['total_factura']
    resultado: dict = {
        "total_ventas": total_ventas,
        "total_ventas_contado": total_ventas_contado,
        "total_ventas_credito": total_ventas_credito
    }
    return resultado


datos: list = [
    {
        "tipo_venta": "credito",
        "total_factura": 85000
    },
    {
        "tipo_venta": "contado",
        "total_factura": 100000
    },
    {
        "tipo_venta": "credito",
        "total_factura": 20000
    }
]

print(consolidar_ventas(datos))
