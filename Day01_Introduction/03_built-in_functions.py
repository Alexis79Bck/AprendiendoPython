"""
Las funciones nativas de Python, también conocidas como funciones incorporadas, son funciones que están disponibles de forma predeterminada en el lenguaje de programación Python. 
Estas funciones no requieren ninguna importación de módulos adicionales y se pueden utilizar directamente en cualquier script de Python.

Las funciones nativas más comunes incluyen:

    1. `print()`: Se utiliza para imprimir un valor, mensajes o contenido de una variable en la consola.

    2. `len()`: Devuelve la longitud (el número de elementos) de un objeto.

    3. `type()`: Devuelve el tipo del objeto.

    4. `int()`, `float()`, `str()`: Convertir entre tipos de datos.

    5. `sum()`: Devuelve la suma de todos los elementos en un iterable.

    6. `max()`, `min()`: Devuelven el valor máximo y mínimo de un iterable, respectivamente.

    7. `input()`: Permite al usuario ingresar datos desde la consola.

    8. `range()`: Genera una secuencia de números.

Estas funciones son solo una pequeña muestra de las muchas funciones nativas disponibles en Python. 
Utilizarlas adecuadamente puede simplificar y hacer más eficiente el desarrollo de programas.
"""

# print() - Imprime un valor, mensajes o contenido de una variable en la consola
print("Hello World! i'm learning Python")  # Salida: Hello World! i'm learning Python

# len() - Devuelve la longitud de un objeto
elements = ['a', 'b', 'c', 1, 2, 3]
print(len(['a', 'b', 'c', 1, 2, 3]))  # Salida: 6 (Aunque es posible realizarlo, no se recomienda usar la función len() sobre el valor directo de la lista)
print(len(elements))  # Salida: 6 (Por convencion se debe escribir: inicializar una variable que va a contener la lista y asignando la lista a esa variable)

# type() - Devuelve el tipo de un objeto
number = 10
print(type(10))  # Salida: <class 'int'>

# int(), float(), str() - Convertir entre tipos de datos
number_str = "123" # Se define un número como cadena de texto
number_int = int(number_str) # Se convierte la cadena de texto a un número entero
print(number_int)  # Salida: 123

# sum() - Devuelve la suma de los elementos en un iterable
numbers_list = [1, 2, 3, 4]
print(sum(numbers_list))  # Salida: 10

# max(), min() - Devuelve el valor máximo y mínimo de un iterable
numbers_list = [1, 2, 3, 4]
print(max(numbers_list))  # Salida: 4
print(min(numbers_list))  # Salida: 1

# input() - Permite al usuario ingresar datos desde la consola
name = input("What is your name? ")  # Se solicita al usuario ingresar su nombre
print("Hello, " + name)  # Salida: Hello, [nombre ingresado por el usuario]

# range() - Genera una secuencia de números
for i in range(5):
    print(i)    # Salida: 0, 1, 2, 3, 4
    
# Ejemplo de uso de la función range() con inicio, fin y paso
for j in range(1, 10, 2):
    print(j)    # Salida: 1, 3, 5, 7, 9

'''
Python tiene la virtud de declarar multiples variables en una sola línea. 
La convención PEP8 no prohíbe esta práctica pero sugiere hacerlo con moderación y siempre que la legibilidad no se vea comprometida.

Consideraciones clave según PEP8:
    * Legibilidad: Lo más importante es que el código sea fácil de entender. Si declarar múltiples variables en una línea dificulta la comprensión, 
                   es mejor hacerlo en líneas separadas.
    * Relación entre variables: Si las variables están relacionadas (por ejemplo, coordenadas x e y), 
                   declararlas en la misma línea puede mejorar la legibilidad al enfatizar su relación.
    * Longitud de la línea: PEP8 recomienda que las líneas de código no superen los 79 caracteres. 
                   Si al declarar múltiples variables se excede este límite, es preferible dividirlas en líneas separadas.
                   
Ventajas:
    * Concisión: Puede hacer el código más compacto y fácil de leer cuando las variables están relacionadas.
    * Pythonic: Es una característica común en Python y se considera un estilo Pythonico.
Desventajas:
    * Legibilidad: Si se abusa de esta práctica, puede dificultar la comprensión del código.
    * Mantenimiento: Si se agregan o eliminan variables, puede ser más difícil realizar cambios en el código.
    
Aquí te presento algunos casos en los que esta práctica puede ser beneficiosa:

1. Variables estrechamente relacionadas:
    * Coordenadas: Cuando se trabaja con coordenadas (x, y) o (latitud, longitud), declararlas en una línea enfatiza su relación.
            Ejemplo: x, y = 10, 20
    * Dimensiones: Al definir las dimensiones de una figura (ancho, alto) o de un array (filas, columnas).
            Ejemplo: width, height = 800, 600
    * Valores por defecto: Al asignar valores por defecto a múltiples parámetros de una función.
            Ejemplo: x, y, z = 10, 20, 30
            
2. Desempaquetado de iterables:
    * Tuplas: Al asignar los elementos de una tupla a variables individuales.
            Ejemplo: name, age = ("Alice", 30)
    * Listas: Al asignar los primeros elementos de una lista a variables.
            Ejemplo: first, second = [1, 2]
    * Diccionarios: Al asignar las claves y valores de un diccionario a variables.
            Ejemplo: key, value = {"name": "Alice", "age": 30}

3. Intercambio de valores:
    * Swap: Para intercambiar los valores de dos variables de forma concisa.
            Ejemplo: 
                a, b = 5, 10
                a, b = b, a
                print(a)  # Salida: 10
                print(b)  # Salida: 5

4. Asignación múltiple con comprensión de listas:
    * Creación de listas: Para crear listas a partir de otras iterables de forma concisa.
    Ejemplo: squares = [x**2 for x in range(10)]
    
En resumen, la declaración múltiple de variables en una línea puede ser una herramienta útil para escribir código más conciso 
y expresivo, pero debe usarse con moderación y siempre teniendo en cuenta la legibilidad.
'''

# Coordenadas:
x, y = 10, 20
print(x, y) # Salida: 10 20

# Dimensiones:
width, height = 800, 600
print(width, height) # Salida: 800 600

# Valores por defecto:
x, y, z = 10, 20, 30
print(x, y, z) # Salida: 10 20 30

# Desempaquetado de tuplas:
name, age = ("Alice", 30)
print(name, age) # Salida: Alice 30

# Desempaquetado de listas:
first, second = [1, 2]
print(first, second) # Salida: 1 2

# Desempaquetado de diccionarios:
key, value = {"name": "Alice", "age": 30}
print(key, value) # Salida: name Alice

# Swap:
a, b = 5, 10
a, b = b, a
print(a) # Salida: 10
print(b) # Salida: 5

# Asignación múltiple con comprensión de listas:
squares = [x**2 for x in range(10)]
print(squares) # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


