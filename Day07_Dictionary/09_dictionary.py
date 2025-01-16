"""
Un diccionario en Python es una colección de datos desordenada y mutable que almacena elementos 
en pares clave-valor. Cada clave debe ser única y, por lo general, es inmutable (como una cadena, 
un número o una tupla). Los valores asociados a las claves pueden ser de cualquier tipo de dato.

Los diccionarios se crean utilizando llaves {} y se separan los pares clave-valor con comas.

A diferencia de los conjuntos, los diccionarios permiten asociar un valor a cada clave, lo que 
los hace ideales para representar datos estructurados. 

La sintaxis de los diccionarios es similar a los objetos literales de otros lenguajes de programación.
"""

# Declarando  un Diccionario
empty_dict = {}

# Declarando e inicializando la variable student como un diccionario
student = {
    "first_name": "John",
    "last_name": "Doe",
    "id": "X-12345678",
    "gender": "Masculino",
    "age": 35,
    "skills": ["Python", "C#", "PHP", "JavaScripts", "TypeScript"],
    "address": {
        "country": "USA",
        "state": "Arizona",
        "city": "Tucson",
        "street": "S 6th Av.",
        "building": "271",
        "zip_code": "520",
    },
}

# Accediendo a los datos del diccionario.
# Se puede acceder a los datos del diccionario utilizando la clave del elemento.
# Como si se tratase un array asociativo, utilizando corchetes y la clave del elemento.
print("\nAccediendo como se tratare un array asociativo:")
print(f'Nombre completo del estudiante: {student["first_name"]} {student["last_name"]}')
print(f'Edad: {student["age"]}')
print(f'Sexo: {student["gender"]}')
print(f'Habilidades: {student["skills"]}')
print(f'Código postal: {student["address"]["zip_code"]}')

# Tambien se puede obtener el valor de un elemento utilizando el método get("clave").
# Si la clave no existe, se devuelve None.
print("\nAccediendo con el método get():")
print(
    f'Nombre completo del estudiante: {student.get("first_name")} {student.get("last_name")}'
)
print(f'Edad: {student.get("age")}')
print(f'Sexo: {student.get("gender")}')
print(f'Habilidades: {student.get("skills")}')
print(f'Código postal: {student.get("address").get("zip_code")}')

# Agregado elementos al diccionario
print("\nAgregando nuevos elementos:")
print(f'Diccionario student (antes de agregar los elementos): {student}')
student['nickname'] = 'Zordon_1980'
student['skills'].append('HTML')
print(f'Diccionario student (despues de agregar los elementos): {student}')

# Para modificar un elemento del diccionario, se puede utilizar la clave del elemento y asignarle un nuevo valor.
print("\nModificando un elemento del diccionario:")
print(f"Valor original: {student['nickname']}")
student['nickname'] = 'Maximus2YK'
print(f"Valor modificado: {student['nickname']}")

# Para verificar o checar si una clave existe en el diccionario, se puede utilizar el operador in.
print("\nVerificando si una clave existe en el diccionario:")
print(f"Clave 'nickname' existe en el diccionario: {'nickname' in student}") # True
print(f"Clave 'pets' existe en el diccionario: {'pets' in student}") # False

# Removiendo una clave-valor de un diccionario:
# 1.- usando el metodo pop("clave"), Elimina el elemento cuyo clave se especifica y devuelve su valor asociado
# 2.- usando el metodo popitem(), Elimina y devuelve un par clave-valor aleatorio del diccionario.
# 3.- usando el metodo clear(), Elimina todos los elementos del diccionario.
# 4.- usando el operador del diccionario["clave"], al igual que el metodo pop(), elimina el elemento cuyo clave se especifica, pero no devuelve su valor asociado.

print("\nRemoviendo una clave-valor de un diccionario:")
print(f"Diccionario student (antes de eliminar el elemento): {student}")
item_removed = student.pop('nickname')
print(f"Diccionario student (despues de eliminar el elemento): {student}")
print(f"Valor eliminado: {item_removed}")

# Removiendo el ultimo elemento del diccionario
print("\nRemoviendo el ultimo elemento del diccionario:")
print(f"Diccionario student (antes de eliminar el elemento): {student}")
last_item_removed = student.popitem()
print(f"Diccionario student (despues de eliminar el elemento): {student}")
print(f"Valor eliminado: {last_item_removed}")

# Removiendo un elemento
print("\nRemoviendo todos los elementos del diccionario:")
print(f"Diccionario student (antes de eliminar el elemento): {student}")
del student['age']
print(f"Diccionario student (despues de eliminar el elemento): {student}")

# Copiando un diccionario
print("\nCopiando un diccionario:")
student_copy = student.copy()
print(f"Diccionario student (antes de copiar el diccionario): {student}")
print(f"Diccionario student (despues de copiar el diccionario): {student_copy}")

# Obteniendo el numero de elementos del diccionario
print("\nObteniendo el numero de elementos del diccionario:")
print(f"Numero de elementos del diccionario: {len(student)}")

# Obteniendo el tipo de dato del diccionario
print("\nObteniendo el tipo de dato del diccionario:")
print(f"Tipo de dato del diccionario: {type(student)}")

# Obteniendo todas las claves de un diccionario
print("\nObteniendo todas las claves de un diccionario:")
print(f"Claves del diccionario: {student.keys()}")

# Obteniendo todos los valores de un diccionario
print("\nObteniendo todos los valores de un diccionario:")
print(f"Valores del diccionario: {student.values()}")




