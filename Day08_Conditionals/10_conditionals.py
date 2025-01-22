'''
Estructura Condicional

if:
En Python y otros lenguajes de programación, la palabra clave if se utiliza para comprobar si una condición es verdadera y ejecutar el código del bloque. Recuerde la sangría después de los dos puntos.

Cabe destacar que la apertura del bloque de codigo se inicia en la siguiente linea despues de dos puntos (:), con un nivel de identacion. A diferencia de otros lenguajes que se requiere un par de llaves {} para indicar el inicio y fin de bloque de codigo.

Sintaxis:
    if <condicion>:
        ---bloque de codigos
        
if ... else:
Se ejecutara el primer bloque si la condicion es verdadera, en caso contrario, se ejecutara el segundo bloque.

Sintaxis:
    if <condicion>:
        ---bloque de codigos, cuando es verdadero la condicion
    else:
        ---bloque de codigos, cuando es falso la condicion

if ... elif ... else
Si se requiere multiples condiciones, se utiliza la palabra reservada elif.

Sintaxis:
    if <condicion>:
        ---bloque de codigos, cuando es verdadero la condicion
    elif <condicion>:
        ---bloque de codigos, cuando la condicion anterior es falsa, y esta nueva condicion es verdadera
    else:
        ---bloque de codigos, cuando la condicion anterior es falsa
'''

# if ... else:
a = input('Ingrese un texto: ')

if a == 'Hola Mundo':
    print(f'El texto "{a}" es igual a "Hola Mundo"')
else:
    print(f'El texto "{a}" no es igual a "Hola Mundo"')
    
# if ... elif ... else
n = int(input('Ingrese un numero: '))
print(type(n))
if n > 0:
    print(f'El número {n} es positivo')
elif n < 0:
    print(f'El número {n} es negativo')
else:
    print(f'El número {n} es igual a 0')
    

# Condicionales anidados (nested if)
age = int(input('Ingrese su edad: '))
country = input('Ingrese el pais: ')

if age >= 18:
    if country == "España":
        print("Eres mayor de edad y vives en España.")
    else:
        print("Eres mayor de edad, pero no vives en España.")
else:
    print("Eres menor de edad.")
    
# Condicionales con operadores lógicos (and / or / not)
have_license = True
have_insurance = False
is_raining = True
have_umbrella = False
age = 20

if not is_raining or have_umbrella:        
    if have_license and age >= 18 and have_insurance:
        print("Podré salir en mi coche.")
    else:
        print("Podré salir pero no en mi coche.")
else:
        print("No podré salir hoy.")
    
''' 
En Python, el shorthand (o sintaxis abreviada) en estructuras condicionales se refiere a una forma más concisa de escribir condiciones, especialmente cuando se trata de asignar valores o realizar acciones simples en función de una condición. La expresión ternaria es la herramienta principal para lograr esto. 

Sintaxis:
    valor_si_verdadero if condición else valor_si_falso
    
¿Cuándo usar shorthand?
    - Asignaciones simples: Cuando necesitas asignar un valor a una variable dependiendo de una condición.
    - Expresiones concisas: Para crear expresiones más compactas y legibles en ciertos casos.
    - Funciones lambda: Dentro de funciones lambda para realizar operaciones simples basadas en condiciones.

¿Cuándo NO usar shorthand?
    - Condicionales anidados: Si tienes múltiples condiciones anidadas, el shorthand puede dificultar la lectura y el mantenimiento del código.
    - Bloques de código largos: Si la acción a realizar en cada rama de la condición es extensa, es mejor utilizar un if tradicional con bloques else.
    - Legibilidad: Si la condición es compleja o el código es crítico, la legibilidad debe ser priorizada sobre la concisión. Un if tradicional puede ser más claro en estos casos.
    
Nota importante: El shorthand puede ser una herramienta útil para escribir código más conciso, pero debe utilizarse con moderación.La legibilidad es fundamental para:
    - Mantenibilidad: Facilita la modificación y actualización del código a largo plazo.
    - Depuración: Permite identificar y corregir errores de manera más eficiente.
    - Colaboración: Mejora la comprensión del código por parte de otros desarrolladores.

En resumen, el shorthand puede ser un aliado en la escritura de código, pero siempre y cuando no comprometa la claridad y mantenibilidad del mismo. Fomenta las buenas prácticas y elige la opción que haga tu código más fácil de entender y mantener.
'''

# Ejemplos    
# Asignación condicional
x = int(input('Ingrese el valor de X: '))
absolute_value = x if x >= 0 else -x
print(f'El valor absoluto de {x} es {absolute_value}')

# Expresión dentro de print
your_age = int(input('Ingrese su edad: '))
print("Eres Mayor de ddad" if your_age >= 18 else "Eres Menor de Edad")

# Comprehension de Lista
numbers_list = [1, 2, 3, 4, 5]
print(f'Los numeros son: {numbers_list}')
pairs = [num for num in numbers_list if num % 2 == 0]
print(f'Los numeros pares encontrados en la lista son: {pairs}')

    