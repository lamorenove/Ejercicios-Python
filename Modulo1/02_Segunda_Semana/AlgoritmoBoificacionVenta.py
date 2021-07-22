'''6.	Elabora un algoritmo que permita ingresar el monto de la venta alcanzada por un vendedor duran un mes,
se debe calcular la bonificación (%) que tiene derecho de acuerdo a la siguiente tabla:


VENTA REALIZADA EN EL MES ($)	BONIFICACION (%)
0 – 1.000.000	                    0%
1.000.100 – 2.500.000	            4%
2.500.100 a más	                    8%

Imprimir Venta realizada en el mes y la bonificación obtenida.


ALGORITMO

Inicio
 venta,bonif: Entero
 LEER venta, bonif
 Si venta > 1000000  entonces
             bonif = venta * 0.0
     Si No
           Si (venta >= 1000000)  and (venta < 2500000) entonces
                         bonif = sm * 0.04
                    Si no
                           Si (venta >= 2500000)   entonces
                                       bonif = sm * 0.08
                           Fin Si
               Fin Si
     Fin Si
     imprimir “La bonificación es: ”,bonif
Fin

'''
venta_mes = int(input("Digite el valor mensual de la venta: "))


def bonif(venta):
    if (venta > 0) and (venta <= 1000000):
        bonif = (venta * 0.00)
    else:
        if (venta >= 1000000) and (venta < 2500000):
            bonif = (venta * 0.04)
        else:
            if (venta >= 2500000):
                bonif = (venta * 0.08)
    return bonif


resultado = bonif(venta_mes)
print('\n')
print("La venta es: ", venta_mes)
print('\n')
print("La bonificación es: ", resultado)
