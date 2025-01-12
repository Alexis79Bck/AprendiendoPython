'''
Ejercicios:

Dado los siguientes conjuntos:
    - it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    - A = {19, 22, 24, 20, 25, 26}
    - B = {19, 22, 20, 25, 26, 24, 28, 27}
    - ages = [22, 19, 24, 25, 26, 24, 25, 24]

1.- Encuentra la longitud del conjunto it_companies
2.- Añade 'Twitter' a it_companies
3.- Insertar varias empresas de TI a la vez en el conjunto it_companies
4.- Eliminar una de las empresas del conjunto it_companies
5.- ¿Cuál es la diferencia entre eliminar y descartar?
6.- Unir A y B
7.- Encuentra la intersección A y B
8.- Es un subconjunto de B
9.- ¿Son A y B conjuntos disjuntos?
10.- Unir A con B y B con A
11.- ¿Cuál es la diferencia simétrica entre A y B?
12.- Eliminar los conjuntos por completo
13.- Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?
14.- Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto.
15.- Soy profesor y me encanta inspirar y enseñar a la gente. 
     ¿Cuántas palabras únicas se han utilizado en la oración? 
     Utilice los métodos de división y de configuración para obtener las palabras únicas.
'''

# 0.
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(f'''Los conjuntos a trabajar en estos ejercicios:
       it_companies = {it_companies}
       A = {A}
       B = {B}
       ages = {ages}  
      ''')

# 1.
print(f'1.- La longitud del conjunto it_companies es: {len(it_companies)}')

# 2.
it_companies.add('Twitter')
print(f'2.-El conjunto it_companies con Twitter añadido es: {it_companies}')

# 3.
new_companies = {'Tesla', 'Samsung', 'Sony', 'LG', 'Panasonic'}
it_companies.update(new_companies)
print(f'3.- El conjunto it_companies con varias empresas añadidas es: {it_companies}')

# 4.
it_companies.remove('IBM')
print(f'4.-El conjunto it_companies con IBM eliminado es: {it_companies}')

# 5
print('''5.- La diferencia entre eliminar y descartar es que el método remove() elimina un elemento específico 
      del conjunto, mientras que el método discard() elimina un elemento si está presente, 
      pero no lanza un error si el elemento no existe.
      ''')

# 6.
union_AB = A.union(B)
print(f'6.- La unión de A y B es: {union_AB}')

# 7.
intersection_AB = A.intersection(B)
print(f'7.- La intersección de A y B es: {intersection_AB}')

# 8.
is_subset_B = A.issubset(B)
print(f'8.- A es un subconjunto de B: {is_subset_B}')

# 9.
is_disjoint = A.isdisjoint(B)
print(f'9.- A y B son conjuntos disjuntos: {is_disjoint}')

# 10.
union_AB = A.union(B)
union_BA = B.union(A)
union_AB_BA = union_AB.union(union_BA)
print(f'10.- La unión de A y B es: {union_AB}')
print(f'10.- La unión de B y A es: {union_BA}')
print(f'10.- La unión de AB y BA es: {union_AB_BA}')

# 11.
symmetric_difference_AB = A.symmetric_difference(B)
print(f'11.- La diferencia simétrica entre A y B es: {symmetric_difference_AB}')

# 12.
A.clear()
B.clear()
print(f'12.- Los conjuntos A y B han sido eliminados por completo: {A} y {B}')

# 13.
print(f"Edades en tipo Lista {ages}")
set_ages = set(ages)
print(f"Edades en tipo Conjunto {set_ages}")
print(f"La longitud de la lista es {len(ages)}")
print(f"La longitud del conjunto es {len(set_ages)}")
print(f"La lista es más grande que el conjunto: {len(ages) > len(set_ages)}")

# 14.
print('''14.- La diferencia entre los tipos de datos es que:
      - Una cadena es una secuencia de caracteres.
      - Una lista es una colección ordenada y mutable de elementos.
      - Una tupla es una colección ordenada e inmutable de elementos.
      - Un conjunto es una colección desordenada y mutable de elementos únicos.
      ''')

# 15.
sentence = "Soy profesor y me encanta inspirar y enseñar a la gente."
unique_words = set(sentence.split())
print(f"La oración es: {sentence}")
print(f'15.- El número de palabras únicas en la oración es: {len(unique_words)}')

