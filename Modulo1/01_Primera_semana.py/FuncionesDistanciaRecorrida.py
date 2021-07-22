#Calcula la distancia recorrida en un periodo de tiempo

v=int(input("Diga la velocidad "))
t=int(input("Diga el tiempo "))

D=v*t

print("La distancia recorrida es: ",D)

#Calcula la distancia recorrida en un periodo de tiempo usando función

def distancia_recorrida(v, t):
    d = v * t
    return d
print('\n')
#Aquí inicia la aplicación, esta es una función.
velocidad = int(input("Diga la velocidad: "))
tiempo = int(input("Diga el tiempo: "))
print('\n')
d = distancia_recorrida(velocidad, tiempo)
print("La distancia recorrida del móvile es: {} m/s2 con una velocidad de {} y un tiempo de {}". format (d, velocidad, tiempo))
print('\n')