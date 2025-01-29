"""
Ejercicios de funciones en Python.

1.- Declara una función add_two_numbers. Toma dos parámetros y devuelve una suma.

2.- El área de un círculo se calcula de la siguiente manera: área = π x r x r.
Escribe una función que calcule calculate_area_of_circle.

3.- Escriba una función llamada add_all_nums que tome una cantidad arbitraria de 
argumentos y sume todos los argumentos. Verifique si todos los elementos de la 
lista son de tipo numérico. Si no es así, proporcione una respuesta razonable.

4.- La temperatura en °C se puede convertir a °F usando esta fórmula: 
        °F = (°C x 9/5) + 32. 
Escriba una función que convierta °C a °F, convert_celsius_to_fahrenheit.

5.- Escriba una función llamada check_season, toma un parámetro de mes y 
devuelve la temporada: Otoño, Invierno, Primavera o Verano.

6.- Escriba una función llamada calculate_slope que devuelva la pendiente de 
una ecuación lineal

7.- La ecuación cuadrática se calcula de la siguiente manera: 
        ax² + bx + c = 0. 
Escriba una función que calcule el conjunto de soluciones de una ecuación 
cuadrática, solve_quadratic_eqn.

8.- Declara una función llamada print_list. Esta toma una lista como parámetro 
e imprime cada elemento de la lista.

9.- Declara una función llamada reverse_list. Toma una matriz como parámetro 
y devuelve el inverso de la matriz (usa bucles).
            ejemplo:
                print(reverse_list([1, 2, 3, 4, 5]))
                # [5, 4, 3, 2, 1]
                print(reverse_list1(["A", "B", "C"]))
                # ["C", "B", "A"]

10.- Declara una función llamada capitalize_list_items. Toma una lista como parámetro 
y devuelve una lista de elementos en mayúsculas.

11.- Declara una función llamada add_item. Esta acepta una lista y un elemento como 
parámetros. Devuelve una lista con el elemento agregado al final.
            ejemplo:
                food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
                print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
                numbers = [2, 3, 7, 9]
                print(add_item(numbers, 5))   # [2, 3, 7, 9, 5]

12.- Declara una función llamada remove_item. Esta toma como parámetros una lista y 
un elemento. Devuelve una lista con el elemento eliminado de ella.
            ejemplo:
                food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
                print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
                numbers = [2, 3, 7, 9]
                print(remove_item(numbers, 3))  # [2, 7, 9]

13.- Declara una función denominada sum_of_numbers. Esta función toma un 
parámetro numérico (limite) y suma todos los números de ese rango.
            ejemplo:
                print(sum_of_numbers(5))  # 15
                print(sum_of_numbers(10)) # 55
                print(sum_of_numbers(100)) # 5050

14.- Declara una función llamada sum_of_odds_numbers. Esta función toma un parámetro 
numérico (limite) y suma todos los números impares en ese rango.

15.- Declara una función llamada sum_of_even_numbers. Esta función toma un parámetro 
numérico (limite) y suma todos los números pares en ese rango.
"""

# 1.- Funcion Sumar 2 números

print("1.- Función que suma dos números ingresados por el usuario:")


def add_two_numbers(num_1: int, num_2: int) -> int:
    """Suma dos números enteros.

    Args:
        num_1: El primer número.
        num_2: El segundo número.

    Returns:
        La suma de los dos números.
    """
    return num_1 + num_2


def is_integer(value: str) -> bool:
    """Verifica si una cadena de texto representa un número entero.

    Args:
        value: La cadena a verificar.

    Returns:
        True si la cadena es un número entero, False en caso contrario.
    """
    return value.lstrip("-+").isnumeric()


while True:
    number_1 = input("Ingrese el 1er. número: ")
    if is_integer(number_1):
        break
    print("Error. Debe ingresar un número.")

while True:
    number_2 = input("Ingrese el 2do. número: ")
    if is_integer(number_2):
        break
    print("Error. Debe ingresar un número.")

number_1, number_2 = int(number_1), int(number_2)  # Conversion a Enteros
print(f"{number_1} + {number_2} = {add_two_numbers(number_1, number_2)}")

