"""
Funciones de Orden Superior (HOF - Higher Order Functions)
-------------------------------------------------------

Las funciones de orden superior son funciones que pueden:
1. Tomar otras funciones como argumentos
2. Retornar funciones como resultado
3. O ambas cosas

Características principales:
- Permiten la abstracción de acciones, no solo valores
- Facilitan la reutilización de código
- Permiten crear código más flexible y modular
- Son fundamentales en la programación funcional

Ejemplos comunes en Python:
1. map(): Aplica una función a cada elemento de un iterable
2. filter(): Filtra elementos según una función de predicado
3. reduce(): Reduce un iterable a un solo valor aplicando una función
4. sorted(): Ordena elementos usando una función key
5. decoradores: Modifican o aumentan el comportamiento de otras funciones
"""

# 1. Funciones que toman funciones como argumentos
print("\n1. Funciones que aceptan funciones:")


def apply_operation(func, value: float) -> float:
    """
    Aplica una función dada a un valor y retorna el resultado.

    Args:
        func (callable): Función a aplicar
        value: Valor sobre el cual se aplicará la función

    Returns:
        El resultado de aplicar la función al valor
    """
    result = func(value)  # Ejecuta la función y guarda el resultado
    return result  # Retorna el resultado


def square(x: float) -> float:
    """
    Eleva un número al cuadrado.

    Args:
        x (int/float): Número a elevar al cuadrado

    Returns:
        int/float: El cuadrado del número
    """
    return x ** 2


def double(x: float) -> float:
    """
    Duplica el valor de un número.

    Args:
        x (int/float): Número a duplicar

    Returns:
        int/float: El doble del número
    """
    return x * 2


def cube(x: float) -> float:
    """
    Eleva un número al cubo.

    Args:
        x (int/float): Número a elevar al cubo

    Returns:
        int/float: El cubo del número
    """
    return x ** 3


def half(x: float) -> float:
    """
    Divide un número entre 2.

    Args:
        x (int/float): Número a dividir

    Returns:
        float: La mitad del número
    """
    return x / 2


def absolute(x: float) -> float:
    """
    Retorna el valor absoluto de un número.

    Args:
        x (int/float): Número del cual obtener el valor absoluto

    Returns:
        int/float: El valor absoluto del número
    """
    return abs(x)


print(f"Cuadrado de 5: {apply_operation(square, 5)}")  # 25
print(f"Doble de 5: {apply_operation(double, 5)}")  # 10
print(f"Cubo de 5: {apply_operation(cube, 5)}")      # 125
print(f"La mitad de 5: {apply_operation(half, 5)}")      # 2.5
print(f"Valor absoluto de -5: {apply_operation(absolute, -5)}")  # 5

# 2. Funciones que retornan funciones
print("\n2. Funciones que retornan funciones:")


def create_multiplier(factor):
    """Crea una función que multiplica por un factor"""
    def multiplier(x):
        return x * factor
    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Doble de 10: {double(10)}")  # 20
print(f"Triple de 10: {triple(10)}")  # 30

# 3. Implementación personalizada de map
print("\n3. Implementación de map personalizado:")


def my_map(func, iterable):
    """Implementación propia de map()"""
    return [func(x) for x in iterable]


numbers = [1, 2, 3, 4, 5]
squared = my_map(square, numbers)
print(f"Lista Original: {numbers}")
print(f"Lista de Cuadrados: {squared}")

# 4. Implementación personalizada de filter
print("\n4. Implementación de filter personalizado:")


def my_filter(func, iterable):
    """Implementación propia de filter()"""
    return [x for x in iterable if func(x)]


def is_even(x):
    return x % 2 == 0


filtered = my_filter(is_even, numbers)
print(f"Numeros pares: {filtered}")

# 5. Composición de funciones
print("\n5. Composición de funciones:")


def compose(f, g):
    """Compone dos funciones: f(g(x))"""
    return lambda x: f(g(x))


def add_one(x):
    """Suma uno al valor dado"""
    return x + 1


square_then_add_one = compose(add_one, square)
add_one_then_square = compose(square, add_one)

print(f"Al cuadrado sumale 1: {square_then_add_one(5)}")  # 26
print(f"Sumale 1 y entonces el cuadrado: {add_one_then_square(5)}")  # 36

# 6. Decorador personalizado
print("\n6. Decorador personalizado:")


def timer_decorator(func):
    """Decorador que mide el tiempo de ejecución"""
    from time import time

    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timer_decorator
def slow_function():
    """Función que simula un proceso lento"""
    import time
    time.sleep(1)
    return "Done!"


print(slow_function())

# 7. Función de orden superior para validación
print("\n7. Validación con HOF:")


def validate_input(validator):
    """Crea una función que valida input según el validador dado"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if all(validator(arg) for arg in args):
                return func(*args, **kwargs)
            raise ValueError("Invalid input")
        return wrapper
    return decorator


def is_positive(x):
    return isinstance(x, (int, float)) and x > 0


@validate_input(is_positive)
def calculate_area(width, height):
    return width * height


try:
    print(f"Area (3, 4): {calculate_area(3, 4)}")
    print(f"Area (-1, 4): {calculate_area(-1, 4)}")
except ValueError as e:
    print(f"Error: {e}")

# 8. Currying (Transformar función de múltiples argumentos en secuencia de funciones)
print("\n8. Currying:")


def curry_function(func):
    """Implementa currying para una función de dos argumentos"""
    def curried(x):
        def inner(y):
            return func(x, y)
        return inner
    return curried


def add(x, y):
    return x + y


curried_add = curry_function(add)
add_five = curried_add(5)
print(f"Add five to 3: {add_five(3)}")  # 8

# 9. Pipeline de funciones
print("\n9. Pipeline de funciones:")


def create_pipeline(*funcs):
    """Crea un pipeline de funciones que se ejecutan en secuencia"""
    def pipeline(value):
        result = value
        for func in funcs:
            result = func(result)
        return result
    return pipeline


def add_two(x): return x + 2
def multiply_by_three(x): return x * 3
def subtract_one(x): return x - 1


pipeline = create_pipeline(add_two, multiply_by_three, subtract_one)
print(f"Pipeline result for 5: {pipeline(5)}")  # ((5 + 2) * 3) - 1 = 20

# 10. Memoización (Caché de resultados)
print("\n10. Memoización:")


def memoize(func):
    """Implementa memoización para una función"""
    cache = {}

    def memoized(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(f"Fibonacci(10): {fibonacci(10)}")
