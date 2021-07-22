"""2. Leer 5 personas y pedir salario. Imprimir sumatoria de salario"""

Salario = 0
for i in range(5):
    nuevoSalario = int(input("Introduce el salario: "))
    Salario += nuevoSalario

print("La sumatoria de salario es: %.2f", Salario)
