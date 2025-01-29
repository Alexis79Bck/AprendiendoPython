'''

Estructuras Repetitivas en Python:

1. Bucle for:
   - Itera sobre una secuencia (lista, tupla, string, etc.)
   - Sintaxis: for elemento in secuencia:
   
2. Bucle while:
   - Repite mientras una condición sea verdadera
   - Sintaxis: while condicion:

3. Palabras reservadas de control:

   break:
   - Termina completamente el bucle
   - Sale inmediatamente de la estructura repetitiva
   - Se usa cuando queremos detener la iteración antes de su fin natural
   Ejemplo:
   for i in range(10):
       if i == 5:
           break  # Sale del bucle cuando i es 5
   
   continue:
   - Salta a la siguiente iteración del bucle
   - Ignora el resto del código dentro del bucle para esa iteración
   - Útil para saltar casos específicos sin romper el bucle
   Ejemplo:
   for i in range(5):
       if i == 2:
           continue  # Salta la iteración cuando i es 2
   
   pass:
   - No hace nada, es un marcador de posición
   - Se usa cuando se requiere sintácticamente una declaración
   - Útil como placeholder durante el desarrollo
   Ejemplo:
   for i in range(5):
       if i == 2:
           pass  # No hace nada, continúa con la siguiente línea
   
4. Uso común de estas palabras:
   - break: Para salir de bucles cuando se encuentra lo que se busca
   - continue: Para saltar casos que no nos interesan
   - pass: Para mantener la estructura del código cuando aún no se implementa la lógica
'''

# Ejemplo 1
counter = 0
end = 10

while counter < end:
    print(f'{counter} ')
    counter += 1
    
# Ejemplo 2
text_entered = input('Ingrese una palabra: ').lower()
texts_to_break = ['salir', 'cancelar', 'escapar', 'saltar', 'renunciar']
texts_to_ignore = ['camion', 'gandola', 'transporte', 'camioneta']

while text_entered not in texts_to_break:
    if text_entered in texts_to_ignore:
        print(f'La palabra {text_entered} es ignorada el bucle.')
    else:
        print(f'La palabra {text_entered} permite seguir ejecutando el bucle.')
    
    text_entered = input('Ingrese una nueva palabra: ').lower()
else:
    print(f'La palabra {text_entered} canceló el bucle.')
    
# Ejemplos prácticos
print("\nEjemplos de break, continue y pass:")

# Ejemplo de break
print("\n1. Usando break:")
for i in range(1, 6):
    if i == 4:
        break
    print(f"Número {i}")
print("Bucle terminado con break")

