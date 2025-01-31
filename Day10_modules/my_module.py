# mymodule.py file
def generate_full_name(first_name: str, last_name: str) -> str:
    """Generar Nombre Completo

    Args:
        first_name (str): Primer nombre
        last_name (str): Apellido

    Returns:
        str: Concatena el primer nombre y el apellido
    """
    return first_name + ' ' + last_name

def input_first_name() -> str:
    """Ingresar Primer Nombre

    Returns:
        str: Retorna el primer nombre ingresado por el usuario
    """
    return input('Ingresa tu primer nombre: ')

def input_last_name() -> str:
    """Ingresar Apellido

    Returns:
        str: Retorna el apellido ingresado por el usuario
    """
    return input('Ingresa tu apellido: ')

def print_full_name(value: str):
    """Imprime el nombre completo del usuario
    """
    print (f"Tu nombre completo es: {value}")