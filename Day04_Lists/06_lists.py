'''
Para declarar e inicializar una lista, se puede hacer de 2 maneras:
1.- Usando la funcion list(). Ejemplo:
    - empty_list = list()
    - first_5_numbers = list((1, 2, 3, 4, 5))
Nota: list() no acepta múltiples argumentos directamente, se puede pasar un objeto 
itereable (cadenas, tuplas, diccionarios) a lista.
    
2.- Utilizando los corchetes(brackets). Ejemplo:
    - empty_list = []
    - colors_list = ['roja', 'azul', 'amarillo', 'negro', 'blanco']
    - even_numbers = [2, 4, 6, 8, 10]
    
Se recomienda por legibilidad, si desea inicializar una variable del tipo lista
y esta inicialmente es vacia, utilizar []. La funcion list() permite la conversion de 
tipo de datos a lista, aun cuando por si solo y sin argumentos inicializa la variable 
como lista.

Una lista no solo puede contener un conjunto de elementos de un mismo tipo, puede tambien 
componerse de elementos de diferentes tipos de datos. Por ejemplo:
    - user_info = ['Johnny', 'Doe', 35, 1.79, 84.65, True, 'j.doe@example.com']
'''

# Ejemplo 1: Usando la función list()
empty_list = list()
print("Lista vacía:", empty_list)

# Para crear una lista a partir de un valor iterable
first_5_numbers = list((1, 2, 3, 4, 5)) #Pasando una tupla a lista
print("Primeros 5 números:", first_5_numbers)

hello_world_chars_list = list("Hello World") #Pasando una cadena a lista
print("Lista de caracteres de Hello World:", hello_world_chars_list)

# Ejemplo 2: Usando corchetes []
empty_list = []
print("Lista vacía:", empty_list)

colors_list = ['roja', 'azul', 'amarillo', 'negro', 'blanco']
print("Lista de colores:", colors_list)

even_numbers = [2, 4, 6, 8, 10]
print("Números pares:", even_numbers)

# Lista con diferentes tipos de datos
user_info = ['Johnny', 'Doe', 35, 1.79, 84.65, True, 'j.doe@example.com']
print('Datos de Usuario:', user_info)

'''
Accesos a los elementos de una lista.
Para acceder a los elementos de una lista, como es bien sabido, se usa un indice.
El indice es el indicador para localizar el elemento y se representa de la siguiente manera:
    - fruits_list = ['mango', 'naranja', 'manzana', 'limon', 'pera']
                  ->    0         1          2         3        4    <-
      print(fruits_list[1]) #'naranja'
      print(fruits_list[4]) #'pera'
      print(fruits_list[2]) #'manzana'
      print(fruits_list[0]) #'mango'
        
Toda lista inicia su indice a partir del valor 0

Tambien se puede localizar un elemento de una lista, de forma reversa usando valores negativos en 
el indice, a partir de -1:

    print(fruits_list[-1]) #'pera'
    print(fruits_list[-4]) #'naranja'
    print(fruits_list[-2]) #'limon'
    
'''

# Ejemplo de acceso a elementos de una lista
fruits_list = ['mango', 'naranja', 'manzana', 'limon', 'pera']

# Acceso con índices positivos
print("\nAcceso con índices positivos:")
print("fruits_list[1] ->", fruits_list[1])  # 'naranja'
print("fruits_list[4] ->", fruits_list[4])  # 'pera'
print("fruits_list[2] ->", fruits_list[2])  # 'manzana'
print("fruits_list[0] ->", fruits_list[0])  # 'mango'

# Acceso con índices negativos
print("\nAcceso con índices negativos:")
print("fruits_list[-1] ->", fruits_list[-1])  # 'pera'
print("fruits_list[-4] ->", fruits_list[-4])  # 'naranja'
print("fruits_list[-2] ->", fruits_list[-2])  # 'limon'