# 2.- Calcular el area de un circulo
print("2.- Calcular el area de un circulo:")


def calculate_area_of_circle(radius: float, pi=3.141593) -> float:
    """Calcula el área de un circulo y retorna su resultado.

    Args:
        radius: el valor del radio.
        pi: valor constante en la matematica

    Returns:
        El resultado de la operacion pi * (radius ** 2).
    """
    return pi * (radius**2)


def is_positive(value: float) -> bool:
    """Verifica si el numero ingresado es positivo.

    Args:
        value: La cadena a verificar.

    Returns:
        True si la cadena es un número positivo, False en caso contrario.
    """
    return value > 0


while True:
    circle_radius = input("Ingrese el radio del circulo: ")
    if is_integer(circle_radius):
        if is_positive(float(circle_radius)):
            break
        else:
            print("Error. El radio debe ser un número positivo.")
    else:
        print("Error. Debe ingresar un número.")

circle_radius = float(circle_radius)
print(
    f"El área de un circulo que tiene un radio de {circle_radius:.2f} es: {calculate_area_of_circle(circle_radius):.2f}"
)

# 3.- Calcular y mostrar la suma de todos los numeros de una cantidad arbitraria de argumentos.
print("3.- Sumar todos los argumentos ingresados por el usuario:")


def add_all_nums(*args) -> int:
    """Suma todos los argumentos ingresados por el usuario.

    Args:
        *args: Un número variable de argumentos numéricos.

    Returns:
        La suma de todos los argumentos.
    """
    return sum(args)


numbers = []

while True:
    while True:
        num = input("Ingrese un numero: ")
        if is_integer(num):
            numbers.append(int(num))
            break
        else:
            print("Error. Debe ingresar un número.")

    if input("Desea ingresar otro número? (s/n): ").lower() == "n":
        break

print(f"La suma de los números ingresados {numbers} es: {add_all_nums(*numbers)}")


# 4.- Convertir grados Celsius a Fahrenheit
print("4.- Convertir grados Celsius a Fahrenheit:")


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """Convertir temeperatura de Celsius a Farenheit

    Args:
        celsius (float): El valor en grado Celsius.

    Returns:
        float: Retorna la conversion a grados fahrenheit
    """
    return (celsius * 9 / 5) + 32


while True:
    temperature_in_celsius = input("Ingrese la temperatura en grados Celsius: ")
    try:
        temperature_in_celsius = float(temperature_in_celsius)  # Conversion a flotante
        break
    except ValueError:
        print("Error. Debe ingresar un número válido.")

print(
    f"{temperature_in_celsius}°C = {convert_celsius_to_fahrenheit(temperature_in_celsius):.2f}°F"
)

# 5.- Verificar la estación del año, segun mes introducido por el usuario
print("5.- Verificar la estación del año:")


def check_seasson(month) -> str:
    """Verificar si el mes dado (nombre o numero) a cual estacion pertenece

    Args:
        month (str): El mes a verificar (nombre o numero).

    Returns:
        Retorna el nombre de la estacion a cual pertenece
    """

    if month in seassons["otoño"]:
        return "Otoño"
    elif month in seassons["invierno"]:
        return "Invierno"
    elif month in seassons["primavera"]:
        return "Primavera"
    else:
        return "Verano"


month_name_dict = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}

seassons = {
    "otoño": {9: "Septiembre", 10: "Octubre", 11: "Noviembre"},
    "invierno": {12: "Diciembre", 1: "Enero", 2: "Febrero"},
    "primavera": {3: "Marzo", 4: "Abril", 5: "Mayo"},
    "verano": {6: "Junio", 7: "Julio", 8: "Agosto"},
}

while True:
    month_entered = input("Ingrese el mes: ")
    try:
        if is_integer(month_entered):
            month_entered = int(month_entered)
            if month_entered not in list(month_name_dict.keys()):
                raise ValueError
        else:
            if month_entered.capitalize() not in month_name_dict.values():
                raise ValueError
        break
    except ValueError:
        print("Error. Debe ingresar un mes valido (nombre o numero correcto).")

