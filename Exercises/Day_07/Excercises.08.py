'''
Ejercicios

1.- Crea un diccionario vacío llamado perro
2.- Añade nombre, color, raza, patas y edad al diccionario de perros
3.- Cree un diccionario de estudiantes y agregue nombre, apellido, género, edad, estado civil, habilidades, país, ciudad y dirección como claves para el diccionario.
4.- Obtenga la longitud del diccionario del estudiante
5.- Obtenga el valor de las habilidades y verifique el tipo de datos, debe ser una lista
6.- Modifique los valores de las habilidades agregando una o dos habilidades
7.- Obtenga las claves del diccionario como una lista
8.- Obtener los valores del diccionario como una lista
9.- Cambie el diccionario a una lista de tuplas usando el método items()
10.- Eliminar uno de los elementos del diccionario
11.- Eliminar uno de los diccionarios
'''

# 1.- Crea un diccionario vacío llamado perro
dog = {}
print(f'Diccionario perro (sin elementos): {dog}')

# 2.- Añade nombre, color, raza, patas y edad al diccionario de perro
dog['name'] = 'Maximus'
dog['color'] = 'Negro'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
print(f'Diccionario perro (con elementos): {dog}')

# 3.- Cree un diccionario de estudiantes y agregue nombre, apellido, género, edad, estado civil, habilidades, país, ciudad y dirección como claves para el diccionario.
student = {}
student['first_name'] = 'John'
student['last_name'] = 'Doe'
student['gender'] = 'Masculino'
student['age'] = 35
student['marital_status'] = 'Soltero'
student['skills'] = ['Python', 'C#', 'PHP', 'JavaScripts', 'TypeScript']
student['country'] = 'USA'
student['city'] = 'Tucson'
student['address'] = 'S 6th Av.'
print(f'Diccionario estudiante (con elementos): {student}')

# 4.- Obtenga la longitud del diccionario del estudiante
print(f'Longitud del diccionario del estudiante: {len(student)}')

# 5.- Obtenga el valor de las habilidades y verifique el tipo de datos, debe ser una lista
print(f'Habilidades del estudiante: {student["skills"]}')
print(f'Tipo de datos de las habilidades: {type(student["skills"])}')

# 6.- Modifique los valores de las habilidades agregando una o dos habilidades
student['skills'].append('Java')
student['skills'].append('C++')
print(f'Habilidades del estudiante: {student["skills"]}')

# 7.- Obtenga las claves del diccionario como una lista
print(f'Claves del diccionario del estudiante: {list(student.keys())}')

# 8.- Obtener los valores del diccionario como una lista
print(f'Valores del diccionario del estudiante: {list(student.values())}')

# 9.- Cambie el diccionario a una lista de tuplas usando el método items()
print(f'Lista de tuplas del diccionario del estudiante: {list(student.items())}')

# 10.- Eliminar uno de los elementos del diccionario
del student['skills']
print(f'Diccionario estudiante (sin habilidades): {student}')

# 11.- Eliminar uno de los diccionarios
del student














