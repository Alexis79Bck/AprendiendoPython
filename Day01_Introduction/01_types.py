'''
Ejemplos de tipos de datos en Python y asignación de valores a variables.

En Python, los tipos de datos más comunes son:
- Entero (int)
- Flotante (float)
- Cadena de texto (str)
- Booleano (bool)
- Lista (list)
- Tupla (tuple)
- Conjunto (set)
- Diccionario (dict)

Usando la funcion print() se pueden imprimir los valores, variables y tipos de datos.
'''


# Entero (int): Los números enteros no tienen decimales
numero_entero = 10  
print("Entero (int):", 10) # Imprime valor directamente
print("Entero (int) usando variable:", numero_entero) # Imprime el valor de la variable numero_entero
print("Mostrando el tipo de dato de la variable:", type(numero_entero)) # Muestra el tipo de dato

# Flotante (float): Los números flotantes se definen con un punto decimal
numero_flotante = 10.5 
print("Flotante (float):", 10.5) # Imprime el valor directamente
print("Flotante (float) usando variable:", numero_flotante) # Imprime el valor de la variable numero_flotante
print("Mostrando el tipo de dato de la variable:", type(numero_flotante)) # Muestra el tipo de dato

# Cadena de texto (str): Las cadenas de texto se pueden definir con comillas dobles o simples
cadena_texto = "Hola, mundo de python" 
print("Cadena de texto (str):", "Hola, mundo de python") # Imprime la cadena de texto "Hola, mundo"
print("Cadena de texto (str) usando variable:", cadena_texto)   # Imprime el valor de la variable cadena_texto
print("Mostrando el tipo de dato de la variable:", type(cadena_texto)) # Muestra el tipo de dato

# Booleano (bool): Los valores booleanos son True (verdadero) y False (falso)
es_verdadero = True
print("Booleano (bool):", True) # Imprime el valor directamente
print("Booleano (bool) usando variable:", es_verdadero) # Imprime el valor de la variable es_verdadero 
print("Mostrando el tipo de dato de la variable:", type(es_verdadero)) # Muestra el tipo de dato

# Lista (list): Las listas son colecciones ordenadas y mutables de elementos
lista_numeros = [1, 2, 3, 4, 5]
print("Lista (list):", [1, 2, 3, 4, 5]) # Imprime la lista de números
print("Lista (list) usando variable:", lista_numeros)   # Imprime el valor de la variable lista_numeros
print("Mostrando el tipo de dato de la variable:", type(lista_numeros)) # Muestra el tipo de dato

# Tupla (tuple): Las tuplas son colecciones ordenadas e inmutables de elementos
tupla_numeros = (1, 2, 3, 4, 5)
print("Tupla (tuple):", (1, 2, 3, 4, 5)) # Imprime la tupla de números
print("Tupla (tuple) usando variable:", tupla_numeros)  # Imprime el valor de la variable tupla_numeros
print("Mostrando el tipo de dato de la variable:", type(tupla_numeros)) # Muestra el tipo de dato

# Conjunto (set): Los conjuntos son colecciones no ordenadas de elementos únicos
conjunto_numeros = {1, 2, 3, 4, 5}
print("Conjunto (set):", {1, 2, 3, 4, 5}) # Imprime el conjunto de números
print("Conjunto (set) usando variable:", conjunto_numeros) # Imprime el valor de la variable conjunto_numeros
print("Mostrando el tipo de dato de la variable:", type(conjunto_numeros)) # Muestra el tipo de dato

# Diccionario (dict): Los diccionarios son colecciones no ordenadas de pares clave-valor
diccionario = {"nombre": "Juan", "edad": 30}
print("Diccionario (dict):", {"nombre": "Juan", "edad": 30}) # Imprime el diccionario
print("Diccionario (dict) usando variable:", diccionario) # Imprime el valor de la variable diccionario
print("Mostrando el tipo de dato de la variable:", type(diccionario)) # Muestra el tipo de dato
