'''
1.- Declarar una lista vacía
2.- Declarar una lista con más de 5 elementos
3.- Encuentra la longitud de tu lista
4.- Obtener el primer elemento, el elemento del medio y el último elemento de la lista.
5.- Declara una lista llamada mixed_data_types, coloca tu(nombre, edad, altura, estado civil, dirección)
6.- Declare una variable de lista llamada it_companies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
7.- Imprima la lista usando print()
8.- Imprima el número de empresas en la lista
9.- Imprima la primera, la segunda y la última empresa.
10.- Imprima el listado después de modificar una de las empresas
11.- Añadir una empresa de TI a it_companies
12.- Insertar una empresa de TI en el medio de la lista de empresas
13.- Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)
14.- Unir it_companies con una cadena '#; '
15.- Comprueba si una determinada empresa existe en la lista it_companies.
16.- Ordenar la lista usando el método sort()
17.- Invierta la lista en orden descendente utilizando el método reverse()
18.- Separa las primeras 3 empresas de la lista.
19.- Elimina las últimas 3 empresas de la lista.
20.- Elimina de la lista las empresas de TI intermedias
21.- Eliminar la primera empresa de TI de la lista
22.- Eliminar la o las empresas de TI intermedias de la lista
23.- Eliminar la última empresa de TI de la lista
24.- Eliminar todas las empresas de TI de la lista
25.- Destruir la lista de empresas de TI
26.- Une las siguientes listas:
        front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
        back_end = ['Node','Express', 'MongoDB']
27.- Después de unir las listas en la pregunta 26. 
     Copie la lista unida y asígnela a una variable full_stack, 
     luego inserte Python y SQL después de Redux.
28.- La siguiente es una lista de 10 estudiantes por edades:
            students_ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    28.1.- Ordena la lista y encuentra la edad mínima y máxima.
    28.2.- Agregue la edad mínima y la edad máxima nuevamente a la lista
    28.3.- Encuentra la edad media (un elemento intermedio o dos elementos intermedios divididos por dos)
    28.4.- Encuentra la edad promedio (suma de todos los elementos dividida por su número)
    28.5.- Encuentra el rango de edades (máximo menos mínimo)
    28.6.- Compare el valor de (mín - promedio) y (máx - promedio), use el método abs()
'''

# 1.- Declarar una lista vacía
print('\n1.- Declarar una lista vacía')
empty_list = []

# 2.- Declarar una lista con más de 5 elementos
print('\n2.- Declarar una lista con más de 5 elementos')
more_than_five = [1, 2, 3, 4, 5, 6]

# 3.- Encuentra la longitud de tu lista
print('\n3.- Encuentra la longitud de tu lista')
length_of_list = len(more_than_five)

