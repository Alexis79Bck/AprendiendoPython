'''
Tuplas en Python:

Una tupla es una colección ordenada e inmutable de elementos. 
A diferencia de las listas, las tuplas:
- Se definen usando paréntesis ()
- Son inmutables (no se pueden modificar después de creadas)
- Son más rápidas de procesar que las listas
- Pueden usarse como claves en diccionarios
- Son útiles para datos que no deben cambiar

Métodos principales de tuplas:
1. count(): Cuenta las ocurrencias de un elemento
2. index(): Encuentra el índice de la primera ocurrencia

Operaciones comunes:
- Acceso a elementos usando índices
- Slicing (rebanado)
- Concatenación
- Desempaquetado
- Conversión a/desde otros tipos
'''

# 1. Creación de tuplas
print("\n1. Creación de tuplas:")
# Tupla vacía
empty_tuple = ()
print("Tupla vacía:", empty_tuple)

# Tupla con un solo elemento (necesita una coma)
single_tuple = (1,)
print("Tupla de un elemento:", single_tuple)

# Tupla con múltiples elementos
numbers = (1, 2, 3, 4, 5)
fruits = ('manzana', 'banana', 'naranja')
mixed_tuple = (1, 'hello', True, 3.14)
print("Tupla de números:", numbers)
print("Tupla de frutas:", fruits)
print("Tupla mixta:", mixed_tuple)

# 2. Métodos de tuplas
print("\n2. Métodos de tuplas:")
repeated_fruits = ('manzana', 'banana', 'naranja', 'mora', 'naranja', 'limon', 'naranja')
print("Cantidad de veces que aparece 'naranja' en la tupla:", repeated_fruits.count('naranja'))
print("Índice de la primera aparicion de 'mora':", repeated_fruits.index('mora'))

# 3. Acceso a elementos
print("\n3. Acceso a elementos:")
print("Primer elemento:", fruits[0])
print("Último elemento:", fruits[-1])

# 4. Slicing (rebanado)
print("\n4. Slicing:")
print("Primeros dos elementos:", numbers[:2])
print("Últimos dos elementos:", numbers[-2:])
print("Elementos del medio:", numbers[1:4])

# 5. Concatenación
print("\n5. Concatenación:")
combined_tuple = numbers + fruits
print("Tuplas concatenadas:", combined_tuple)

# 6. Desempaquetado
print("\n6. Desempaquetado:")
x, y, z = fruits
print(f"x: {x}, y: {y}, z: {z}")

# 7. Conversión
print("\n7. Conversión:")
# Lista a tupla
list_to_tuple = tuple([1, 2, 3])
print("Lista convertida a tupla:", list_to_tuple)

# Tupla a lista
tuple_to_list = list(fruits)
print("Tupla convertida a lista:", tuple_to_list)

# 8. Operaciones de verificación
print("\n8. Operaciones de verificación:")
print("Longitud de la tupla fruits:", len(fruits))
print("'banana' está en fruits?:", 'banana' in fruits)
print("'mango' está en fruits?:", 'mango' in fruits)

# 9. Tuplas anidadas
print("\n9. Tuplas anidadas:")
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Tupla anidada:", nested_tuple)
print("Elemento (1,1):", nested_tuple[0][1])

# 10. Repetición de tuplas
print("\n10. Repetición de tuplas:")
repeated_tuple = (1, 2) * 3
print("Tupla repetida:", repeated_tuple)

# 11. Comparación de tuplas
print("\n11. Comparación de tuplas:")
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (1, 2, 4)
print("tuple1 == tuple2:", tuple1 == tuple2)
print("tuple1 < tuple3:", tuple1 < tuple3)

# 12. Uso como clave de diccionario
print("\n12. Uso como clave de diccionario:")
coordinates = {(0, 0): 'origen', (1, 0): 'derecha', (0, 1): 'arriba'}
print("Coordenadas:", coordinates)
print("Valor en origen:", coordinates[(0, 0)])
