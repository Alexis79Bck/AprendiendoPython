"""
¿Qué es un módulo?
Un módulo es un archivo independiente que contiene código de Python que puede ser 
reutilizado en diferentes partes de un programa o en otros programas. Un módulo puede contener:
    Funciones: Bloques de código que realizan tareas específicas.
    Clases: Plantillas para crear objetos que comparten características y comportamientos.
    Variables: Almacenan datos de diferentes tipos (números, texto, listas, etc.).
    Código ejecutable: Instrucciones que se ejecutan cuando se importa el módulo.

¿Por qué usar módulos?
Los módulos ofrecen muchas ventajas a los programadores:

    * Organización: Permiten dividir el código en partes más pequeñas y manejables, 
            lo que facilita la comprensión y el mantenimiento. Los módulos son una herramienta 
            fundamental para la organización del código en proyectos grandes y complejos, ya que 
            permiten dividir el código en unidades lógicas y reutilizables, lo que facilita el 
            desarrollo, el mantenimiento y la colaboración en equipos.
    * Reusabilidad: Se pueden utilizar las funciones, clases y variables definidas en un módulo 
            en diferentes programas sin tener que reescribirlas.
    * Legibilidad: Al separar el código en módulos, se mejora la legibilidad y se facilita 
            la identificación de errores.
    * Mantenimiento: Los cambios en un módulo no afectan a otros módulos, lo que simplifica el 
            mantenimiento y la actualización del código.
    * Colaboración: Varios programadores pueden trabajar en diferentes módulos de un mismo 
            proyecto sin interferir entre ellos.

¿Cómo usar módulos?
Para utilizar un módulo en Python, se utiliza la palabra clave import. De esta manera se puede 
acceder a todas las funciones que en ese modulo contiene. Para acceder a las funciones de un 
modulo se debe trabajar como si de un objeto se tratare, por ejemplo: my_module.function_name()

Por ejemplo:
    import my_module  
    
Tambien puede llamar una función o varias funciones determinadas de un modulo, de 
la siguiente manera:
    Importando las funciones:
            generate_full_name, 
            input_first_name, 
            input_last_name, 
            print_full_name 
    del un módulo (my_module.py)
    
    from my_module import generate_full_name, input_first_name, input_last_name, print_full_name
    
Incluyendo podria agregarle alias a las funciones, para hacer mas legible el codigo, 
de la siguiente manera:
       from my_module import generate_full_name as fullname, input_first_name as userfirstname, 
                             input_last_name as userlastname, print_full_name as showfullname
       
Es preferible importar funciones específicas en lugar de usar * para evitar conflictos 
de nombres y mejorar la legibilidad del código.

No solo se puede importar funciones, tambien se puede importar clases, variables, etc.

Tambien debe tener en cuenta que no solo los modulos personalizados se pueden importar, 
tambien aquellos modulos que son propios de python o de algun paquete instalado de terceros, 
tales como:
    - math
    - random
    - datetime
    - os
    - sys
    - etc.
    
Para importar un modulo propio de python, se debe hacer de la siguiente manera:

    import math
    import random
    import datetime
    
    from math import pi, si solo queremos utilizar el valor de pi
    from random import randint, si solo queremos generar un numero aleatorio
    from datetime import datetime, si solo queremos obtener la fecha y hora actual
    
asi sucesivamente, se puede importar cualquier modulo de python, y utilizar las funciones, 
clases, variables, etc. que contenga.
      
Las Buenas prácticas
    * Utilizar nombres descriptivos para los módulos y sus elementos.
    * Agrupar funciones y clases relacionadas en módulos separados. 
        Por ejemplo, un módulo podría contener funciones para la gestión de usuarios, 
        otro módulo para la gestión de productos, etc
    * Documentar los módulos y sus funciones utilizando docstrings.
"""

# Importar el modulo math y random
import math
import random

# Importar un módulo (my_module.py)
import my_module



# Llamar a las funciones generate_full_name del módulo, input_first_name e input_last_name
# para generar el nombre completo del usuario
firstname = my_module.input_first_name()
lastname = my_module.input_last_name()
full_name = my_module.generate_full_name(
    firstname, lastname)  # Generar el nombre completo
my_module.print_full_name(full_name)  # Imprimir el resultado

print("\n")

# Otra forma de hacerlo en una sola linea
# Aunque no es recomendable, ya que es dificil de leer
# Se recuerda que la prioridad es la legibilidad del codigo antes de la concision
print("Llamando solo una unica funcion, para generar el nombre completo: ")

my_module.print_full_name(my_module.generate_full_name(
    my_module.input_first_name(), my_module.input_last_name()))

# Generar el primer número aleatorio entre 1 y 100
first_number_random = random.randint(1, 100)
# Generar el segundo número aleatorio entre 1 y 100
second_number_random = random.randint(1, 100)
# Generar el tercer número aleatorio entre 1 y 100
third_number_random = random.randint(1, 100)

# Calcular el factorial del primer número aleatorio
factorial_first_number = math.factorial(first_number_random)
# Calcular la raíz cuadrada del segundo número aleatorio
sqrt_second_number = math.sqrt(second_number_random)
# Elevar el tercer número aleatorio al cuadrado
pow_third_number = math.pow(third_number_random, 2)

print(f"Primer número aleatorio: {first_number_random}")
print(f"Segundo número aleatorio: {second_number_random}")
print(f"Tercer número aleatorio: {third_number_random}")
print(f"Factorial del primer número aleatorio: {factorial_first_number}")
print(f"Raíz cuadrada del segundo número aleatorio: {sqrt_second_number}")
print(f"Tercer número aleatorio elevado al cuadrado: {pow_third_number}")
