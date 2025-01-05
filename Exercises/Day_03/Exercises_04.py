'''
1.- Concatena la cadena 'Aprendiendo', 'Python', 'Desde', 'Cero' en una sola cadena, 'Aprendiendo Python Desde Cero'.
2.- Concatenar la cadena 'Tutoriales', 'En', 'Videos' en una sola cadena, 'Tutoriales En Videos'.
3.- Declara una variable llamada sentence1 y asígnele un valor inicial "Tutoriales en videos". Realice:
    3.1.- Imprima su valor.
    3.2.- Imprima la longitud.
    3.3.- Cambie todos los caracteres a letras mayúsculas.
    3.4.- Cambie todos los caracteres a letras minúsculas.
    3.5.- Formatee el valor de la variable a Capital, Titulo y Alternar mayusculas y minusculas.
4.- Recortar (cortar) la primera palabra de la cadena "Aprendiendo python desde cero".
5.- Compruebe si en la cadena "Aprendiendo python desde cero" contiene la palabra "videos".
6.- Reemplace la palabra "typescript" por "python" en la cadena 'Aprendiendo typescript desde cero'.
7.- Divida la cadena "Aprendiendo python desde cero" usando el espacio como separador.
8.- "Java, C#, JavaScript, PHP, TypeScript, Python, Rust" divide la cadena en la coma.
9.- Declara una variable llamada sentence2 y asígnele un valor inicial "Aprendiendo Python Desde Cero". Realice:
    9.1.- ¿Cuál es el carácter en el primer posición?
    9.2.- ¿Cuál es el caracter en el último posición?.
    9.3.- ¿Qué carácter se encuentra en la posicion 10?
    9.4.- Utilice el índice para determinar la posición de la primera aparición de 'C'.
    9.5.- Utilice el índice para determinar la posición de la primera aparición de 'n'.
    9.6.- Utilice rfind() para determinar la posición de la última aparición de 'd'.
    9.7.- Utilice index() o find() para encontrar la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'
    9.8.- Utilice rindex() o rfind() para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'
    9.9.- Elimina la frase 'porque porque porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'
10.- Comprueba en la variable sentence2:
    10.1.- ¿Comienza con la subcadena 'Aprendiendo'?
    10.2.- ¿Termina con la subcadena 'Aprendiendo' ?
    10.3.- ¿Si solo contiene caracteres Alfanumerico?
    10.4.- ¿Si solo contiene letras?
    10.5.- ¿Si está en mayúscula?
11.- La siguiente lista contiene los nombres de algunas bibliotecas de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
    Únase a la lista con un hash con una cadena de espacios.
12.- Utilice la secuencia de escape de nueva línea para separar las siguientes oraciones.
      
            I am enjoying this challenge.
            I just wonder what is next.
            
13.- Utilice una secuencia de escape de tabulación para escribir las siguientes líneas.
            
            Name      Age      Country   City
            Asabeneh1   25     Finland   Helsinki
            Asabeneh2   23     Finland   Helsinki
            Asabeneh3   27     Finland   Helsinki

14.- Utilice el método de formato de cadena para mostrar lo siguiente:
        radius = 10
        area = 3.14 * radius ** 2
        The area of a circle with radius 10 is 314 meters square.
'''

# 1.-
word1, word2, word3, word4 = 'Aprendiendo ', 'Python ', 'Desde ', 'Cero.'
sentence = word1 + word2 + word3 + word4
print(f"Palabras a concatenar: {word1}, {word2}, {word3}, {word4}")
print(f"Oracion creada: {sentence}")
print("\n")

#2.-
word1, word2, word3 = 'Tutoriales ', 'En ', 'Video '
sentence1 = word1 + word2 + word3
print(f"Palabras a concatenar: {word1}, {word2}, {word3}")
print(f"Oracion creada: {sentence}")
print("\n")

#3.1.-
print(f'El valor de la variable sentence1: {sentence1}')

#3.2.-
print(f'La longitud de la variable sentence1: {len(sentence1)}')

#3.3.-
print(f'Cambiar las letras a mayusculas: {sentence1.upper()}')

#3.4.-
print(f'Cambiar las letras a minusculas: {sentence1.lower()}')

