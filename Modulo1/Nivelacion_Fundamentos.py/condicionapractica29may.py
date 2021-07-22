experiencia = 2
salario = 2000000

# Este ejercicio es de condicionales if (si condicional)
# if traduce si en ingles
# si tiene más de dos años de exp el bono es de 100000
# si tiene cuatro años o más de exp el bono es de 200000
# si tiene seis años o más de exp el bono es de 200000

if experiencia > 2 and experiencia < 4:
    salario = salario + 100000
elif experiencia >= 4 and experiencia < 6:
    salario = salario + 200000
elif experiencia >= 6:
    salario = salario + 300000
print(salario)