print(f"El mes ingresado esta en la estacion de {check_seasson(month_entered)}")


# 6.- Calcular la pendiente o inclinacion de una ecuacion lineal, dado 2 puntos cartesianos
print("6.- Calcular la pendiente de una ecuacion lineal, dado 2 puntos cartesianos:")


def calculate_slope(coordinate_x1_y1: tuple, coordinate_x2_y2: tuple) -> float:
    """Calcula la pendiente de una recta dados dos puntos.

    Args:
        coordinate_x1_y1 (tuple): Coordenada (x, y) del primer punto.
        coordinate_x2_y2 (tuple): Coordenada (x, y) del segundo punto.


    Returns:
        float: La pendiente de la recta, o un mensaje de error si la recta es vertical.
    """
    x1, y1 = coordinate_x1_y1
    x2, y2 = coordinate_x2_y2
    if x1 == x2:
        raise ValueError("La recta es vertical y no tiene pendiente definida.")

    slope = (y2 - y1) / (x2 - x1)
    return slope


def get_coordinate() -> tuple:
    """Obtiene las coordenadas de un punto.

    Args:
        x: La coordenada x del punto.
        y: La coordenada y del punto.

    Returns:
        tuple: Las coordenadas del punto.
    """
    while True:
        try:
            x = float(input("Ingrese la coordenada x: "))
            y = float(input("Ingrese la coordenada y: "))
            return (float(x), float(y))
        except ValueError:
            print("Por favor, ingrese valores numéricos.")


first_coordinate = get_coordinate()
second_coordinate = get_coordinate()

print(
    f"La pendiente de la recta que pasa por los puntos {first_coordinate} y {second_coordinate} es: {calculate_slope(first_coordinate, second_coordinate):.2f}"
)


# 7.- Calcular las soluciones de una ecuación cuadrática
print("7.- Calcular las soluciones de una ecuación cuadrática:")


def solve_quadratic_eqn(a: float, b: float, c: float) -> tuple:
    """Calcula las soluciones de una ecuación cuadrática.

    Args:
        a (float): El coeficiente cuadrático.
        b (float): El coeficiente lineal.
        c (float): El término independiente.

    Returns:
        tuple: Las soluciones de la ecuación cuadrática.
    """

    if a == 0:
        raise ValueError("El coeficiente cuadrático no puede ser cero.")

    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2 * a)
        x2 = (-b - discriminant**0.5) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        raise ValueError("La ecuación no tiene solución real..")


def get_values() -> tuple:
    """Obtiene los valores de los coeficientes de una ecuación cuadrática.

    Returns:
        tuple: Los valores de los coeficientes.
    """
    while True:
        try:
            a = float(input("Ingrese el coeficiente cuadrático (a): "))
            b = float(input("Ingrese el coeficiente lineal (b): "))
            c = float(input("Ingrese el término independiente (c): "))
            return a, b, c
        except ValueError:
            print("Por favor, ingrese valores numéricos.")


a, b, c = get_values()
print(
    f"Las soluciones de la ecuación cuadrática {a}x² + {b}x + {c} = 0 son: {solve_quadratic_eqn(a, b, c):.2f}"
)


# 8.- Imprimir todos los elementos de una lista
print("8.- Imprimir todos los elementos de una lista:")


def print_all_list_elements(lst: list) -> None:
    """Imprime todos los elementos de una lista.

    Args:
        lst (list): La lista a imprimir.
    """
    for element in lst:
        print(element, end=" ")


def get_list_from_user_input() -> list:
    """Obtiene una lista de elementos ingresados por el usuario.

    Returns:
        list: La lista de elementos.
    """
    lst = []
    while True:
        element = input("Ingrese un elemento (o 'fin' para terminar): ")
        if element.lower() == "fin":
            break
        lst.append(element)
    return lst


items_list = get_list_from_user_input()

print_all_list_elements(items_list)


# 9.- Definir una funcion que reverse una lista
print("9.- Definir una funcion que reverse una lista:")


def reversing_list(lst: list) -> list:
    """Invertir una lista

    Args:
        lst (list): Conjunto de elementos a invertir

    Returns:
        list: Lista invertida
    """
    return lst[::-1]