#3.5.-
print(f'Capitalizar la oracion: {sentence1.capitalize()}')
print(f'Titulizar la oracion: {sentence1.title()}')
print(f'Alternar mayusculas y minusculas en la oracion: {sentence1.swapcase()}')
print("\n")

#4.-
print(f'La oracion es: {sentence}', )
print(f'La primera palabra de la oracion es: {sentence[0:11]}')
print("\n")

#5.-
videos_word_exist_in_sentence = "videos" in sentence
print(f"Comprobando si la sub-cadena 'videos' existe en la oracion 'Aprendiendo python desde cero': {videos_word_exist_in_sentence}")
print('\n')

#6.- 
string_before_replacement = "Aprendiendo typescript desde cero"
replacing_typescript_with_python = string_before_replacement.replace('typescript', 'python')
print(f'Oracion antes del reemplazo: {string_before_replacement}')
print(f"Oracion reemplazando 'typescript' con 'python': {replacing_typescript_with_python}")
print('\n')

#7.-
string_before_splitting = "Aprendiendo python desde cero"
split_words = string_before_splitting.split(' ')
print(f'Oracion antes de la división: {string_before_splitting}')
print(f"Palabras obtenidas despues de la división: {split_words}")
print('\n')

#8.-
words_in_a_string = "Java, C#, JavaScript, PHP, TypeScript, Python, Rust"
words_after_split = words_in_a_string.split(', ')
print(f"Palabras antes de la división: {words_in_a_string}")
print(f"Palabras obtenidas despues de la división: {words_after_split}")
print('\n')

#9.-
sentence2 = "Aprendiendo Python desde Cero"
print(f'La oracion: {sentence2}')

#9.1.-
print(f'El caracter en la primera posicion es: {sentence2[0]}')

#9.2.-
print(f'El caracter en la última posicion es: {sentence2[-1]}')

#9.3.-
print(f'El caracter en la posicion 10 es: {sentence2[10]}')

#9.4.-
print(f'La primera aparición del caracter "C" es en la posicion: {sentence2.index('C')}')

#9.5.-
print(f'La primera aparición del caracter "n" es en la posicion: {sentence2.index('n')}')

#9.6.-
print(f'La ultima aparición del caracter "d" es en la posicion: {sentence2.rfind('d')}')
print('\n')

sentence = 'No puedes terminar una oración con porque porque porque es una conjunción'
print(f'La oración es: {sentence}')

#9.7.-
print(f'La primera aparición de la palabra "porque" es en la posicion: {sentence.find('porque')}')

#9.8.-
print(f'La última aparición de la palabra "porque" es en la posicion: {sentence.rfind('porque')}')

#9.9.-
print(f'La frase "porque porque porque" ha sido eliminada: {sentence.replace('porque','')}')
print('\n')

#10.-
print(f'La oración es: {sentence2}')

#10.1.- 
print(f'Comprobando si la oración comienza con "Aprendiendo": {sentence2.startswith('Aprendiendo')}')

#10.2.- 
print(f'Comprobando si la oración termina con "Aprendiendo": {sentence2.endswith('Aprendiendo')}')

#10.3.- 
print(f'Comprobando si solo contiene caracteres alfanumericos: {sentence2.isalnum()}')

#10.4.- 
print(f'Comprobando si solo contiene caracteres letras: {sentence2.isalpha()}')

#10.5.- 
print(f'Comprobando si está en mayusculas: {sentence2.isupper()}')
print('\n')

#11.-
python_libs_names = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
names_joins_with_hash = " # ".join(python_libs_names)
print(f'Resultado de la union de la lista es: {names_joins_with_hash}')
print('\n')

#12.-
first_sentence =  'Estoy alegre con estos ejercicios.'
second_sentence = 'Me emociona conocer que contenido sigue.'
print(f'{first_sentence}\n{second_sentence}')
print('\n')

#13.- 
print("Name\t\tAge\t\tCountry\t\tCity")
print("====\t\t===\t\t=======\t\t====")
print("Asabeneh1\t25\t\Finland\t\t\Helsinki")
print("Asabeneh2\t23\t\Finland\t\Helsinki")
print("Asabeneh3\t27\t\Finland\t\t\Helsinki")
print("\n")

#14.-
radius = 10
area = 3.14 * radius ** 2
print('El área de un circulo con el rado de {}cm es {}cm cuadrados.'.format(radius, area))