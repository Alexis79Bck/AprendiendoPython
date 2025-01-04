'''
1.- Escriba un script que solicite al usuario ingresar la base y la altura del triángulo y 
    Calcule e imprima el área de este triángulo (área = B * h * 0.5).
    
2.- Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. 
    Calcule e imprima el perímetro del triángulo (perímetro = a + b + c).
    
3.- Escriba un script que solicite al usuario que ingrese la longitud de los lados de un rectángulo.
    Calcule e imprima el área (área = longitud * ancho) y su perímetro (perímetro = 2 * (longitud + ancho)).
    
4.- Escriba un script que solicite al usuario que ingrese el radio de un círculo. 
    Calcule e imprima el área de un círculo (área = π * r ^ 2) y la circunferencia de un círculo (circunferencia = 2 * π * r).
    El valor de π es 3.14159.
    
5.- Escriba un script que solicite al usuario que ingrese la masa de un objeto en Kg.
    Calcule y muestre el peso del objeto en Newtons (fórmula: masa = peso * gravedad).
    La gravedad es 9.8.
    
6.- Escriba un script que solicite al usuario que ingrese su peso en kg y su altura en metros.
    Calcule e imprima el Indice de Masa Corporal (IMC = peso / altura ^ 2).

7.- Compare la longitud de 'python' y 'dragon' y haz una afirmación de comparación falsa. Imprima el resultado.

8.- Utilice el operador (and) para comprobar si 'on' se encuentra tanto en 'python' como en 'dragon'. Imprima el resultado.

9.-  Utilice el operador in para comprobar si hay 'curso' en la oración 'Python es un lenguaje de programación de alto nivel'. Imprima el resultado.

10.- Compruebe:
     10.1.- Si la división del piso de 7 por 3 es igual al valor int convertido de 2,7.
     10.2.- Si el tipo de '10' es igual al tipo de 10
     10.3.- Si int(9.8) es igual a 10
'''
# 1.- 
print("1.- Área de un triángulo:")
triangle_base = float(input("Ingrese la base del triángulo: "))
triangle_height = float(input("Ingrese la altura del triángulo: "))
triangle_area = triangle_base * triangle_height * 0.5
print("Área del triángulo:", triangle_area)

print("\n") # Salto de línea

# 2.-
print("2.- Perímetro de un triángulo:")
side_a = float(input("Ingrese el lado a del triángulo: "))
side_b = float(input("Ingrese el lado b del triángulo: "))
side_c = float(input("Ingrese el lado c del triángulo: "))
perimeter = side_a + side_b + side_c
print("Perímetro del triángulo:", perimeter)

print("\n") # Salto de línea

# 3.-
print("3.- Área y perímetro de un rectángulo:")
rectangle_length = float(input("Ingrese la longitud del rectángulo: "))
rectangle_width = float(input("Ingrese el ancho del rectángulo: "))
rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)
print("Área del rectángulo:", rectangle_area)
print("Perímetro del rectángulo:", rectangle_perimeter)

print("\n") # Salto de línea

# 4.-
print("4.- Área y circunferencia de un círculo:")
circle_radius = float(input("Ingrese el radio del círculo: "))
pi = 3.14159
circle_area = pi * (circle_radius ** 2)
circle_circunferencia = 2 * pi * circle_radius
print("Área del círculo:", circle_area)
print("Circunferencia del círculo:", circle_circunferencia)


print("\n") # Salto de línea

# 5.-
print("5.- Peso de un objeto:")
object_mass = float(input("Ingrese la masa del objeto en Kg: "))
gravity = 9.8
object_weight = object_mass * gravity
print("Peso del objeto en Newtons:", object_weight)

print("\n") # Salto de línea

# 6.-
print("6.- Índice de Masa Corporal (IMC):")
corporal_weight = float(input("Ingrese su peso en kg: "))
corporal_height = float(input("Ingrese su altura en metros: "))
imc = corporal_weight / (corporal_height ** 2)
print("Índice de Masa Corporal (IMC):", imc)

print("\n") # Salto de línea

# 7.-
print("7.- Comparación de la longitud de 'python' y 'dragon':")
string_python = "python"
string_dragon = "dragon"
lenght_python = len(string_python)
lenght_dragon = len(string_dragon)
print("¿La longitud de 'python' y 'dragon' es igual?", lenght_python == lenght_dragon)
print("¿'python' es más largo que 'dragon'?", lenght_python > lenght_dragon)
print("¿'dragon' es más largo que 'python'?", lenght_python < lenght_dragon)

print("\n") # Salto de línea

# 8.-
print("8.- Comprobando si 'on' se encuentra en 'python' y 'dragon':")
string_on = "on"
print("¿La cadena 'on' esta en la cadena 'dragon' y la cadena 'python'?", string_on in string_dragon and string_on in string_python)

print("\n") # Salto de línea

# 9.-
print("9.- Comprobando si 'curso' se encuentra en la oración 'Python es un lenguaje de programación de alto nivel':")
sentence = "Python es un lenguaje de programación de alto nivel"
word = "curso"
print("¿La palabra 'curso' se encuentra en la oración?", word in sentence)

print("\n") # Salto de línea

# 10.-
print("10.- Comprobaciones:")
print("10.1.- ¿La división del piso de 7 por 3 es igual al valor int convertido de 2,7?")
print("Respuesta:", 7 // 3 == int(2.7))
print("10.2.- ¿El tipo de '10' es igual al tipo de 10?")
print("Respuesta:", type('10') is type(10))
print("10.3.- ¿int(9.8) es igual a 10?")
print("Respuesta:", int(9.8) == 10)