# Se aprovecha la funcion creada en el ejercicio anterior
list_to_reverse = get_list_from_user_input()

print(f"La lista invertida es: {reversing_list(list_to_reverse)}")


# 10.- Definir una funcion que Capitalice los elementos de una lista
print("10.- Definir una funcion que Capitalice los elementos de una lista:")


def capitalize_list_items(lst: list) -> list:
    """Capitalizar los elementos de una lista

    Args:
        lst (list): Conjunto de elementos a capitalizar

    Returns:
        list: Lista con los elementos capitalizados
    """

    for element in lst:
        lst[lst.index(element)] = element.capitalize()

    return lst


# Se aprovecha la funcion creada en el ejercicio anterior
list_to_capitalize = get_list_from_user_input()

print(f"La lista invertida es: {capitalize_list_items(list_to_capitalize)}")


# 11.- Definir una funcion para agregar elementos a una lista
print("11.- Definir una funcion agregar un elemento a una lista:")


def add_item(lst: list, item) -> list:
    """Agregar un elemento a una lista

    Args:
        lst (list): La lista a la que se le agregara el elemento.
        item: El elemento a agregar.

    Returns:
        list: La lista con el elemento agregado.
    """
    lst.append(item)
    return lst


# Se aprovecha la funcion creada en el ejercicio anterior
items_list = get_list_from_user_input()

new_element = input("Ingrese el elemento a agregar a la lista: ")

print(
    f"Se ha agregado el elemento {new_element} a la lista. Ahora la lista es: {add_item(items_list, new_element)}"
)


# 12.- Definir una funcion para remover elementos a una lista
print("12.- Definir una funcion remover un elemento a una lista:")


def remove_item_from_list(lst: list, item) -> list:
    """remover un elemento a una lista

    Args:
        lst (list): La lista a la que se le removera un elemento.
        item: El elemento a remover.

    Returns:
        list: La lista sin el elemento removido.
    """
    if item in lst:
        lst.remove(item)
        return lst
    else:
        raise ValueError("El elemento no se encuentra en la lista.")


# Se aprovecha la funcion creada en el ejercicio anterior
items_list = get_list_from_user_input()

element_to_remove = input("Ingrese el elemento a remover a la lista: ")

print(
    f"Se ha removido el elemento {new_element} de la lista. Ahora la lista es: {remove_item_from_list(items_list, element_to_remove)}"
)

# 13.- Definir una funcion para sumar todos los numeros de un rango
# 14.- Definir una funcion para sumar todos los numeros impares de un rango
# 15.- Definir una funcion para sumar todos los numeros pares de un rango

print("13.- Definir una funcion para sumar todos los numeros de un rango:")


def sum_of_numbers(limit: int) -> int:
    """Suma todos los números de un rango.

    Args:
        limit (int): El límite del rango.

    Returns:
        int: La suma de todos los números del rango.
    """
    return sum(range(limit + 1))


def sum_of_odds_numbers(limit: int) -> int:
    """Suma todos los números impares de un rango.

    Args:
        limit (int): El límite del rango.

    Returns:
        int: La suma de todos los números impares del rango.
    """
    return sum(num for num in range(limit + 1) if num % 2 != 0)


def sum_of_evens_numbers(limit: int) -> int:
    """Suma todos los números pares de un rango.

    Args:
        limit (int): El límite del rango.

    Returns:
        int: La suma de todos los números pares del rango.
    """
    return  sum(num for num in range(limit + 1) if num % 2 == 0)

while True:
    user_limit = input("Ingrese el maximo de numero a sumar: ")
    try:
        if is_integer(user_limit):
            user_limit = int(user_limit)
            break
    except ValueError:
        print("Error. Debe ingresar un número válido.")

print(f"La suma de todos los números del 1 al {user_limit} es: {sum_of_numbers(user_limit)}")
print(f"La suma de los números pares del 1 al {user_limit} es: {sum_of_evens_numbers(user_limit)}")
print(f"La suma de los números impares del 1 al {user_limit} es: {sum_of_odds_numbers(user_limit)}")