# 4.- Obtener el primer elemento, el elemento del medio y el último elemento de la lista.
print('\n4.- Obtener el primer elemento, el elemento del medio y el último elemento de la lista.')
first_element = more_than_five[0]
middle_element = more_than_five[len(more_than_five) // 2]
last_element = more_than_five[-1]

# 5.- Declara una lista llamada mixed_data_types, coloca tu(nombre, edad, altura, estado civil, dirección)
print('\n5.- Declara una lista llamada mixed_data_types, coloca tu(nombre, edad, altura, estado civil, nacionalidad)')
mixed_data_types = ["Johnny Bravo", 32, 1.78, "Soltero", "Venezolano"]

# 6.- Declare una variable de lista llamada it_companies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
print('\n6.- Declare una variable de lista llamada it_companies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.')
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7.- Imprima la lista usando print()
print('\n7.- Imprima la lista usando print()')
print(it_companies)

# 8.- Imprima el número de empresas en la lista
print('\n8.- Imprima el número de empresas en la lista')
print(len(it_companies))

# 9.- Imprima la primera, la segunda y la última empresa.
print('\n9.- Imprima la primera, la segunda y la última empresa.')
print(it_companies[0], it_companies[1], it_companies[-1])

# 10.- Imprima el listado después de modificar una de las empresas
print('\n10.- Imprima el listado después de modificar una de las empresas.')
it_companies[0] = "Meta"
print(it_companies)

# 11.- Añadir una empresa de TI a it_companies
print('\n11.- Añadir una empresa de TI a it_companies.')
it_companies.append("Tesla")
print(it_companies)

# 12.- Insertar una empresa de TI en el medio de la lista de empresas
print('\n12.- Insertar una empresa de TI en el medio de la lista de empresas.')
it_companies.insert(len(it_companies) // 2, "Twitter")
print(it_companies)

# 13.- Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)
print('\n13.- Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!).')
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14.- Unir it_companies con una cadena '#; '
print("\n14.- Unir it_companies con una cadena '#; '.")
joined_companies = '#; '.join(it_companies)
print(joined_companies)

# 15.- Comprueba si una determinada empresa existe en la lista it_companies.
print("\n15.- Comprueba si una determinada empresa existe en la lista it_companies.")
print("Google" in it_companies)

# 16.- Ordenar la lista usando el método sort()
print("\n16.- Ordenar la lista usando el método sort().")
it_companies.sort()
print(it_companies)

# 17.- Invierta la lista en orden descendente utilizando el método reverse()
print("\n17.- Invierta la lista en orden descendente utilizando el método reverse()")
it_companies.reverse()
print(it_companies)

# 18.- Separa las primeras 3 empresas de la lista.
print("\n18.- Separa las primeras 3 empresas de la lista.")
first_three_companies = it_companies[:3]
print(first_three_companies)

# 19.- Elimina las últimas 3 empresas de la lista.
print("\n19.- Elimina las últimas 3 empresas de la lista.")
it_companies = it_companies[:-3]
print(it_companies)

# 20.- Elimina de la lista las empresas de TI intermedias
print("\n20.- Elimina de la lista las empresas de TI intermedias")
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)

# 21.- Eliminar la primera empresa de TI de la lista
print("\n21.- Eliminar la primera empresa de TI de la lista")
it_companies.pop(0)
print(it_companies)

# 22.- Eliminar la o las empresas de TI intermedias de la lista
print("\n22.- Eliminar la o las empresas de TI intermedias de la lista")
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)

# 23.- Eliminar la última empresa de TI de la lista
print("\n23.- Eliminar la última empresa de TI de la lista")
it_companies.pop()
print(it_companies)

# 24.- Eliminar todas las empresas de TI de la lista
print("\n24.- Eliminar todas las empresas de TI de la lista")
it_companies.clear()
print(it_companies)

# 25.- Destruir la lista de empresas de TI
print("\n25.- Destruir la lista de empresas de TI")
del it_companies

# 26.- Une las siguientes listas:
print('''\n26.- Une las siguientes listas:
        front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
        back_end = ['Node', 'Express', 'MongoDB']      
      ''')
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27.- Después de unir las listas en la pregunta 26. 
# Copie la lista unida y asígnela a una variable full_stack, 
# luego inserte Python y SQL después de Redux.
print("\n27.- Copie la lista unida y asígnela a una variable full_stack, luego inserte Python y SQL después de Redux.")
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

# 28.- La siguiente es una lista de 10 estudiantes por edades
students_ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f"\n28.- Lista de edades de estudiantes: {students_ages}")

# 28.1.- Ordena la lista y encuentra la edad mínima y máxima
students_ages.sort()
min_age = min(students_ages)
max_age = max(students_ages)
print(f"28.1.- Edad mínima: {min_age}, edad máxima: {max_age}")

# 28.2.- Agregue la edad mínima y la edad máxima nuevamente a la lista
students_ages.extend([min_age, max_age])
print(f"28.2.- Lista con edades min y max agregadas: {students_ages}")

# 28.3.- Encuentra la edad media
sorted_ages = sorted(students_ages)
n = len(sorted_ages)
if n % 2 == 0:
    median = (sorted_ages[n//2 - 1] + sorted_ages[n//2]) / 2
else:
    median = sorted_ages[n//2]
print(f"28.3.- Edad media: {median}")

# 28.4.- Encuentra la edad promedio
average_age = sum(students_ages) / len(students_ages)
print(f"28.4.- Edad promedio: {average_age}")

# 28.5.- Encuentra el rango de edades
age_range = max_age - min_age
print(f"28.5.- Rango de edades: {age_range}" )

# 28.6.- Compara el valor de (mín - promedio) y (máx - promedio)
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print(f"28.6.- Diferencia con promedio - Mínima: {min_diff} Máxima: {max_diff}", )

