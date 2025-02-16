"""
Ejercicios de Comprensiones de Listas y Funciones Lambda:

1.- Filtrar solo los negativos y ceros en la lista usando la comprensión de listas
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

2.- Crea una lista plana unidimensional a partir siguiente lista de listas de listas:
    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
3.- Usando la comprensión de listas, crea la siguiente lista de tuplas:
    [(0, 1, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), (2, 1, 2, 4, 8, 16, 32),
     (3, 1, 3, 9, 27, 81, 243), (4, 1, 4, 16, 64, 256, 1024), (5, 1, 5, 25, 125, 625, 3125),
     (6, 1, 6, 36, 216, 1296, 7776), (7, 1, 7, 49, 343, 2401, 16807), 
     (8, 1, 8, 64, 512, 4096, 32768), (9, 1, 9, 81, 729, 6561, 59049), 
     (10, 1, 10, 100, 1000, 10000, 100000)]
     
4.- Aplanar la siguiente lista para formar una nueva lista:
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    # Salida: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], 
               ['NORWAY', 'NOR', 'OSLO']]
    
5.- Cambie la siguiente lista a una lista de diccionarios:
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    # Salida: [{'country': 'FINLAND', 'city': 'HELSINKI'}, 
    #          {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
               {'country': 'NORWAY', 'city': 'OSLO'}]
               
6.- Usando comprension de listas, cambie la siguiente lista de listas a una lista de 
cadenas concatenadas, teniendo en cuenta que se debe crear una funcion que permita capturar 
el nombre y el apellido desde el teclado y retornar una lista de listas. 
Debe ser creado en un módulo llamado fns_helpers.py:
    Ejemplo:
        names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], 
                 [('Bill', 'Gates')]]
        # Salida: ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
        
7.- Escriba una función lambda que pueda resolver una pendiente o una intersección con 
el eje y de funciones lineales.

8.- Escriba una función lambda que pueda resolver el área de un triángulo.

9.- Escriba una función lambda que pueda resolver el área de un rectángulo.

10.- Escriba una función lambda que pueda resolver el área de un círculo.

11.- Escriba una función lambda como parte funcion de orden superior y que pueda resolver 
el área de una figura geométrica. Ten en cuenta que las unicas que se permiten son:
    - Círculo
    - Triángulo
    - Cuadrado
    - Trapecio
    - Rombo
    - Rectángulo
    - Paralelogramo
    - Pentágono
    - Hexágono
    - Heptágono

El usuario debe escoger una figura, al seleccionar la figura, se debe mostrar la fórmula 
para calcular el área y luego solicitar los valores necesarios para calcular el área.

Recuerda crear las formulas en el módulo fns_helpers.py y luego importarlas en el script.

"""
import fns_helpers as helpers

def calculate_area():
    """Función principal para calcular áreas de las figuras."""

    while True:
        # Mostrar menú
        print("\nSeleccione una figura geométrica:")
        for key, value in helpers.OPTIONS_MENU.items():
            print(f"{key}. {value}")
        print("0. Salir")

        # Obtener opción del usuario
        selected_option = helpers.select_option()

        # Salir si el usuario elige 0
        if selected_option == 0:
            break

        # Obtener figura y fórmula
        figure_selected = helpers.OPTIONS_MENU[selected_option]
        figure_name = helpers.FIGURES_NAMES[selected_option]
        formula = helpers.get_figure_formula(figure_selected)

        # Mostrar fórmula
        print(f"\nFórmula: {formula}")

        # Obtener parámetros (usando getattr para hacerlo dinámico)
        # --Construye el nombre de la función dinamicamente
        input_function_name = f"input_{figure_name.lower()}_params"
        input_function = getattr(helpers, input_function_name)
        params = input_function()

        # Calcular área (usando la función genérica)
        area = helpers.calculate_figure_area(figure_selected, *params)

        # Mostrar resultado
        print(f"El área del {figure_selected.lower()} es: {area}")
    input()

# 1.-
print("\n1.- Filtrar solo los negativos y ceros en la lista usando la comprensión de listas")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [num for num in numbers if num <= 0]
print(f"El resultado del filtro es: {filtered}")

# 2.-
print("\n2.- Crea una lista plana unidimensional a partir siguiente lista de listas de listas:")
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatted_list = [num for sublist in list_of_lists for sub_sublist in sublist for num in sub_sublist]
print(f"La lista plana es: {flatted_list}")

