# Función
def calcularDefinitiva(p1, p2, l, t):
    defini = p1*0.3 + p2*0.35 + l*0.25 + t*0, 1
    return (defini)


# Programa principal
numeroEst = int(input("Ingrese el número de estudiantes: "))
j = 1
while(j <= numeroEst):
    nombre = input("Ingrese el nombre: ")
    par1 = float(input("parcial 1: "))
    par2 = float(input("parcial 2: "))
    lab = float(input("Laboratorios: "))
    tra = float(input("Trabajos: "))

    definitiva = (calcularDefinitiva(par1, par2, lab, tra))
    print(definitiva)
    print("la nota definitiva de ", nombre, " es: ", definitiva)
    j += 1
