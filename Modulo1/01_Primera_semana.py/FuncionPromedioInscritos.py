'''
 Promedio de personas inscritas en la Academia de dibujo profesional Leonardo da Vinci al curso  de dibujo de lunes a viernes
 :Parámetros:

nro_inscritos:lunes(int),nro_inscritos_martes: (int), nro_inscritos_miercoles: (int), nro_inscritos_jueves: (int), nro_inscritos_viernes: (int)

 Retorno:

 String de la forma "El promedio de personas inscritas al curso de dibujo de lunes a viernes 
 
 es {promedioSuma}" pass

 '''



# Aquí inicia aplicación 

nro_inscritos_lunes = 50 
nro_inscritos_martes = 80
nro_inscritos_miercoles = 100 
nro_inscritos_jueves = 45 
nro_inscritos_viernes = 30 

# Función que realiza el promedio de varios números


Promedio_suma = (nro_inscritos_lunes + nro_inscritos_martes + nro_inscritos_miercoles + nro_inscritos_jueves + nro_inscritos_viernes)/5


print("El promedio de personas inscritas al curso de dibujo de lunes a viernes es: %d" %Promedio_suma)