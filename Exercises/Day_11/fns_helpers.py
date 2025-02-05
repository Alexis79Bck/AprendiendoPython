"""fns_helpers.py
Este módulo contiene funciones y utilidades para el archivo principal exercises_13.py. 

incluye:
- Diccionarios con fórmulas y nombres de figuras geométricas.
- Funciones para validar la entrada del usuario.
- Funciones para solicitar los parámetros de las figuras geométricas.
- Funciones lambda para calcular el área de las figuras geométricas.
"""

from math import pi, tan

# Diccionario de formulas de figuras geométricas
FIGURES_FORMULA = {
    "Círculo": "Área = π * r^2",
    "Triángulo": "Área = (b * h) / 2",
    "Cuadrado": "Área = l^2",
    "Trapecio": "Área = ((B + b) * h) / 2",
    "Rombo": "Área = (D * d) / 2",
    "Rectángulo": "Área = l * a",
    "Paralelogramo": "Área = b * h",
    "Pentágono": "Área = (5 * l * a) / 2",
    "Hexágono": "Área = (3 * l^2 * √3) / 2",
    "Heptágono": "Área = (7 * l^2 * (1/tan(π/7))) / 4"
}

# Diccionario de nombres de figuras geométricas para el menú
FIGURES_NAMES = {
    1: "Círculo",
    2: "Triángulo",
    3: "Cuadrado",
    4: "Trapecio",
    5: "Rombo",
    6: "Rectángulo",
    7: "Paralelogramo",
    8: "Pentágono",
    9: "Hexágono",
    10: "Heptágono"
}

# Diccionario de funciones lambda para áreas de figuras geométricas
LAMBDA_FUNCTIONS = {
    "Círculo": lambda radius: pi * radius**2,
    "Triángulo": lambda base, height: (base * height) / 2,
    "Cuadrado": lambda side: side**2,
    "Trapecio": lambda major_base, minor_base, height: ((major_base + minor_base) * height) / 2,
    "Rombo": lambda major_diagonal, minor_diagonal: (major_diagonal * minor_diagonal) / 2,
    "Rectángulo": lambda length, width: length * width,
    "Paralelogramo": lambda base, height: base * height,
    "Pentágono": lambda side, apothem: (5 * side * apothem) / 2,
    # 3**0.5 es la raíz cuadrada de 3
    "Hexágono": lambda side: (3 * side**2 * 3**0.5) / 2,
    # pi, tan: Se debe importar el modulo math
    "Heptágono": lambda side: (7 * side**2 * (1/tan(pi/7))) / 4
}


# Funciones definidas
def calculate_figure_area(figure, *params):
    """Calcula el área de una figura geométrica.
    Args:
        figure: str: Nombre de la figura geométrica
        *params: tuple: Parámetros necesarios para calcular el área
    Returns:
        float: Área de la figura
    """
    calculator = LAMBDA_FUNCTIONS[figure]  # Acceso directo a la función
    return calculator(*params)


def get_figure_formula(figure: str):
    """Obtener la fórmula de una figura geométrica
    Args:
        figure: str: Nombre de la figura geométrica"""
    return FIGURES_FORMULA.get(figure)


def input_name_surname() -> tuple:
    """Solicitar el nombre y apellido del usuario"""
    name = input("Ingrese su nombre: ")
    surname = input("Ingrese su apellido: ")
    return name, surname


def concatenate_names_surnames_in_string_list(names_surnames: list) -> list:
    """Concatenar nombres y apellidos en una lista de cadenas"""
    return [f"{name} {surname}" for name, surname in names_surnames]


def validate_int_input(input_message: str) -> int:
    """Validar un valor entero positivo ingresado por el usuario."""
    while True:
        value_str = input(input_message)  # Leer la entrada como cadena
        try:
            value = int(value_str)  # Intentar convertir a entero
            if value < 0:
                print("Debe ingresar un valor positivo.")
                continue  # Volver a pedir el valor si es negativo
            return value  # Retornar el entero si es válido
        except ValueError:
            print("Debe ingresar un valor entero positivo.")


def validate_option_selected(input_message: str) -> int:
    """Validar una opción seleccionada por el usuario."""
    while True:
        value = validate_int_input(input_message)
        if 0 <= value <= 10:
            return value
        print("Debe seleccionar una opción válida (0-10).")


# Funciones para solicitar los valores de las figuras geométricas
def input_values_x_y() -> tuple:
    """Solicitar los valores de x y y"""
    x = validate_int_input("Ingrese el valor de x: ")
    y = validate_int_input("Ingrese el valor de y: ")
    return x, y


def input_circle_params() -> int:
    """Solicitar el parametro del circulo"""
    radius = validate_int_input("Ingrese el radio: ")
    return radius


def input_triangle_params() -> tuple:
    """Solicitar los parametros base y altura"""
    base = validate_int_input("Ingrese la base: ")
    height = validate_int_input("Ingrese la altura: ")
    return base, height


def input_rectangle_params() -> tuple:
    """Solicitar los parametros ancho y largo"""
    width = validate_int_input("Ingrese el ancho: ")
    lenght = validate_int_input("Ingrese el largo: ")
    return width, lenght


def input_square_params() -> int:
    """Solicitar los parametros lado"""
    side = validate_int_input("Ingrese el lado: ")
    return side


def input_trapezoid_params() -> tuple:
    """Solicitar los parametros base mayor, base menor y altura"""
    major_base = validate_int_input("Ingrese la base mayor: ")
    minor_base = validate_int_input("Ingrese la base menor: ")
    height = validate_int_input("Ingrese la altura: ")
    return major_base, minor_base, height


def input_rhombus_params() -> tuple:
    """Solicitar los parametros diagonal mayor, diagonal menor"""
    major_diagonal = validate_int_input("Ingrese la diagonal mayor: ")
    minor_diagonal = validate_int_input("Ingrese la diagonal menor: ")
    return major_diagonal, minor_diagonal


def input_parallelogram_params() -> tuple:
    """Solicitar los parametros base y altura"""
    base = validate_int_input("Ingrese la base: ")
    height = validate_int_input("Ingrese la altura: ")
    return base, height


def input_pentagon_params() -> tuple:
    """Solicitar los parametros lado y apotema"""
    side = validate_int_input("Ingrese el lado: ")
    apothem = validate_int_input("Ingrese el apotema: ")
    return side, apothem


def input_hexagon_params() -> int:
    """Solicitar los parametros lado"""
    side = validate_int_input("Ingrese el lado: ")
    return side


def input_heptagon_params() -> int:
    """Solicitar los parametros lado"""
    side = validate_int_input("Ingrese el lado: ")
    return side


def select_option() -> int:
    """Solicitar que seleccione una opcion del menu"""
    option_selected = validate_option_selected("Debe seleccionar una opción válida.")
    return option_selected
