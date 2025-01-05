
"""
Los tipos de datos strings en Python son secuencias de caracteres que se utilizan para representar texto. 
Se pueden declarar y asignar a una variable utilizando comillas simples (' ') o comillas dobles (" ").

Ejemplo de declaración y asignación:
    texto = 'Hola, mundo'
    otro_texto = "Python es genial"
    
Tambien es posible utilizar comillas triples (''' ''') o (""" """) para declarar strings de varias líneas.
Ejemplo:
    texto = '''Este es un string
    que ocupa varias líneas
    y se puede escribir en varias líneas'''

Funciones básicas nativas para trabajar con strings:
    - len(cadena): Devuelve la longitud de la cadena.
    - cadena.lower(): Convierte todos los caracteres de la cadena a minúsculas.
    - cadena.upper(): Convierte todos los caracteres de la cadena a mayúsculas.
    - cadena.strip(): Elimina los espacios en blanco al principio y al final de la cadena.
    - cadena.replace(viejo, nuevo): Reemplaza todas las ocurrencias de una subcadena por otra.
    - cadena.split(separador): Divide la cadena en una lista de subcadenas utilizando el separador especificado.
    - cadena.find(subcadena): Devuelve el índice de la primera aparición de la subcadena, o -1 si no se encuentra.
    - cadena.join(iterable): Une los elementos de un iterable en una sola cadena, separados por la cadena original.
"""

# Declaración y asignación de strings
texto = 'Hola, mundo'
otro_texto = "Python es genial"
multilinea = '''Este es un string   
que ocupa varias líneas
y se puede escribir en varias líneas'''

# Imprimir los strings
print(texto)
print(otro_texto)
print(multilinea)
print("\n")

# Concatecación de strings
saludo = 'Hola, '
nombre = 'Juan'
mensaje = saludo + nombre
print(mensaje)
print("\n")

# Secuencia de Escape
'''
Las secuencias de escape son caracteres especiales que se utilizan para representar caracteres no imprimibles o especiales.
Algunas de las secuencias de escape más comunes son:
  - \n: Nueva línea
  - \t: Tabulación
  - \': Comilla simple
  - \": Comilla doble
  - \\: Barra invertida
'''

print('Este es un string con una secuencia de escape: \nNueva línea')
print('Este es un string con una secuencia de escape: \tTabulación')
print('Este es un string con una secuencia de escape: \'Comilla simple')
print('Este es un string con una secuencia de escape: \"Comilla doble')
print('Este es un string con una secuencia de escape: \\Barra invertida')
print("\n")

# Lista de alumnos creado con secuencias de escape
print("\nListado de Alumnos:")
print("======= == =======:\n")
print("ID\t\tNombres\t\tApellidos\t\tEdad")
print("==\t\t=======\t\t=========\t\t====")
print("JP7B20IF\tJuan\t\tPérez\t\t\t20")
print("MG7B21IF\tMaría\t\tGonzález\t\t21")
print("CL7B22IF\tCarlos\t\tLópez\t\t\t22")
print("AM7B23IF\tAna\t\tMartínez\t\t23")
print("LG7B24IF\tLuis\t\tGarcía\t\t\t24")
print("ER7B25IF\tElena\t\tRodríguez\t\t25\n")
print("\n")

# Formatear strings
'''
Python permite formatear strings utilizando el método format() o el operador %.
El método format() permite reemplazar los valores de las llaves {} en una cadena por los valores de las variables.
El operador % permite formatear una cadena utilizando especificadores de formato.

Como programador se debe tener en cuenta que el uso de format() es más recomendado que el operador %, ya que es más flexible y legible.
Ademas que el orden de los argumentos no importa en el método format(). Debido al uso de las llaves {} y los placeholders
para identificar los valores a reemplazar.

A partir de Python 3.6, se puede utilizar f-strings para formatear strings de una manera más sencilla y legible.
esto es conocido Interpolación de strings. 

La interpolación de strings es una forma de formatear strings que permite insertar valores de variables directamente en la cadena.
Para utilizar f-strings, se debe anteponer la letra f al inicio de la cadena y utilizar llaves {} para insertar los valores de las variables.

'''

