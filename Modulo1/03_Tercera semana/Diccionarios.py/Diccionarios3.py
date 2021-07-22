def promedioVentas(dicVentas):
    sumatoria = 0
    sumatoria += dicVentas['ventaLunes']
    sumatoria += dicVentas['ventaMartes']
    sumatoria += dicVentas['ventaMiercoles']
    sumatoria += dicVentas['ventaJueves']
    sumatoria += dicVentas['ventaViernes']
    promedio = round(sumatoria/5, 2)
    return promedio


# Creo el diccionario dicNotas={}
dicventas = {
    "ventaLunes": 100000,
    "ventaMartes": 50000,
    "ventaMiercoles": 200000,
    "ventaJueves": 350000.2,
    "ventaViernes": 400000.5
}
print("El promedio de las ventas de Lunes a Viernes es:", promedioVentas(dicventas))
