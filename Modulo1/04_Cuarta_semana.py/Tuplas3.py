"""
count()
Este método recibe un elemento como argumento y cuenta la cantidad de veces que aparece en la tupla"""

valores = ("Uva", True, "Avión", 10)
print("La palabra Uva aparece en la tupla: ", valores.count('Uva'))

# Acceso a los elementos usando un índice negativo
frutas = ('Uva', 'Lulo', 'Naranja', 'Mango')
frutas[-1]  # Mango

# Acceso a un subconjunto de elementos

vocales = 'a', 'e', 'i', 'o', 'u'
vocales[2:3]  # Elementos desde elíndice 2 hasta el índice 3-1 (i)
vocales[2:4]  # Elementos desde el 2 hasta el índice 4-1 (i,o)
vocales[:]  # Todos los elementos
