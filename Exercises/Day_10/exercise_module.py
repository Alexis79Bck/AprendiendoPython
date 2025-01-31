"""
exercise_module.py: Contendra todas las funciones solicitadas que son necesarias
para cumplir con los ejercicios propuestos en el archivo: exercises_12.py
"""

import random
import string


def list_of_alpha_charaters() -> str:
    """Listado de Caracteres alfanumericos"""
    return string.ascii_letters + string.digits  # Manera recomendada
    # Forma convencional
    # return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def random_number_between_0_255() -> int:
    """Genera un numero entre 0 y 255 aleatoriamente

    return:
        int: Un numero aleatorio entre 0 y 255
    """
    return random.randint(0, 255)


def list_generated_by_user_input(qty_of_items: int) -> list:
    """Genera una lista de items, con una cantidad dada por el usuario.

    Args:
        qty_of_items (int): Cantidad de elementos que tendrá la lista

    Returns:
        list: Lista de items generada
    """

    list_generated = []

    for n in range(qty_of_items):
        item_input = input(
            f"Ingrese el elemento {n + 1}. a la lista (texto o numero): ")
        list_generated.append(item_input)

    return list_generated


def get_quantity(message: str) -> int:
    """Obtener una entrada entera válida."""

    while True:
        try:
            quantity = int(
                input(f"{message} "))
            break
        except ValueError:
            print("Por favor, ingrese un numero entero")
            continue
    return int(quantity)


def select_colors_format() -> str:
    """Entrada del usuario para seleccionar el tipo de formato de colores."""

    format_color_list = ["hex", "rgb"]

    while True:
        color_code = input("Selecione (hex o rgb): ")
        if color_code in format_color_list:
            return color_code.lower()
        else:
            print("Por favor, ingrese un formato válido. Debe ser 'hex' o 'rgb'")

    
def user_id_random() -> str:
    """Genera aleatoriamente un id de usuario de 6 caracteres alfanumericos.

    Returns:
        str: Id de 6 caracteres alfanumericos generado aleatoriamente
    """

    # Caracteres alfanumericos
    characters = list_of_alpha_charaters()

    # Generar un id de usuario de 6 caracteres alfanumericos
    user_id = "".join(random.choices(characters, k=6))

    return user_id


def user_id_gen_by_user() -> list[str]:
    """Genera un id de usuario de acuerdo a la cantidad de caracteres y la cantidad de ids
    que se supone que se generarán.

    Returns:
        str: El id de usuario generado
    """

    # Solicitar al usuario la cantidad de caracteres
    qty_char = get_quantity("Ingrese la cantidad de caracteres: ")
    while True:
        try:
            if qty_char <= 0:
                print("Debe ingresar un número positivo.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    # Solicitar al usuario la cantidad de ids que se desea generar
    qty_ids_to_gen = get_quantity("Ingrese la cantidad de ids que desea generar: ")
    while True:
        try:
            if qty_ids_to_gen <= 0:
                print("Debe ingresar un número positivo.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    # Caracteres alfanumericos
    characters = list_of_alpha_charaters()

    user_ids_list = ["".join(random.choices(characters, k=int(qty_char)))
                     for _ in range(int(qty_ids_to_gen))]
    # Generar un id de usuario de acuerdo a la cantidad de caracteres y la cantidad de ids

    return user_ids_list


def rgb_color_gen() -> str:
    """Genera un color RGB aleatorio, a partir de 3 números aleatorios entre 0 y 255.

    Returns:
        str: Color RGB Aleatorio
    """
    # Generar 3 números aleatorios entre 0 y 255
    r, g, b = random_number_between_0_255(
    ), random_number_between_0_255(), random_number_between_0_255()

    return f"rgb({r}, {g}, {b})"


def shuffle_list(list_to_shuffle: list) -> list:
    """Devuelve una lista aleatoria a partir de una lista dada.

    Args:
        list_to_shuffle (list): Lista a ser mezclada

    Returns:
        list: Lista mezclada
    """
    return random.sample(list_to_shuffle, len(list_to_shuffle))


def list_of_seven_unique_random_numbers() -> list:
    """Genera una lista de siete números aleatorios únicos en un rango de 0 a 9.

    Returns:
        list: Lista de siete números aleatorios únicos
    """
    return random.sample(range(10), 7)


def generate_hex_color():
    """Genera un color hexadecimal aleatorio."""
    return "#" + ''.join(random.choices(string.hexdigits, k=6))


def list_of_hexa_colors(num_colors):
    """Genera una lista de colores hexadecimales aleatorios.

    Args:
        num_colors (int): Número de colores a generar.

    Returns:
        list: Una lista de cadenas, cada una representando un color hexadecimal.
    """
    return [generate_hex_color() for _ in range(num_colors)]


def generate_rgb_color():
    """Genera un color RGB aleatorio en una tupla (R, G, B)."""
    return rgb_color_gen()


def list_of_rgb_colors(num_colors):
    """Genera una lista de colores RGB aleatorios.

    Args:
        num_colors (int): Número de colores a generar.

    Returns:
        list: Una lista de tuplas, cada una representando un color RGB.
    """
    return [generate_rgb_color() for _ in range(num_colors)]


def generate_colors(num_colors, color_format='hex'):
    """Genera una lista de colores aleatorios en el formato especificado.

    Args:
        num_colors (int): Número de colores a generar.
        color_format (str): Formato de los colores ('hex' o 'rgb').

    Returns:
        list: Una lista de colores en el formato especificado.
    """
    if color_format == 'hex':
        return list_of_hexa_colors(num_colors)
    else:
        return list_of_rgb_colors(num_colors)
