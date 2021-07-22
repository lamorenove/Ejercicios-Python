"""2. Leer 5 personas y pedir salario. Imprimir sumatoria de salario"""
# manera clásica de resolverlo

print("\n")
suma_salario = 0

for i in range(5):
    salario = int(input("Ingrese el salario: "))
    suma_salario = suma_salario + salario
print("La sumatoria del salario delas 5 personas es ", suma_salario)
print("\n")