# Método format()
mensaje = 'Hola, {nombre} {apellido} tienes {edad} años'.format(nombre='Juan', edad=20, apellido='Pérez')
print('Usando metodo format():', mensaje)

# Operador %
mensaje = 'Hola, %s %s tienes %d años' % ('Juan', 'Perez', 20)
print('Usando el operador % :', mensaje)

# F-strings
nombre = 'Juan'
apellido = 'Pérez'
edad = 20
mensaje = f'Hola, {nombre} {apellido} tienes {edad} años'
print('Usando la interpolacion f-string:', mensaje)

print("\n")

'''
Los strings en Python son una secuencia de caracteres, por lo que se pueden acceder a los caracteres individuales utilizando índices.
Los índices en Python comienzan en 0, por lo que el primer carácter de un string tiene un índice de 0, el segundo tiene un índice de 1, y así sucesivamente.

Por tal flexibilidad y debido a que python trata a los datos de strings como un objeto. Se puede desempaquetar, acceder a los elementos e iterar
como si fuera una lista.
'''

# Acceder a los caracteres de un string
sentence = 'Python es un lenguaje de aplicacion general'
print('Accediendo al elemento en la posición 8:', sentence[8]) # Imprime 's'
print('Accediendo al elemento en la posición 3 desde el final:',sentence[-3]) # Imprime 'a', el tercer caracter desde el final
print("\n")

# Desempaquetar un string
a, b, c, d, e, f = 'Python' 
print(a) # Imprime 'P'
print(b) # Imprime 'y'
print(c) # Imprime 't'
print(d) # Imprime 'h'
print(e) # Imprime 'o'
print(f) # Imprime 'n'
print("\n")

# Iterar sobre un string
for letra in 'Python':
    print(letra)
print("\n")
    
# Longitud de un string
print('Cantidad de caracteres en la palabra "Python":', len('Python')) # Imprime 6
print('\n')

# Rebanar (Slicing) un string
'''
El slicing es una técnica que se utiliza para obtener una subcadena de un string.
Para realizar un slicing, se debe especificar el índice de inicio, el índice de fin y el paso, separados por dos puntos (:).
El índice de inicio es inclusivo, mientras que el índice de fin es exclusivo.
'''

sentence = 'Python es un lenguaje de aplicacion general'
print('Imprimiendo los primeros 6 caracteres:', sentence[:6]) # Imprime 'Python'
print('Imprimiendo los caracteres de la posición 7 a la 14:', sentence[7:14]) # Imprime 'es un l'
print('Imprimiendo los últimos 6 caracteres:', sentence[-6:]) # Imprime 'general'

# Reverso (Reversing) de un string
print('Reverso de la cadena:', sentence[::-1]) # Imprime 'laraneg noicacilpa ed ejeugnal nu se nohtyP'

# Cortar con pasos (Step) un string
print('Imprimiendo los caracteres de la posición 0 a la 10 con un paso de 2:', sentence[0:15:2]) # Imprime 'Pto su e'
print("\n")


# Metodos de strings

## lower() y upper(): Convertir a minúsculas y mayúsculas
sentence = 'PytHon ES un leNgUajE de ApLicACion GeNEral'
print('Oracion:', sentence)
print('Cadena en minúsculas:', sentence.lower())
print('Cadena en mayúsculas:', sentence.upper())
print("\n")

## strip(): Eliminar espacios en blanco al principio y al final
sentence = '   Python es un lenguaje de aplicacion general   '
print('Oracion:', sentence)
print('Cadena sin espacios en blanco:', sentence.strip())
print("\n")

## replace(): Reemplazar una subcadena por otra
sentence = 'Python es un lenguaje de aplicacion general'
print('Oracion:', sentence)
print('Reemplazando "Python" por "Java":', sentence.replace('Python', 'Java'))
print("\n")

