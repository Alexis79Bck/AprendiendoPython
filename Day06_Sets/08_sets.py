'''
Conjuntos (Sets) en Python:

Un conjunto es una colección desordenada y sin duplicados de elementos inmutables.

Características principales:
- Se definen usando llaves {} o la función set()
- No permiten elementos duplicados
- Son desordenados (no mantienen un orden específico)
- Son mutables (el conjunto puede modificarse)
- Los elementos deben ser inmutables (números, strings, tuplas)
- No se puede acceder por índice

Casos de uso comunes:
1. Eliminar duplicados de una secuencia
2. Operaciones matemáticas de conjuntos:
   - Unión (|): Combina elementos de dos conjuntos
   - Intersección (&): Elementos comunes entre conjuntos
   - Diferencia (-): Elementos en A que no están en B
   - Diferencia simétrica (^): Elementos que están en A o B, pero no en ambos

Métodos principales:
1. Agregar elementos:
   - add(): Agrega un elemento
   - update(): Agrega múltiples elementos

2. Eliminar elementos:
   - remove(): Elimina un elemento (error si no existe)
   - discard(): Elimina un elemento (sin error si no existe)
   - pop(): Elimina y retorna un elemento aleatorio
   - clear(): Elimina todos los elementos

3. Operaciones de conjuntos:
   - union(): Retorna la unión de conjuntos
   - intersection(): Retorna la intersección
   - difference(): Retorna la diferencia
   - symmetric_difference(): Retorna la diferencia simétrica
   
4. Métodos de verificación:
   - issubset(): Verifica si un conjunto es subconjunto de otro
   - issuperset(): Verifica si un conjunto contiene a otro
   - isdisjoint(): Verifica si dos conjuntos no tienen elementos en común

5. Operadores de comparación:
   - == : Verifica si dos conjuntos tienen los mismos elementos
   - <= : Verifica si es subconjunto
   - >= : Verifica si es superconjunto

6. Métodos de copia:
   - copy(): Crea una copia superficial del conjunto

'''

# Ejemplos básicos
print("\nEjemplos de conjuntos:")

# 1. Creación de conjuntos
numeros = {1, 2, 3, 4, 5}
frutas = {'manzana', 'banana', 'naranja'}
print("Conjunto de números:", numeros)
print("Conjunto de frutas:", frutas)

# 2. Eliminar duplicados
lista_con_duplicados = [1, 2, 2, 3, 3, 4, 4, 5, 5]
sin_duplicados = set(lista_con_duplicados)
print("\nLista original:", lista_con_duplicados)
print("Sin duplicados:", sin_duplicados)

# 3. Operaciones de conjuntos
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("\nOperaciones entre conjuntos:")
print("Set1:", set1)
print("Set2:", set2)
print("Unión:", set1 | set2)
print("Intersección:", set1 & set2)
print("Diferencia (set1 - set2):", set1 - set2)
print("Diferencia simétrica:", set1 ^ set2)

# 4. Métodos de modificación
colores = {'rojo', 'azul'}
print("\nMétodos de modificación:")
print("Conjunto original:", colores)
colores.add('verde')
print("Después de add():", colores)
colores.update(['amarillo', 'naranja'])
print("Después de update():", colores)
colores.remove('rojo')
print("Después de remove():", colores)

# 5. Métodos de operaciones de conjuntos
print("\nMétodos de operaciones de conjuntos:")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("A:", A)
print("B:", B)
print("A.union(B):", A.union(B))
print("A.intersection(B):", A.intersection(B))
print("A.difference(B):", A.difference(B))
print("A.symmetric_difference(B):", A.symmetric_difference(B))

# 6. Métodos de verificación
print("\nMétodos de verificación:")
C = {1, 2}
D = {1, 2, 3, 4, 5}
print("C:", C)
print("D:", D)
print("C es subconjunto de D?:", C.issubset(D))
print("D es superconjunto de C?:", D.issuperset(C))
print("A y B son disjuntos?:", A.isdisjoint(B))

# 7. Operadores de comparación
print("\nOperadores de comparación:")
set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = {1, 2}
print("set1 == set2:", set1 == set2)
print("set3 <= set1:", set3 <= set1)
print("set1 >= set3:", set1 >= set3)

# 8. Métodos de copia
print("\nMétodos de copia:")
original = {1, 2, 3}
copia = original.copy()
print("Original:", original)
print("Copia:", copia)