# 3.-
print("\n3.- Usando la comprensión de listas, crea la siguiente lista de tuplas:")
tuples_list = [(num, 1, num, num**2, num**3, num**4, num**5) for num in range(11)]
print(f"La lista de tuplas es: {tuples_list}")

# 4.-
print("\n4.- Aplanar la siguiente lista para formar una nueva lista:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatted_countries = [[country.upper(), country[:3].upper(), city.upper()]
                     for sublist in countries
                     for country, city in sublist]
print(f"La lista aplanada es: {flatted_countries}")

# 5.-
print("\n5.- Cambie la siguiente lista a una lista de diccionarios:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{"country": country.upper(), "city": city.upper()}
                  for sublist in countries
                  for country, city in sublist]
print(f"La lista de diccionarios es: {dict_countries}")

# 6.-
print("""\n6.- Usando comprension de listas, cambie la siguiente lista de listas a
      una lista de cadenas concatenadas.""")

names_and_surnames = []
while True:
    # Se emplea el helper input_name_surename para la interaccion con el usuario
    name, surname = helpers.input_name_surname()
    names_and_surnames.append((name, surname))

    user_resp = input("¿Desea continuar ingresando (S/N)? ").lower()
    while user_resp not in ('s', 'n'):
        print("Error: Ingrese 'S' o 'N'.")
        user_resp = input("¿Desea continuar ingresando (S/N)? ").lower()

    if user_resp.lower() != 's':  # Si la respuesta no es 's', termina el bucle principal
        break

print(f"""La lista de nombres y apellidos es:
      {helpers.concatenate_names_surnames_in_string_list(names_and_surnames)}""")

# 7.-
print("""\n7.- Escriba una función lambda que pueda resolver una pendiente
      o una intersección con el eje y de funciones lineales.""")

print("Ingrese los valores del primer punto (x1, y1): ")
x1, y1 = helpers.input_values_x_y()
print("Ingrese los valores del segundo punto (x2, y2): ")
x2, y2 = helpers.input_values_x_y()

calculate_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

the_slope = calculate_slope(x1, y1, x2, y2)

print(f"La pendiente de la recta es: {the_slope}")

# 8.-
print("\n8.- Escriba una función lambda que pueda resolver el área de un triángulo.")

while True:
    try:
        triangle_base, triangle_height = helpers.input_triangle_params()

        # Validar que la base y la altura sean positivas
        if triangle_base <= 0 or triangle_height <= 0:
            raise ValueError("La base y/o la altura deben ser valores positivos.")

        # Usa la función lambda importada
        area = helpers.LAMBDA_FUNCTIONS["Triángulo"](triangle_base, triangle_height)

        print(f"El área del triángulo es: {area}")
        break  # Salir del bucle si no hay errores
    except ValueError as e:
        print(f"Error: {e}")


# 9.-
print("\n9.- Escriba una función lambda que pueda resolver el área de un rectángulo.")

while True:
    try:
        rectangle_width, rectangle_lenght = helpers.input_rectangle_params()

        # Validar que la base y la altura sean positivas
        if rectangle_width <= 0 or rectangle_lenght <= 0:
            raise ValueError("El ancho y/o el largo deben ser valores positivos.")

        # Usa la función lambda importada
        area = helpers.LAMBDA_FUNCTIONS["Rectángulo"](rectangle_lenght, rectangle_width)

        print(f"El área del rectángulo es: {area}")
        break  # Salir del bucle si no hay errores
    except ValueError as e:
        print(f"Error: {e}")

# 10.-
print("\n9.- Escriba una función lambda que pueda resolver el área de un rectángulo.")

while True:
    try:
        circle_radius = helpers.input_circle_params()[0]

        # Validar que la base y la altura sean positivas
        if circle_radius <= 0:
            raise ValueError("El radio deben ser positivo.")

        # Usa la función lambda importada
        area = helpers.LAMBDA_FUNCTIONS["Círculo"](circle_radius)

        print(f"El área del circulo es: {area:.2f}")
        break  # Salir del bucle si no hay errores
    except ValueError as e:
        print(f"Error: {e}")

# 11.
print("""\n11.- Escriba una función lambda como parte funcion de orden superior
      y que pueda resolver el área de una figura geométrica.""")

calculate_area()