## split(): Dividir la cadena en una lista de subcadenas
sentence = 'Python es un lenguaje de aplicacion general'
print('Oracion:', sentence)
print('Dividiendo la oración en palabras:', sentence.split(' '))
print("\n")

## find():  Encontrar la posición de una subcadena
sentence = 'Python es un lenguaje de aplicacion general'
print('Oracion:', sentence)
print('Indice de la palabra "lenguaje":', sentence.find('lenguaje'))
print("\n")

## join(): Unir los elementos de una lista en una cadena
words = ['Python', 'es', 'un', 'lenguaje', 'de', 'aplicacion', 'general']
sentence = ' '.join(words)
print('Lista de palabras:', words)
print('Uniendo las palabras en una oración:', sentence)
print("\n")

## count(): Contar el número de ocurrencias de una subcadena
sentence = 'Python es un lenguaje de aplicacion general'
print('Oracion:', sentence)
print('Número de veces que aparece la palabra "Python":', sentence.count('Python'))
print("\n")

## startswith() y endswith(): Verificar si una cadena comienza o termina con una subcadena
sentence = 'Python es un lenguaje de aplicacion general'
print('Oracion:', sentence)
print('La oración comienza con "Python":', sentence.startswith('Python'))
print('La oración comienza con "lenguaje":', sentence.startswith('lenguaje'))
print('La oración termina con "general":', sentence.endswith('general'))
print('La oración termina con "de":', sentence.endswith('de'))
print("\n")

## isdigit() y isalpha(): Verificar si la cadena contiene solo dígitos o solo letras
number, word = '12345',  'Python'
print('La cadena "12345" contiene solo dígitos:', number.isdigit())
print('La cadena "Python" contiene solo letras:', word.isalpha())

## islower() y isupper(): Verificar si la cadena contiene solo minúsculas o solo mayúsculas
lower_word, upper_word = 'python', 'PYTHON'
print('La cadena "python" contiene solo minúsculas:', lower_word.islower())
print('La cadena "PYTHON" contiene solo mayúsculas:', upper_word.isupper())

## isalnum() y isalpha(): Verificar si la cadena contiene solo caracteres alfanuméricos o solo letras
alpha = 'Python123'
letters = 'Python'
print('La cadena "Python123" contiene solo caracteres alfanuméricos:', alpha.isalnum())
print('La cadena "Python" contiene solo letras:', letters.isalpha())

## isnumeric() y isdecimal(): Verificar si la cadena contiene solo caracteres numéricos o solo dígitos decimales
number = '12345'
decimal = '12.345'
print('La cadena "12345" contiene solo caracteres numéricos:', number.isnumeric())
print('La cadena "12.345" contiene solo dígitos decimales:', decimal.isdecimal())

## isidentifier(): Verificar si la cadena es un identificador válido
text_id = 'Python'
print('La cadena "Python" es un identificador válido:', text_id.isidentifier())

## isspace(): Verificar si la cadena contiene solo espacios en blanco
spaces = '   '
print('La cadena "   " contiene solo espacios en blanco:', spaces.isspace())

## capitalize(): Convertir la primera letra de la cadena a mayúscula
sentence = 'python es un lenguaje de aplicacion general'
print('Oracion:', sentence)
print('Oración con la primera letra en mayúscula:', sentence.capitalize())

## title(): Convertir la primera letra de cada palabra a mayúscula
sentence = 'python es un lenguaje de aplicacion general'
print('Oracion:', sentence)
print('Oración con la primera letra de cada palabra en mayúscula:', sentence.title())

## swapcase(): Convertir las letras minúsculas en mayúsculas y viceversa
sentence = 'Python es un lenguaje de aplicacion general'
print('Oracion:', sentence)
print('Oración con las letras en mayúsculas y minúsculas intercambiadas:', sentence.swapcase())