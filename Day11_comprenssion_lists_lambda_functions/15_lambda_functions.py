"""
Funciones Lambda

Las funciones lambda en Python son pequeñas funciones anónimas que 
se definen en una sola línea de código. Se crean con la palabra 
clave lambda, seguida de los argumentos y una expresión que se evalúa 
y retorna.

Su sintaxis es simple:
    lambda <argumentos>: <expresion>
    
Características principales
    - Anonimato: No tienen un nombre formal, lo que las hace ideales para 
                 tareas rápidas y sencillas.
    - Concisión: Se definen en una sola línea, lo que agiliza el código.
    - Expresión única: Solo pueden contener una expresión que se evalúa y retorna.

¿Dónde se utilizan las funciones lambda?
Las funciones lambda son útiles en diversos escenarios y cuando necesitas una función temporal:

    - Funciones de orden superior: Como argumentos para funciones como map, filter y sorted, 
                donde se requiere una función simple y rápida.
    - Comprensión de listas y otras estructuras: Para realizar operaciones sencillas dentro 
                de comprensiones de listas, conjuntos o diccionarios.
    - Tareas puntuales: Cuando necesitas una función rápida y sencilla para una tarea específica 
                y no quieres definir una función completa con def.
                
Ejemplos prácticos
    * map() con lambda:
            numbers = [1, 2, 3, 4, 5]
            squares = list(map(lambda x: x**2, numbers))  
            # Salida: [1, 4, 9, 16, 25]
            
    * filter() con lambda:
            numbers = [1, 2, 3, 4, 5, 6]
            evens = list(filter(lambda x: x % 2 == 0, numbers))  
            # Salida: [2, 4, 6]
            
    * sorted() con lambda:
            words = ["casa", "árbol", "sol", "luna"]
            words_sorted = sorted(palabras, key=lambda x: len(x))  
            # Salida: ["sol", "luna", "casa", "árbol"]

Las funciones lambda son una herramienta valiosa en Python para crear funciones 
anónimas y concisas. Su uso adecuado puede mejorar la legibilidad y eficiencia 
del código en situaciones específicas. Sin embargo, es importante recordar que 
están limitadas a expresiones simples de una sola línea.
"""
from functools import reduce

# 1. Operaciones matemáticas básicas
print("\n1. Operaciones matemáticas básicas:")
square = lambda x: x ** 2
cube = lambda x: x ** 3
power = lambda x, n: x ** n
add = lambda x, y: x + y

print(f"El cuadrado de 5: {square(5)}")  # 25
print(f"El Cubo de 3: {cube(3)}")      # 27
print(f"2 elevado a 4: {power(2, 4)}")  # 16
print(f"La suma de 3 y 4: {add(3, 4)}")      # 7

# 2. Funciones lambda con map()
print("\n2. Lambda con map():")
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
squared = list(map(lambda x: x ** 2, numbers))
to_fahrenheit = list(map(lambda c: (c * 9/5) + 32, [0, 10, 20, 30]))

print(f"Lista de números base: {numbers}")
print(f"Lista de números multiplicado por 2: {doubled}")
print(f"Lista de números elevado al cuadrado: {squared}")
print(f"Convertir Celsius a Fahrenheit: {to_fahrenheit}")

# 3. Funciones lambda con filter()
print("\n3. Lambda con filter():")
numbers = range(-5, 6)
positive = list(filter(lambda x: x > 0, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

print(f"Lista original de números: {list(numbers)}")
print(f"Números Positivos: {positive}")
print(f"Números Pares: {even}")
print(f"Números Divisible en 3: {divisible_by_3}")

# 4. Funciones lambda con sorted()
print("\n4. Lambda con sorted():")
words = ['banana', 'apple', 'date', 'cherry']
numbers = [23, 45, 12, 67, 89, 34]
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

sorted_by_length = sorted(words, key=lambda x: len(x))
sorted_by_last_digit = sorted(numbers, key=lambda x: x % 10)
sorted_by_second_element = sorted(pairs, key=lambda x: x[1])

print(f"Ordenado por longitud: {sorted_by_length}")
print(f"Ordenado por último dígito: {sorted_by_last_digit}")
print(f"Ordenado por el segundo elemento: {sorted_by_second_element}")

# 5. Funciones lambda en funciones de orden superior
print("\n5. Lambda en Funciones de Orden Superior (Higher-Order Functions):")
def apply_operation(num, func):
    """Aplica una función a un valor"""
    return func(num)

double = lambda x: x * 2
triple = lambda x: x * 3
square = lambda x: x ** 2
cube = lambda x: x ** 3

print(f"El doble de 5: {apply_operation(5, double)}")
print(f"El Triple de 5: {apply_operation(5, triple)}")
print(f"El Cuadrado de 5: {apply_operation(5, square)}")
print(f"El Cuabo de 5: {apply_operation(5, cube)}")

# 6. Lambda con múltiples condiciones
print("\n6. Lambda con Multiple Condiciones:")
grade_status = lambda score: "Excelente" if score >= 90 else "Bueno" if score >= 70 else "Necesita Mejorar"
age_group = lambda age: "Niño" if age < 13 else "Adolescente" if age < 20 else "Adulto"

print(f"Score 95: {grade_status(95)}")
print(f"Score 75: {grade_status(75)}")
print(f"Score 60: {grade_status(60)}")
print(f"Edad 10: {age_group(10)}")
print(f"Edad 15: {age_group(15)}")
print(f"Edad 25: {age_group(25)}")

# 7. Lambda con diccionarios
print("\n7. Lambda con Dictionaries:")
students = [
    {'name': 'John', 'age': 20, 'grade': 90},
    {'name': 'Jane', 'age': 19, 'grade': 88},
    {'name': 'Bob', 'age': 21, 'grade': 95}
]

sorted_by_age = sorted(students, key=lambda x: x['age'])
sorted_by_grade = sorted(students, key=lambda x: x['grade'], reverse=True)
names_only = list(map(lambda x: x['name'], students))

print(f"Ordenado por edad: {sorted_by_age}")
print(f"Ordenado descendientemente por grado: {sorted_by_grade}")
print(f"Solo nombres: {names_only}")

# 8. Lambda con reduce()
print("\n8. Lambda con reduce():")
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
max_value = reduce(lambda x, y: x if x > y else y, numbers)
concatenated = reduce(lambda x, y: f"{x},{y}", map(str, numbers))

print(f"Producto de los números {numbers} es: {product}")
print(f"El máximo valor de los numeros {numbers} es: {max_value}")
print(f"Concatenación de los números {numbers} es: {concatenated}")

# 9. Lambda en list comprehension y expresiones generadoras
print("\n9. Lambda en Comprensión de Lista y Expresiones Generadoras:")
operations = [(lambda x: x ** 2), (lambda x: x ** 3), (lambda x: x ** 4), (lambda x: x ** 5), (lambda x: x ** 6), (lambda x: x ** 7)]
number = 2
results = [func(number) for func in operations]
print(f"Diferentes potencias de {number}: {results}")

# 10. Lambda con argumentos por defecto
print("\n10. Lambda con Argumento por DEfecto:")
greeting = lambda name, greeting="Saludo Visitante..!!": f"{greeting}, {name}!"
power_n = lambda x, n=2: x ** n

print(greeting("John")) # Saludo por defecto
print(greeting("Jane", "Saludos...")) # El segundo parámetro sobreescribe el valor por defecto
print(f"Cuadrado de un número (por defecto): {power_n(3)}") # Valor por defecto
print(f"Cubo de un número: {power_n(3, 3)}") # El segundo parámetro sobreescribe el valor por defecto
