'''
FUNCIONES EN PYTHON

1. Definición y Conceptos Básicos:
   - Una función es un bloque de código reutilizable que realiza una tarea específica
   - Se define usando la palabra clave 'def'
   - Puede recibir parámetros y retornar valores
   - Promueve la reutilización de código y el principio DRY (Don't Repeat Yourself)

2. Sintaxis Básica:
   def function_name(parameter1, parameter2, ...):
       """Docstring: Descripción de la función"""
       # Cuerpo de la función
       return value  # Opcional

3. Tipos de Parámetros:
   a) Parámetros posicionales (obligatorios)
   b) Parámetros con valores por defecto
   c) Parámetros de tipo *args (número variable de argumentos posicionales)
   d) Parámetros de tipo **kwargs (número variable de argumentos con nombre)

4. Alcance de Variables (Scope):
   - Variables locales: Definidas dentro de la función
   - Variables globales: Definidas fuera de la función
   - Palabra clave 'global': Para modificar variables globales dentro de funciones

5. Valores de Retorno:
   - return: Devuelve un valor y termina la función
   - Puede retornar múltiples valores (como tupla)
   - Si no hay return, devuelve None

6. Documentación:
   - Docstrings: Documentación de la función
   - Help: Obtener ayuda sobre la función
'''


# 1. Función Básica
def greet(name):
    """Saludo simple"""
    return f"Hola Usuario, {name}!"


print("\n1. Función Básica:")
print(greet("Alice"))


# 2. Función con Parámetros por Defecto
def power(base, exponent=2):
    """
    Calcular la potencia de un Número.

    Args:
        base: la base
        exponent: el exponente (predeterminado es 2)

    Returns:
        El resultado es la base elevado al exponente
    """
    return base**exponent


print("\n2. Función con Parámetros por defecto:")
print(f"2^3 = {power(2, 3)}")
print(f"3^2 = {power(3)}")  # Using default exponent


# 3. Función con *args
def sum_all(*args):
    """Sumar todos los numeros del argumento"""
    return sum(args)


print("\n3. Función con *Argumentos:")
print(f"Sumar 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sumar 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")


# 4. Función con **kwargs
# Es util cuando se trabaje con diccionario, par clave-valor
def print_info(**kwargs):
    """
    Mostrar la informacíon de una Persona.
    **kwargs: significa keywords args, traducido como argumentos con nombres
    """
    for key, value in kwargs.items():
        print(f"{key.title()}: {value}")


print("\n4. Función con **Argumentos con nombres:")
print_info(name="John", age=30, city="New York")


# 5. Función con Múltiples Valores de Retorno
def get_statistics(numbers):
    """Calcula las Estadisticas basica de un conjunto de numeros"""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


print("\n5. Función con múltiples retornos de valores:")
numbers = [1, 2, 3, 4, 5]
# Desempaqueta el resultado de la funcion asignandolo a las variables correspondientes
minimum, maximum, average = get_statistics(numbers)
print(f"Min: {minimum}, Max: {maximum}, Average: {average}")

# 6. Función con Variable Local y Global
global_var = 10


def modify_global():
    """Modificación de una variable global"""
    global global_var
    global_var = 20
    local_var = 30
    print(f"Inside function - Global: {global_var}, Local: {local_var}")


print("\n6. Funcion con Variables Globales y Locales:")
print(f"Before function - Global: {global_var}")
modify_global()
print(f"After function - Global: {global_var}")

# 7. Función Lambda (función anónima)
print("\n7. Función Lambda:")
def square(x): return x**2  # noqa: E731


print(f"Square of 5: {square(5)}")


# 8. Función como Parámetro (Higher-Order Function)
def apply_operation(func, value):
    """Aplicar una funcion a un valor"""
    return func(value)


print("\n8. Función como Parámetro:")
print(f"Square of 6: {apply_operation(square, 6)}")
print(f"Absolute of -7: {apply_operation(abs, -7)}")


# 9. Función con Type Hints (Python 3.5+)
def calculate_price(quantity: int, price: float, discount: float = 0.0) -> float:
    """
    Calcula el precio total con descuento.

    Args:
        quantity: Numero de articulos
        price: Precio por articulos
        discount: Porcentaje de descuento (0-1)

    Returns:
        Precio total despues del descuento
    """
    total = quantity * price
    return total * (1 - discount)


print("\n9. Funcion con Sugerencia de Tipos:")
print(f"Total: ${calculate_price(5, 10.0, 0.1):.2f}")


# 10. Función Recursiva
def factorial(n: int) -> int:
    """El factorial de un número mediante función recursiva"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print("\n10. Funcion Recursiva:")
while True:
    number_entered = input("Ingrese un numero entre 5 y 50: ")
    if number_entered.isdigit():
        number_entered = int(number_entered)
        if 5 <= number_entered <= 50:
            break
        else:
            print("Debe ingresar un número entre 5 y 50.")
    else:
        print("Debe ingresar un número entre 5 y 50.")

print(f"El Factorial del número {number_entered}: {factorial(number_entered)}")


# 11. Función Decoradora
def uppercase_decorator(func):
    """Decorador que convierte el resultado en MAYUSCULAS"""

    def wrapper(*args):
        original_result = func(*args)
        return original_result.upper()

    return wrapper


@uppercase_decorator
def greetings(name):
    """Retorna un Saludo Simple"""
    return f"hello, {name}!"


print("\n11. Funcion decorador:")
full_name = "john doe"
print(greetings(full_name))


# 12. Función Generadora
def fibonacci_generator(limit):
    """Generar la secuencia de fibonacci hasta un valor limite"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


print("\n12. Funcion generadora:")
while True:
    number_entered = input("Ingrese un numero entre 5 y 100: ")
    if number_entered.isdigit():
        number_entered = int(number_entered)
        if 5 <= number_entered <= 100:
            break
        else:
            print("Debe ingresar un número entre 5 y 100.")
    else:
        print("Dato inválido. El valor introducido no es un número.")

print(f"Secuencia de Fibonacci hasta el número {number_entered}:")
for num in fibonacci_generator(number_entered):
    print(num, end=" ")

print()
