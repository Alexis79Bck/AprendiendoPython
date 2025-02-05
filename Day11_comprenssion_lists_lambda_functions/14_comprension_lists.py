"""
Compresion de Listas

La comprensión de listas es una forma concisa y elegante de crear 
listas en Python. Permite generar una nueva lista aplicando una 
expresión a cada elemento de una secuencia existente (como otra lista, 
tupla, rango, etc.) y, opcionalmente, filtrando elementos que cumplan
una condición.

Sintaxis:
    [<expresión> for <elemento> in <iterable> <[if condición]>]
    
    <expresión>: Operación que se aplicará a cada elemento.
    <elemento>: Variable que representa cada elemento en el iterable.
    <iterable>: Secuencia de elementos o funcion generadora.
    <[if condición]>: Condición opcional que se debe cumplir para determinar
                      si un elemento se incluye en la nueva lista.
                      
Ejemplo:
    numbers = [1, 2, 3, 4, 5]
    squares = [number ** 2 for number in numbers]
    
    print(f"Lista de números: {numbers}")
    print(f"Lista de cuadrados: {squares}")
    
El uso de las comprensiones de lista:
    - Simplifica la escritura de código.
    - Transformar la lista a una nueva aplicando una operación a cada elemento.
    - Filtrar listas que cumplan una condición específica.
    - Hace que el código sea más legible.
    - Combinar listas en una nueva efectuando una combinancion elementos de dos o más listas.
    - Reduce la cantidad de líneas de código.
    - Mejora el rendimiento.

Dónde implementarlas
La comprensión de listas se puede utilizar en cualquier lugar donde necesites 
crear una nueva lista basada en una secuencia existente. Algunos ejemplos comunes incluyen:
    - Procesamiento de datos: Manipular datos de una lista para realizar cálculos, 
                              transformaciones o análisis.
    - Filtrado de información: Seleccionar elementos específicos de una lista que 
                              cumplan ciertos criterios.
    - Generación de nuevas listas: Crear listas basadas en datos existentes 
                              de forma rápida y sencilla.    

Relación con buenas prácticas y principios
La comprensión de listas se alinea con varias buenas prácticas y 
principios de programación:

    - DRY (No te repitas): La comprensión de listas evita la necesidad de escribir 
              bucles for repetitivos para realizar operaciones en listas, lo que 
              reduce la duplicación de código.
    - KISS (Mantenlo simple, estúpido): La sintaxis concisa de la comprensión de listas 
              hace que el código sea más legible y fácil de entender en comparación 
              con los bucles for tradicionales.
    - SOLID (Principios de diseño de software): Si bien la comprensión de listas no se 
              relaciona directamente con todos los principios SOLID, su uso adecuado 
              puede contribuir a un código más limpio y modular, lo que facilita el 
              mantenimiento y la extensión del software.
"""

import statistics
import random


def calculate_statistics(x, y, z):
    """
    Calcula estadísticas descriptivas para un punto tridimensional.
    Retorna un diccionario con los resultados.
    """
    mean = statistics.mean([x, y, z])
    standard_deviation = statistics.stdev([x, y, z]) if len(
        set([x, y, z])) > 1 else 0  # Manejo de la excepción
    return {"mean": mean, "standard_deviation": standard_deviation}


def create_full_name(name: str, surename: str) -> str:
    """crea un nombre completo a partir de un nombre y un apellido.

    Args:
        name (str): Parametro de nombre
        surename (str): Parametro de apellido

    Returns:
        str: Retorna el nombre completo
    """
    return f"{name} {surename}"


numbers = list(range(1, 20))
print(f"Mi lista de números del 1 al 20: {numbers}")
print("\n")

# Obtener lista de cuadrados a partir de la lista de números
squares = [number ** 2 for number in numbers]
print(f"Lista de cuadrado de numeros ({numbers}) es: {squares}")
print("\n")

# Filtrar números impares de la lista de números
odd_numbers = [number for number in numbers if number % 2 != 0]
print(f"Lista de números impares de la lista ({numbers}) es: {odd_numbers}")

# Filtrar números pares de la lista de números
even_numbers = [number for number in numbers if number % 2 == 0]
print(f"Lista de números pares de la lista ({numbers}) es: {even_numbers}")

# Combinar elementos de dos listas
names = ["Alice", "Bob", "Charlie", "Joe", "Billy"]
surenames = ["Smith", "Johnson", "Williams", "Brown", "Davis"]
full_names = [create_full_name(name, surename)
              for name in names for surename in surenames]

print(f"Lista de nombres: {names}")
print(f"Lista de apellidos: {surenames}")
print(f"Lista de nombres completos: {full_names}")

print("\n")

# Crear una lista de estadisticas

# Datos de ejemplo aleatorios entre 10 y 100 con 5 pasos
x_values = [random.randint(-25, 25) for _ in range(random.randint(1, 5))]
y_values = [random.randint(-25, 25) for _ in range(random.randint(1, 5))]
z_values = [random.randint(-25, 25) for _ in range(random.randint(1, 5))]

# Comprensión de lista para producto cartesiano tridimensional
cartesian_product_results = [
    (x, y, z)
    for x in x_values
    for y in y_values
    for z in z_values
]

# Calcular estadísticas para cada punto tridimensional
statistics_results = [
    calculate_statistics(x, y, z)
    for x, y, z in cartesian_product_results
]

print(f"Resultado final Producto Cartesiano: {cartesian_product_results}")
print(f"Resultado final Calculo de Estadisticas: {statistics_results}")
