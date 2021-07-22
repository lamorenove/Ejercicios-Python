'''
* Zip es una función para reorganizar listas
* Como parámetros admite un conjunto de listas

*La función zip empareja el primer elemento de cada iterador
 luego a los segundos elementos y así sucesivamente.

* Los iterables pueden ser listas Python, diccionarios,
  cadenas, o cualquier objeto iterable.

Lo que hace es tomar un elemento  de cada lista y unirlos
en una tupla, después une todas las tuplas en una sola lista.
'''


paises = ["China", "India", "Estados Unidos", "Indonesia"]
poblaciones = [1391, 1364, 327, 264]
resultado = list(zip(paises, poblaciones))
print(resultado)

# [(China, 1392)]