'''
Desempaquetando una lista:

Desempaquetar se refiere pasar los elementos de una lista a un conjunto de variables,
para almacenarlo de forma independiente y tratarlo de manera atomica.

Seguiremos con el ejemplo de lista fruits_list.

fruit_one, fruit_two, fruit_three, fruit_four, fruit_five = fruits_list
print('Fruta 1:', fruit_one)
print('Fruta 2:', fruit_two)
print('Fruta 3:', fruit_three)
print('Fruta 4:', fruit_four)
print('Fruta 5:', fruit_five)

Aspectos a destacar antes de utilizar el desempaquetado:
    - Número de variables: El número de variables en el lado izquierdo de la asignación 
                           debe coincidir con el número de elementos en la lista.
    - Orden: Los elementos de la lista se asignan a las variables en el mismo orden.
    - Desempaquetado parcial: Se puede utilizar el operador * para desempaquetar un número variable 
                           de elementos en una lista.
    - Manejo de excepciones: Si la lista tiene menos elementos que las variables, se producirá un error. 
                           Se puede agregar un bloque try-except para manejar esta situación.
'''

# Desempaquetando fruits_list
print("\nDesempaquetando la lista fruit_list:")
fruit_one, fruit_two, fruit_three, fruit_four, fruit_five = fruits_list
print('Fruta 1:', fruit_one)
print('Fruta 2:', fruit_two)
print('Fruta 3:', fruit_three)
print('Fruta 4:', fruit_four)
print('Fruta 5:', fruit_five)

print("\nDesempaquetando la lista user_info:")
first_name, last_name, age, height, weight, is_active, email = user_info
print('Nombre:', first_name)
print('Apellido:', last_name)
print('Edad:', age)
print('Estatura (m):', height)
print('Peso (Kg):', weight)
print('Esta Activo:', is_active)
print('Email:', email)

'''
Operaciones con listas:

1. Verificar longitud de una lista:
   - Usando la función len() podemos obtener el número de elementos en una lista
   
2. Concatenar listas:
   - Usando el operador + podemos unir dos o más listas
   - También se puede usar el método extend()
   
3. Agregar elementos:
   - append(): Agrega un elemento al final de la lista
   - insert(): Agrega un elemento en una posición específica
   
4. Eliminar elementos:
   - remove(): Elimina la primera ocurrencia de un elemento específico
   - pop(): Elimina y retorna el último elemento (o el elemento en el índice especificado)
   - del: Elimina un elemento o un rango de elementos usando índices
   - clear(): Elimina todos los elementos de la lista
   
5. Buscar elementos:
   - index(): Encuentra el índice de la primera ocurrencia de un elemento
   - count(): Cuenta cuántas veces aparece un elemento en la lista
   - in: Verifica si un elemento existe en la lista
   
6. Ordenar elementos:
   - sort(): Ordena la lista en orden ascendente (modifica la lista original)
   - reverse(): Invierte el orden de los elementos
   - sorted(): Retorna una nueva lista ordenada (no modifica la original)
'''

print("\nOperaciones con listas:")
print("=======================")
# 1. Verificar longitud
numbers = [1, 2, 3, 4, 5]
print("\nLongitud de la lista:", len(numbers))  # 5

# 2. Concatenar listas
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print("\nListas concatenadas:", concatenated)  # [1, 2, 3, 4, 5, 6]

list1.extend(list2)
print("Lista extendida:", list1)  # [1, 2, 3, 4, 5, 6]

# 3. Agregar elementos
fruits = ['manzana', 'banana']
fruits.append('naranja')
print("\nDespués de append:", fruits)  # ['manzana', 'banana', 'naranja']

fruits.insert(1, 'uva')
print("Después de insert:", fruits)  # ['manzana', 'uva', 'banana', 'naranja']

# 4. Eliminar elementos
colors = ['rojo', 'azul', 'verde', 'amarillo', 'azul']
colors.remove('azul')  # Elimina la primera ocurrencia de 'azul'
print("\nDespués de remove:", colors)

