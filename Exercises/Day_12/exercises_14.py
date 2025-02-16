"""
Ejercicios

Tenemos las siguientes listas:
    countries = ['Estonia', 'Finlandia', 'Suecia', 'Dinamarca', 'Noruega', 'Islandia']
    names = ['Asabeneh', 'Lidiya', 'Ermias', 'Alexa', 'Tony', 'Christian', 'Joe']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
1.- Explique la diferencia entre mapa, filtro y reducción.
2.- Explique la diferencia entre función de orden superior (HOF), cierre (Closure)
    y decorador (Decorator).
3.- Defina una función de llamada antes de map, filter o reduce, vea los ejemplos.
4.- Utilice el bucle for para imprimir cada país en la lista de países.
5.- Utilice for para imprimir cada nombre en la lista de nombres.
6.- Utilice for para imprimir cada número en la lista de números.
7.- Utilice el mapa para crear una nueva lista cambiando cada país a mayúscula 
    en la lista de países
8.- Utilice el mapa para crear una nueva lista cambiando cada número por su 
    cuadrado en la lista de números.
9.- Utilice el mapa para cambiar cada nombre a mayúsculas en la lista de nombres
10.- Utilice el filtro para filtrar los países que contienen la palabra "landia".
11.- Utilice el filtro para filtrar países que tengan exactamente seis caracteres.
12.- Utilice el filtro para filtrar los países que contengan seis letras o más en 
    la lista de países.
13.- Utilice el filtro para filtrar los países que comienzan con 'E'
14.- Encadenar dos o más iteradores de lista (por ejemplo, arr.map(callback)
    .filter(callback).reduce(callback))
15.- Declare una función llamada get_string_lists que toma una lista como parámetro 
    y luego devuelve una lista que contiene solo elementos de cadena.
16.- Utilice reducir para sumar todos los números en la lista de números.
17.- Utilice reduce para concatenar todos los países y producir esta oración: 
    Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa.
18.- Declare una función llamada categorize_countries que devuelva una lista de países
    con algún patrón común (por ejemplo, 'land', 'ia', 'isla', 'stan')).

Utilizando el archivo countries.py, ubicado en la carpeta datas
19.- Declare una función get_first_ten_countries: devuelve una lista de los primeros
    diez países de la lista.
20.- Declare una función get_last_ten_countries que devuelva los últimos diez países de
    la lista de países.
    
Utilizando el archivo countries_data.py, ubicado en la carpeta datas
21.- Ordenar países por nombre, por capital, por población
22.- Clasifique los diez idiomas más hablados por ubicación.
23.- Clasifique los diez países más poblados.

========================================================================
1. Diferencia entre map, filter y reduce:

map():
- Aplica una función a cada elemento de un iterable
- Retorna un nuevo iterable con los resultados
- No modifica el iterable original
Ejemplo: map(lambda x: x*2, [1,2,3]) -> [2,4,6]

filter():
- Filtra elementos según una función que retorna True/False
- Retorna solo los elementos que cumplen la condición
- No modifica el iterable original
Ejemplo: filter(lambda x: x > 2, [1,2,3,4]) -> [3,4]

reduce():
- Combina elementos de un iterable aplicando una función acumulativa
- Retorna un único valor final
- Requiere importar de functools
Ejemplo: reduce(lambda x,y: x+y, [1,2,3,4]) -> 10

2. Diferencia entre HOF, Closure y Decorator:

HOF (Higher Order Function):
- Función que puede recibir otras funciones como argumentos
- Y/o retornar funciones como resultado
- Ejemplo: map(), filter(), reduce()

Closure:
- Función que retorna otra función
- Mantiene acceso a variables de su scope exterior
- Útil para mantener estado entre llamadas
Ejemplo:
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

Decorator:
- Función que modifica el comportamiento de otra función
- Se aplica usando el símbolo @
- Es un tipo especial de HOF
Ejemplo:
@timer
def my_function():
    pass
"""
import fns_exercises_14 as helpers

ALL_COUNTRIES = helpers.COUNTRIES_NAMES.countries
"""Lista de nombres de países."""

COUNTRIES_INFO = helpers.COUNTRIES_DATA.data
"""Lista de dicionarios con informacion de los países."""

countries = ['Estonia', 'Finlandia', 'Suecia',
             'Dinamarca', 'Noruega', 'Islandia']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Alexa', 'Tony', 'Christian', 'Joe']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def print_data(data_list: list, func):
    """HOF para imprimir los elementos de la lista
       en consola.
    Args:
        data_list (list): Lista a procesar
        func (callable): Funcion a emplear en cada elemento
    """
    for data in data_list:
        func(data)


