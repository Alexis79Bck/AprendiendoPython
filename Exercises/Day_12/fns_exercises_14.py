import random
from functools import reduce
from collections import defaultdict
from datas import countries as COUNTRIES_NAMES, countries_data as COUNTRIES_DATA


def is_list(value) -> bool:
    """Verifica si valor es una lista.
    
    Args:
        value: La valor a verificar.
    Returns:
        Retorna True si el valor es una lista, en caso contrario retorna False
    """
    return isinstance(value, list)


def is_int_list(value) -> bool:
    """ Verifica si todos los elementos de una lista son números enteros.

    Args:
        value: La lista a verificar.
    Returns:
        Retorna True si todos los elementos son enteros, False en caso contrario.
    """
    return all(isinstance(item, int) for item in value)


def is_strings_list(value) -> bool:
    """ Verifica si todos los elementos de una lista son cadena de caracteres.

    Args:
        value: La valor a verificar.
    Returns:
        Retorna True si todos los elementos son strings, False en caso contrario.
    """
    return all(isinstance(item, str) for item in value)


def is_empty_string_list(value) -> bool:
    """Verifica si la lista de cadenas está vacía.
    
    Args:
        value: La value a verificar.
    Returns:
        Retorna True si esta vacía, False en caso contrario.
    """
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return not value
    return False


def print_item(item):
    """Imprimir por consola
    
    Args:
        item: Elemento a imprimir
    """
    print(item)


def change_to_uppercase(text: str) -> str:
    """Cambiar a mayuscula una cadena
    
    Args:
        text (str): Texto a cambiar
    Return:
        Texto a MAYUSCULA
    """
    return text.upper()


def square_of(num: int) -> int:
    """Elevar al cuadrado un numero
    
    Args:
        num (int): Numero a elevar al cuadrado
    Return:
        El cuadrado del numero
    """
    return num ** 2


def contain_landia(text: str) -> bool:
    """Contiena el texto landia
    
    Args:
        text (str): texto a comprobar
    Return:
        Retorna si contiene o no el texto 'landia'
    """
    return "landia" in text.lower()


def have_six_chars_exact(text: str) -> bool:
    """Tiene el texto 6 caracteres exactos
    
    Args:
        text (str): texto a comprobar
    Return:
        Retorna si tiene o no una longitud de 6 caracteres
    """
    return len(text) == 6


def have_six_or_more_chars(text: str) -> bool:
    """Tiene el texto 6 o mas caracteres
    
    Args:
        text (str): texto a comprobar
    Return:
        Retorna si tiene o no una longitud mayor o igual a 6
    """
    return len(text) >= 6


def start_with_letter_e(text: str) -> bool:
    """El texto empieza con la letra E
    
    Args:
        text (str): texto a comprobar
    Return:
        Retorna si empieza o no con la letra 'E'
    """
    return text.lower().startswith('e')


def square_on_odds_cube_on_even(num: int) -> int:
    """Cuadrado en numeros impares y cubo en numeros pares
    
    Args:
        num (int): Numero a Transformar
    Return:
        El Cuadrado del numero si es impar, El Cubo si es par
    """
    return num**2 if num % 2 != 0 else num**3


def only_cubes_even_numbers(x_cube: int, number: int) -> bool:
    """    Verifica si x_cube es el cubo de un número par.

    Args:
        x_cube (int): Resultado de elevar un número al cubo.

    Returns:
        bool: True si x_cube es el cubo de un número par, False en caso contrario.
    """

    # Calculamos la raíz cúbica y redondeamos al entero más cercano
    raiz_cubica = round(x_cube**(1/3))

    # Verificamos si es cubo perfecto
    if raiz_cubica**3 == x_cube and number % 2 == 0:
        return True

    return False


def unpacking_tuple(data: tuple):
    """Desempaquetando tupla
    Args:
        data (tuple): La tupla a deempaquetar
    """
    number, x_cube = data
    return only_cubes_even_numbers(x_cube, number)


