"""
*Los iterables pueden ser lista Python, diccionarios,
    cadenas, o cualquier objeto iterable.
"""

x = ("Carmen", "Clara", "Carlos")

y = ("Torres", "Cossio", "Mosquera")

z = ("Perez", "Mejía", "Duque")

result = zip(x, y, z)

print(tuple(result))