# Ejemplo de continue
print("\n2. Usando continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"Número {i}")
print("Bucle completado con continue")

# Ejemplo de pass
print("\n3. Usando pass:")
for i in range(1, 6):
    if i == 3:
        pass
    print(f"Número {i}")
print("Bucle completado con pass")

# Ejemplo combinado
print("\n4. Ejemplo combinado:")
for i in range(1, 10):
    if i == 3:
        continue  # Salta el 3
    if i == 7:
        break    # Termina en 7
    if i == 5:
        pass     # No hace nada especial con 5
    print(f"Número {i}")
print("Ejemplo combinado completado")

# Ejemplo 5: Búsqueda en lista con break
print("\n5. Search in list with break:")
numbers = [4, 8, 15, 16, 23, 42]
search_value = 16
for number in numbers:
    if number == search_value:
        print(f"Found! The number {search_value} is in the list")
        break
    print(f"Checking number {number}")

# Ejemplo 6: Filtrar números pares con continue
print("\n6. Filtrar números pares con continue:")
for i in range(1, 12):
    if i % 2 != 0:  # Si es impar
        continue
    print(f"Número par encontrado: {i}")

# Ejemplo 7: Validación de entrada con while
print("\n7. Validación de entrada con while:")
while True:
    edad = input("Ingrese su edad (0-120) o 'q' para salir: ")
    if edad.lower() == 'q':
        print("Programa terminado")
        break
    
    if not edad.isdigit():
        print("Por favor, ingrese un número válido")
        continue
        
    edad = int(edad)
    if 0 <= edad <= 120:
        print(f"Edad válida: {edad}")
        break
    else:
        print("La edad debe estar entre 0 y 120")

# Ejemplo 8: Procesamiento de lista con múltiples condiciones
print("\n8. List processing with multiple conditions:")
fruits = ['apple', 'banana', '', 'pear', None, 'orange', '']
print("Processing fruit list:")
for fruit in fruits:
    if fruit is None:
        print("Found null value, continuing...")
        continue
    if fruit == '':
        print("Found empty string, ignoring...")
        continue
    print(f"Processed fruit: {fruit}")

# Ejemplo 9: Menú interactivo con while
print("\n9. Menú interactivo:")
while True:
    print("\nMenú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '4':
        print("¡Hasta luego!")
        break
    elif opcion in ['1', '2', '3']:
        print(f"Seleccionó la opción {opcion}")
    else:
        print("Opción no válida, intente de nuevo")
        continue

# Ejemplo 10: Nested loops con break y continue
print("\n10. Nested loops (bucles anidados):")
for i in range(1, 4):
    print(f"\nTabla del {i}:")
    for j in range(1, 6):
        if i == 2 and j == 3:
            print("Saltando 2 x 3")
            continue
        if i == 3 and j == 4:
            print("Terminando tabla del 3")
            break
        print(f"{i} x {j} = {i*j}")

# Ejemplo 11: Procesamiento de diccionario
print("\n11. Dictionary processing:")
students = {
    'John': 85,
    'Anna': 92,
    'Peter': 78,
    'Mary': 95,
    'Louis': 70
}

print("Passing students (grade > 80):")
for name, grade in students.items():
    if grade <= 80:
        continue
    print(f"{name}: {grade}")

# Ejemplo 12: While con contador y break
print("\n12. While con contador y break:")
intentos_maximos = 3
contador = 0

while contador < intentos_maximos:
    respuesta = input("\n¿Cuál es la capital de Francia? ").lower()
    contador += 1
    
    if respuesta == 'paris':
        print("¡Correcto!")
        break
    
    intentos_restantes = intentos_maximos - contador
    if intentos_restantes > 0:
        print(f"Incorrecto. Te quedan {intentos_restantes} intentos")
    else:
        print("Se acabaron los intentos. La respuesta era Paris")

# Ejemplo 13: Filtrado y transformación con funciones nativas
print("\n13. Filtrado y transformación de datos:")
numeros = [1, -2, 3, -4, 5, -6, 7, -8, 9]

# Usando filter() y lambda para obtener números positivos
positivos = list(filter(lambda x: x > 0, numeros))
print("Números positivos:", positivos)

# Usando map() para duplicar valores
duplicados = list(map(lambda x: x * 2, numeros))
print("Números duplicados:", duplicados)

# Usando enumerate() para índices
for indice, valor in enumerate(numeros, 1):
    print(f"Posición {indice}: {valor}")

# Ejemplo 14: Procesamiento de strings
print("\n14. String processing:")
texts = ['  Python  ', 'JAVA', 'javascript   ', '  PHP  ']

for text in texts:
    # Skip empty strings after strip
    if not text.strip():
        continue
    
    # Process text: remove spaces and convert to title
    processed_text = text.strip().title()
    print(f"Original: '{text}' -> Processed: '{processed_text}'")

# Ejemplo 15: Manejo de iterables con zip()
print("\n15. Combining lists with zip():")
names = ['Anna', 'John', 'Mary']
ages = [25, 30, 35]
cities = ['Madrid', 'Barcelona', 'Valencia']

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# Ejemplo 16: Uso de any() y all()
print("\n16. Validations with any() and all():")
grades = [85, 90, 78, 92, 88]

# Check if all students passed (grade >= 70)
all_passed = all(grade >= 70 for grade in grades)
print(f"Did everyone pass? {all_passed}")

# Check if any student achieved excellence (grade >= 90)
any_excellence = any(grade >= 90 for grade in grades)
print(f"Any excellence? {any_excellence}")

# Ejemplo 17: Manejo de diccionarios con dict comprehension
print("\n17. Dictionary processing with comprehension:")
products = {'apple': 1.0, 'banana': 0.5, 'orange': 0.75, 'pear': 0.8}

# Apply 10% discount to products with price > 0.7
discounted_products = {
    name: round(price * 0.9, 2) 
    for name, price in products.items() 
    if price > 0.7
}
print("Products with discount:", discounted_products)

# Ejemplo 18: Uso de sorted() con key personalizada
print("\n18. Custom sorting:")
words = ['python', 'Java', 'JAVASCRIPT', 'PHP', 'Ruby']

# Sort ignoring case
sorted_words = sorted(words, key=str.lower)
print("Sorted ignoring case:", sorted_words)

# Sort by length
sorted_by_length = sorted(words, key=len)
print("Sorted by length:", sorted_by_length)

# Ejemplo 19: Manejo de excepciones en bucles
print("\n19. Exception handling in loops:")
values = ['1', '2', 'three', '4', '5.5', 'six']

valid_numbers = []
for value in values:
    try:
        number = float(value)
        valid_numbers.append(number)
    except ValueError:
        print(f"Non-numeric value found: {value}")
        continue

print("Valid numbers processed:", valid_numbers)

# Ejemplo 20: Generador con yield
print("\n20. Uso de generador:")
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("Secuencia Fibonacci hasta 50:")
for num in fibonacci(50):
    print(num, end=' ')
print()  # Nueva línea al final