def shuffling_list_and_select(*args: list, qty_items: int = 7) -> list:
    """Mezclar aleatoriamente los elementos de las listas
    
    Args:
        *args (list): Cantidad de listas a mezclar sus elementos
        qty_items (int): Cantidad de elementos a seleccionar, default = 7
    Return:
        Retorna una lista de 7 elementos seleccionados aleatoriamente
    """

    # Declarar una lista general y combinamos todas las listas de argumentos
    all_items = [element for the_list in args for element in the_list]

    # Mezclar aleatoriamente los elementos
    random.shuffle(all_items)

    # Seleccionar la cantidad de elementos especificada
    qty_items = min(qty_items, len(all_items))
    selected_items = all_items[:qty_items]

    return selected_items


def to_sum_numbers(data_list):
    """
    Funcion para reducir una lista de números.

    Args:
        data_list: La lista a reducir.

    Returns:
        Retorna la lista reducida o mensaje de error.
    """

    if is_list(data_list):
        if is_int_list(data_list):
            return  reduce(lambda x, y: x + y, data_list)

        return f"La lista {data_list} contiene al menos un elemento no entero."

    return f"{data_list} es un tipo de dato diferente. Se espera que sea una lista"



def combine_strings(data_list):
    """
    Funcion para combinar una lista de cadenas.

    Args:
        data_list: La lista a reducir.

    Returns:
        Retorna la lista reducida o mensaje de error.
    """

    if is_list(data_list):
        if is_strings_list(data_list):
            return reduce(lambda x, y: f"{x}, {y}", data_list)

        return f"La lista {data_list} contiene al menos un elemento que no es string."

    return f"{data_list} es un tipo de dato diferente. Se espera que sea una lista"


def pattern_contain(value, pattern: str) -> bool:
    """
    Verifica si un texto contiene un patrón.

    Args:
        texto (str): El texto a verificar.
        patron (str): El patrón a buscar.

    Returns:
        bool: True si el texto contiene el patrón, False en caso contrario.
    """
    return pattern in value


def key_gen_name():
    """Retorna funcion para ordenar por Nombre

    Returns:
        (callable): Retorna los elementos por nombre
    """
    return lambda item: item['name']

def key_gen_capital():
    """Retorna funcion para ordenar por Capital

    Returns:
        (callable): Retorna los elementos por Capital
    """
    return lambda item: item['capital']

def key_gen_population():
    """Retorna funcion para ordenar por total de Poblacion

    Returns:
        (callable): Retorna los elementos por total de Poblacion
    """
    return lambda item: item['population']


def _classify_by_language(data_list):
    """
    Clasifica una lista de países por idioma.

    Args:
        data_list (list): La lista de países.

    Returns:
        list: Una lista de diccionarios con los idiomas y sus frecuencias.
    """
    language_frequencies = defaultdict(int)
    for country in data_list:
        for language in country['languages']:
            language_frequencies[language] += 1

    ordered_languages = sorted(language_frequencies.items(), key=lambda item: item[1], reverse=True)
    return [{"language": lang, "frequency": freq} for lang, freq in ordered_languages]

def _classify_by_population(data_list):
    """
    Clasifica una lista de países por población.

    Args:
        data_list (list): La lista de países.

    Returns:
        list: Una lista de diccionarios con los países y sus poblaciones.
    """
    ordered_countries = sorted(data_list, key=lambda country: country['population'], reverse=True)
    return [{"name": country['name'], "population": country['population']} for country in ordered_countries]

def classify_by(data_list, classify_type):
    """
    Clasifica una lista por un tipo dado.

    Args:
        data_list (list): La lista a clasificar.
        classify_type (str): El tipo de clasificación ("Idioma" o "Poblacion").

    Returns:
        list: Una lista de diccionarios con los resultados de la clasificación.
    """
    if classify_type == "Idioma":
        return _classify_by_language(data_list)
    elif classify_type == "Poblacion":
        return _classify_by_population(data_list)
    else:
        return []  # Manejo de tipo de clasificación no válido


def print_countries_sorted_by(countries_list: list, sort_type: str):
    """Salida formateada para imprimir el ordenamiento de los paises

    Args:
        countries_list (list): lista de paises
        sort_by (str): tipo de ordenamiento
    """
    print(f"\nPaíses ordenados por {sort_type}:")
    for country in countries_list:
        print("País:")
        print(f"  Nombre: {country['name']}")
        print(f"  Capital: {country['capital']}")
        print(f"  Población: {country['population']}")
        print(".-"*60)