def transform_list(data_list: list, func):
    """HOF para transformar los elementos de una lista
    Args:
        data_list (list): Lista a procesar
        func (callable): Funcion a emplear en cada elemento
    Return:
        Nueva lista transformada
    """
    return list(map(func, data_list))


def filter_list_by(data_list: list, filter_func):
    """HOF para filtrar la lista segun funcion de 
       filtrado.
    Args:
        data_list (list): Lista a procesar
        filter_func (callable): Funcion a emplear en cada elemento
    Return:
        Nueva lista filtrada
    """
    return list(filter(filter_func, data_list))


def filter_strings(func):
    """
    Decorador para filtrar solo las cadenas de texto de una lista.

    Args:
        func (callable): La función a decorar.

    Returns:
        callable: La función decorada.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if helpers.is_list(result):
            string_list = [item for item in result if isinstance(item, str)]

            if helpers.is_empty_string_list(string_list):
                print(f"La lista {result} no contiene ningún elemento string o cadena de texto.")
                return []

            return string_list

        return f"{result} es un tipo de dato diferente. Se espera que sea una lista"

    return wrapper


@filter_strings
def get_string_list(data_list: list) -> list:
    """Función para obtener una lista de cadenas de una lista dada."""
    return data_list


def list_to_process(data_list, operation):
    """
    Función de orden superior para procesar listas de números o cadenas.

    Args:
        data_list (list): La lista a procesar.
        operation (callable): La función a aplicar (suma, combinación, etc.).

    Returns:
        El resultado de aplicar la operación a la lista, o un mensaje de error.
    """

    if helpers.is_list(data_list):
        if helpers.is_int_list(data_list):
            return operation(data_list)  # Aplicamos la operación directamente
        elif helpers.is_strings_list(data_list):
            return operation(data_list)  # Aplicamos la operación directamente
        else:
            return "La lista contiene elementos de tipo no compatible."
    return f"{data_list} es un tipo de dato diferente. Se espera que sea una lista"


def categorize_items(data_list: list, pattern: str):
    """
    HOF que crea una función para categorizar una coleccion de elementos.

    Args:
        pattern (str): El patrón común a buscar.

    Returns:
        callable: Una función que recibe una lista de datos y devuelve una nueva lista con
                  los elementos que contienen el patrón.
    """
    return filter_list_by(data_list, lambda item: helpers.pattern_contain(item, pattern))



def get_n_items(qty: int = 1):
    """Obtener n elementos de una lista
    
    Args:
        qty (int): Cantindad de elementos a extraer, default = 1.
    
    Returns:
        _slice_from (callable): Retorna una lista con la cantidad de elementos obtenidos 
    """
    def _slice_from(data_list: list) -> list:
        if qty >= 0:
            return data_list[:qty]

        return data_list[qty:]

    return _slice_from


def sorted_list(data_list: list, reverse=False):
    """Ordenar una lista dada, con opción a orden reverso

    Args:
        data_list (list): Lista dada para ordenar.
        reverse (bool): Opcional, True para orden inverso. False por defecto

    Returns:
        _sorted_by(callable): Retorna la lista ordenada por la columna criterio
    """
    def _sort_by_column(key_gen) -> list:
        """
        Ordena una lista según un criterio generado por una función.

        Args:
            key_generator (callable): La función que genera la clave de ordenamiento.

        Returns:
            list: La lista ordenada.
        """
        if not isinstance(data_list, list):
            raise TypeError("data_list debe ser una lista.")
        if not callable(key_gen):
            raise TypeError("key_generator debe ser una función.")

        return sorted(data_list, key=key_gen(), reverse=reverse)

    return _sort_by_column


def classify_list(classifying_func):
    """
    Función de orden superior genérica para clasificar una lista.

    Args:
        func (callable): La función que realiza la clasificación específica.

    Returns:
        callable: La función anidada _list_to_classify.
    """
    def _list_to_classify(data_list: list, classify_type: str) -> list:
        """
        Clasifica una lista utilizando la función especificada.

        Args:
            data_list (list): La lista a clasificar.

        Returns:
            list: La lista clasificada.
        """
        return classifying_func(data_list, classify_type)

    return _list_to_classify



print("4.- Imprimir los nombres de los paises: ")
print_data(countries, helpers.print_item)
print("\n5.- Imprimir los nombres de la lista: ")
print_data(names, helpers.print_item)
print("\n6.- Imprimir los números de la lista: ")
print_data(numbers, helpers.print_item)

print("*"*40)

print("\n7.- Imprimir los nombres de los paises en MAYUSCULAS: ")
new_countries_list = transform_list(countries, helpers.change_to_uppercase)
print_data(new_countries_list, helpers.print_item)

print("\n8.- Imprimir los cuadrados números de la lista: ")
squares_numbers = transform_list(numbers, helpers.square_of)
print_data(squares_numbers, helpers.print_item)

print("\n9.- Imprimir los nombres de la lista en MAYUSCULAS: ")
new_names_list = transform_list(names, helpers.change_to_uppercase)
print_data(new_names_list, helpers.print_item)

print("*"*40)

print("\n10.- Imprimir los países que contienen la palabra 'landia': ")
countries_with_landia = filter_list_by(countries, helpers.contain_landia)
print_data(countries_with_landia, helpers.print_item)

print("\n11.- Imprimir los países que tienen 6 caracteres exactos: ")
countries_with_6_chars = filter_list_by(
    countries, helpers.have_six_chars_exact)
print_data(countries_with_6_chars, helpers.print_item)

print("\n12.- Imprimir los países que tienen 6 o mas caracteres: ")
countries_with_6_more_chars = filter_list_by(
    countries, helpers.have_six_or_more_chars)
print_data(countries_with_6_more_chars, helpers.print_item)

print("\n13.- Imprimir los países que empiece con E: ")
countries_start_with_e = filter_list_by(countries, helpers.start_with_letter_e)
print_data(countries_start_with_e, helpers.print_item)

print("*"*40)

print("\n14.- Encadenación de varios iteradores: ")
filter_result = filter_list_by(
                    list(
                        zip(
                            numbers,
                            transform_list(numbers, helpers.square_on_odds_cube_on_even)
                            )
                        ), helpers.unpacking_tuple
                    )
print("El numero par y su cubo:")
print_data(filter_result, helpers.print_item)

print("*"*40)

print("\n15.- Filtrar solo los elementos que son cadena de texto: ")
list_with_randoms_items = helpers.shuffling_list_and_select(countries, names, numbers)
print_data(get_string_list(list_with_randoms_items), helpers.print_item)

print("*"*40)

print("\n16.- Reduce la lista 'numbers' a la suma de sus elementos: ")
numbers_list_reduced = list_to_process(numbers, helpers.to_sum_numbers)
print(f"La lista {numbers} se redujo a {numbers_list_reduced} mediante la suma.")

print("*"*40)

print("""\n17.- Combina la lista 'countries' y crear la oracion:
    (los nombres de paises separado por coma) son paises europa del norte.""")
combined_countries_names = list_to_process(countries, helpers.combine_strings)
print(f"{combined_countries_names} son paises de europa del norte.")

print("*"*40)

print("\n18.- Filtra la lista 'countries' usando un patron.")
the_pattern = input("Ingrese un texto patrón a buscar: ")
filtered_list_countries = categorize_items(countries, the_pattern)
print(f"La lista de nombres de paises filtrado por el patron dado: {filtered_list_countries}")

print("*"*40)

print("\n19.- lista de los primeros diez países .")
get_first_10_countries = get_n_items(10)
first_10_countries = get_first_10_countries(ALL_COUNTRIES)
print_data(first_10_countries, helpers.print_item)


print("\n20.- lista de los últimos diez países .")
get_last_10_countries = get_n_items(-10)
last_10_countries = get_last_10_countries(ALL_COUNTRIES)
print_data(last_10_countries, helpers.print_item)

print("*"*40)

print("\n21.- Ordenar los paises por: ")
print("\n\tA.- Nombre: ")

countries_sorted_by_names = sorted_list(COUNTRIES_INFO)(helpers.key_gen_name)
helpers.print_countries_sorted_by(countries_sorted_by_names, "Nombre")

print("\n\tB.- Capital: ")
countries_sorted_by_capitals = sorted_list(COUNTRIES_INFO)(helpers.key_gen_capital)
helpers.print_countries_sorted_by(countries_sorted_by_capitals, "Capital")

print("\n\tC.- Población: ")
countries_sorted_by_populations = sorted_list(COUNTRIES_INFO, reverse=True)(helpers.key_gen_population)
helpers.print_countries_sorted_by(countries_sorted_by_populations, "Poblacion")

print("\n22.- Clasificar los 10 idiomas mas hablados por ubicacion: ")
classify_by_language = classify_list(helpers.classify_by)
ten_most_spoken_languages = classify_by_language(COUNTRIES_INFO, "Idioma")

print("10 Idiomas más hablados:")
for item in ten_most_spoken_languages[:10]:
    print(f"- {item['language']}: {item['frequency']}")


print("\n23.- Clasificar los 10 idiomas mas hablados por ubicacion: ")
classify_by_populations = classify_list(helpers.classify_by)
ten_most_populations_countries = classify_by_populations(COUNTRIES_INFO, "Poblacion")

print("10 Paises mas poblados:")
for country in ten_most_populations_countries[:10]:
    print("País:")
    print(f"  Nombre: {country['name']}")
    print(f"  Población: {country['population']}")
    print(".-"*60)