last_color = colors.pop()  # Elimina y retorna el último elemento
print("Elemento eliminado:", last_color)
print("Lista después de pop:", colors)

del colors[0]  # Elimina el primer elemento
print("Después de del:", colors)

colors.clear()  # Elimina todos los elementos
print("Después de clear:", colors)

# 5. Buscar elementos
numbers = [1, 2, 3, 2, 4, 2, 5]
print("\nÍndice del primer 2:", numbers.index(2))  # 1
print("Cantidad de 2 en la lista:", numbers.count(2))  # 3
print("¿Está el 3 en la lista?", 3 in numbers)  # True

# 6. Ordenar elementos
unsorted = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("\nLista original:", unsorted)

# Ordenar la lista original
unsorted.sort()
print("Lista ordenada (sort):", unsorted)

# Invertir la lista
unsorted.reverse()
print("Lista invertida (reverse):", unsorted)

# Crear nueva lista ordenada
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
print("Nueva lista ordenada (sorted):", sorted_numbers)
print("Lista original sin cambios:", numbers)

'''
Otras operaciones con listas:

1. Slicing (Rebanado):
   - lista[inicio:fin:paso] -> Obtiene una sublista desde inicio hasta fin-1, con un paso opcional
   - Se pueden usar índices negativos
   - Si se omite inicio, comienza desde el principio
   - Si se omite fin, llega hasta el final
   
2. Copiar listas:
   - copy(): Crea una copia superficial de la lista
   - list(): Crea una nueva lista
   - slicing [:]: Crea una copia de toda la lista
   
3. Comprensión de listas (List Comprehension):
   - Forma concisa de crear listas basadas en listas existentes
   - Sintaxis: [expresion for elemento in iterable if condicion]
   
4. Operaciones matemáticas:
   - sum(): Suma todos los elementos numéricos
   - max(): Encuentra el valor máximo
   - min(): Encuentra el valor mínimo
   
5. Modificación múltiple:
   - Multiplicar lista: Repite los elementos
   - Asignación múltiple: Cambia varios elementos a la vez
'''

print("\nOtras operaciones con listas:")
print("=============================")

# 1. Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nLista original:", numbers)
print("Primeros 3 elementos:", numbers[:3])  # [0, 1, 2]
print("Últimos 3 elementos:", numbers[-3:])  # [7, 8, 9]
print("Del segundo al quinto:", numbers[1:5])  # [1, 2, 3, 4]
print("Elementos pares:", numbers[::2])  # [0, 2, 4, 6, 8]
print("Lista invertida:", numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 2. Copiar listas
original = [1, 2, 3]
copy_1 = original.copy()
copy_2 = list(original)
copy_3 = original[:]

print("\nCopias de listas:")
print("Original:", original)
print("Copia 1:", copy_1)
print("Copia 2:", copy_2)
print("Copia 3:", copy_3)

# 3. Comprensión de listas
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # Cuadrados de los números
even_numbers = [x for x in numbers if x % 2 == 0]  # Solo números pares

print("\nComprensión de listas:")
print("Números originales:", numbers)
print("Cuadrados:", squares)
print("Números pares:", even_numbers)

# 4. Operaciones matemáticas
numeric_list = [10, 5, 8, 3, 1, 9, 4]
print("\nOperaciones matemáticas:")
print("Lista:", numeric_list)
print("Suma total:", sum(numeric_list))
print("Valor máximo:", max(numeric_list))
print("Valor mínimo:", min(numeric_list))

# 5. Modificación múltiple
simple_list = [1, 2, 3]
print("\nModificación múltiple:")
print("Lista original:", simple_list)
print("Lista multiplicada por 3:", simple_list * 3)

# Cambiar múltiples elementos
numbers = [0, 0, 0, 0, 0]
numbers[1:4] = [1, 2, 3]  # Cambia elementos del índice 1 al 3
print("Lista después de modificación múltiple:", numbers)

