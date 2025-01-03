'''
1.- Declarar y asignar valores a las siguientes variables:
    - first_name
    - last_name 
    - full_name 
    - country 
    - city 
    - age 
Declarar y asignar valores a las siguientes variables en una sola linea:
    - is_married 
    - is_true 
    - is_light_on 
    
2.- Usando la función incorporada len() , encuentre la longitud de su nombre
3.- Compara la longitud de tu nombre y tu apellido
4.- Declara 5 como num_one y 4 como num_two
5.- Sume num_one y num_two y asigne el valor a una variable total
6.- Resta num_two de num_one y asigna el valor a una variable diff
7.- Multiplica num_two y num_one y asigna el valor a una variable producto
8.- Dividir num_one por num_two y asignar el valor a una variable división
9.- Utilice la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
10.- Calcula num_one a la potencia de num_two y asigna el valor a una variable exp
11.- Encuentra la división del piso de num_one por num_two y asigna el valor a una variable floor_division
12.- El radio de un círculo es de 30 metros.
     12.1.- Calcula el área de un círculo y asigna el valor a una variable llamada area_of_circle
     12.2.- Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circum_of_circle
13.- Tome el radio como entrada del usuario y calcule el área.
14.- Utilice la función de entrada incorporada para obtener el first_name, last_name, 
     country y age del usuario y almacenar los valores en sus variables correspondientes.
'''

# 1.- Declarar y asignar valores a las siguientes variables:
first_name = "Juanito"
last_name = "Nieves"
full_name = first_name + " " + last_name
country = "Narnia"
city = "Ciudad de los Enanos"
age = 32

# Declarar y asignar valores a las siguientes variables en una sola linea:
is_married, is_true, is_light_on = False, True, True

# 2.- Usando la función incorporada len() , encuentre la longitud de su nombre
print("Longitud de mi nombre:", len(first_name))
print("Longitud de mi apellido:", len(last_name))

# 3.- Compara la longitud de tu nombre y tu apellido
print("Comparando la longitud de mi nombre y mi apellido:")
both_are_equal = len(first_name) == len(last_name)
first_name_is_longer = len(first_name) > len(last_name)
last_name_is_longer = len(first_name) < len(last_name)
print("¿La longitud de mi nombre y mi apellido es igual?", both_are_equal)
print("¿Mi nombre es más largo que mi apellido?", first_name_is_longer)
print("¿Mi apellido es más largo que mi nombre?", last_name_is_longer)

# 4.- Declara 5 como num_one y 4 como num_two
num_one, num_two = 5, 4
print("num_one:", num_one, "num_two:", num_two)

# 5.- Sume
total = num_one + num_two
print("Suma:", total)

# 6.- Resta
diff = num_one - num_two
print("Resta:", diff)

# 7.- Multiplica
product = num_one * num_two
print("Multiplicación:", product)

# 8.- Dividir
divission = num_one / num_two
print("División:", divission)

# 9.- Utilice la división de módulo
remain_module = num_two % num_one
print("División de módulo:", remain_module)

# 10.- Calcula num_one a la potencia de num_two
exp = num_one ** num_two
print("Potencia:", exp)

# 11.- Encuentra la división del piso
floor_division = num_one // num_two
print("División de piso:", floor_division)

# 12.- El radio de un círculo es de 30 metros.
radio = 30
pi = 3.14159
print("Radio del círculo:", radio)

# 12.1.- Calcula el área de un círculo
area_of_circle = pi * (radio ** 2)
print("Área del círculo:", area_of_circle)

# 12.2.- Calcula la circunferencia de un círculo
circum_of_circle = 2 * pi * radio
print("Circunferencia del círculo:", circum_of_circle)

# 13.- Tome el radio como entrada del usuario y calcule el área.
radio = float(input("Ingrese el radio del círculo: "))
area_of_circle = pi * (radio ** 2)
print("Área del círculo:", area_of_circle)

# 14.- Utilice la función de entrada incorporada para obtener el first_name, last_name, country y age del usuario 
# y almacenar los valores en sus variables correspondientes.
first_name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
country = input("Ingrese su país: ")
age = input("Ingrese su edad: ")

print("Nombre:", first_name)
print("Apellido:", last_name)
print("País:", country)
print("Edad:", age)
