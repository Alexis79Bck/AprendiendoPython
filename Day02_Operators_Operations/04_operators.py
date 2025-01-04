'''
Los operadores en Python son símbolos especiales que realizan operaciones aritméticas o de comparación.
Python tiene varios tipos de operadores, incluidos operadores aritméticos, de asignación, de comparación, lógicos, de identidad y de membresía.

1.- Los operadores aritméticos son operadores matemáticos que se utilizan para realizar operaciones matemáticas en variables y valores.
        Estos son:
            +: Suma
            -: Resta
            *: Multiplicación
            /: División
            %: Módulo
            **: Potencia
            //: División de piso    
    
2.- Los operadores de asignación se utilizan para asignar valores a las variables.
        Estos son:
            =: Asignar
            +=: Asignar y sumar
            -=: Asignar y restar
            *=: Asignar y multiplicar
            /=: Asignar y dividir
            %=: Asignar y módulo
            **=: Asignar y potencia
            //=: Asignar y división de piso
    
3.- Los operadores de comparación se utilizan para comparar dos valores. Cuando se comparan dos valores, 
    el resultado sera siempre un valor booleano, True o False.
        Estos son:
            ==: Igual a
            !=: No igual a
            >: Mayor que
            <: Menor que
            >=: Mayor o igual que
            <=: Menor o igual que
    
4.- Los operadores lógicos se utilizan para combinar declaraciones condicionales.
    Al igual que los operadores de comparación, el resultado sera siempre un valor booleano, True o False.
        Estos son:
            and: Devuelve True si ambas declaraciones son verdaderas
            or: Devuelve True si una de las declaraciones es verdadera
            not: Invierte el resultado, devuelve False si el resultado es verdadero

Otros operadores que python tiene son los operadores de identidad y los operadores de membresía.
    
5.- Los operadores de identidad se utilizan para comparar objetos, no si son iguales, sino si son realmente el mismo objeto, con la misma ubicación de memoria.
        Estos son:
            is: Devuelve True si ambas variables son el mismo objeto
            is not: Devuelve True si ambas variables no son el mismo objeto

6.- Los operadores de membresía se utilizan para probar si una secuencia se presenta en un objeto.
        Estos son:
            in: Devuelve True si un secuencia con el valor especificado se presenta en el objeto
            not in: Devuelve

Tambien existen los operadores bitwise, que se utilizan para comparar números (binarios).
7.- Los operadores bitwise actúan a nivel de bits y realizan operaciones bit a bit.  En lugar de operar con números enteros como unidades completas, 
    estos operadores manipulan los bits individuales que componen esos números. (especialmente en lenguajes de bajo nivel como C y C++). 
        Estos son:
            &: AND
            |: OR
            ^: XOR
            ~: NOT
            <<: Desplazamiento a la izquierda
            >>: Desplazamiento a la derecha
            
Los siguientes ejemplos se mostraran el uso de los operadores aritméticos, de asignación, de comparación, lógicos, de identidad y de membresía.

'''

print("1.- Ejemplos de operadores aritméticos:") 
x, y = 5, 3  # Se asignan valores a las variables x y y

print("Suma:", x + y) # Suma
print("Resta:", x - y) # Resta
print("Multiplicación:", x * y) # Multiplicación
print("División:", x / y) # División
print("Módulo:", x % y) # Módulo
print("Potencia:", x ** y) # Potencia
print("División de piso:", x // y) # División de piso

print("\n") # Salto de línea

print("2.- Ejemplos de operadores de asignación:") 

a = 10 # Asignar un valor a la variable a
print("Asignar un valor (a = 10):", a)

a += 5 # Asignar y sumar
print("Asignar y sumar 5 (a += 5):", a)

a -= 5 # Asignar y restar
print("Asignar y restar 5 (a -= 5):", a)

a *= 15 # Asignar y multiplicar
print("Asignar y multiplicar 15 (a *= 15):", a)

a /= 9 # Asignar y dividir
print("Asignar y dividir 9 (a /= 9):", a)

a %= 3 # Asignar y módulo
print("Asignar y módulo 3 (a %= 3):", a)

a **= 5 # Asignar y potencia
print("Asignar y potencia 5 (a **= 5):", a)
    
a //= 3 # Asignar y división de piso
print("Asignar y división de piso 3 (a //= 3):", a)

print("\n") # Salto de línea

print("3.- Ejemplos de operadores de comparación:")
x, y = 5, 3 # Se asignan valores a las variables x y y
print("x:", x, "y:", y)

print("Igual a (x == y):", x == y) # Igual a
print("No igual a (x != y):", x != y) # No igual a
print("Mayor que (x > y):", x > y) # Mayor que
print("Menor que (x < y):", x < y) # Menor que
print("Mayor o igual que (x >= y):", x >= y) # Mayor o igual que
print("Menor o igual que (x <= y):", x <= y) # Menor o igual que

print("\n") # Salto de línea

print("4.- Ejemplos de operadores lógicos:")
print("x:", x, "y:", y)

print("x > 3 and y < 10:", x > 3 and y < 10) # Devuelve True si ambas declaraciones son verdaderas  
print("x > 3 or y < 10:", x > 3 or y < 10) # Devuelve True si una de las declaraciones es verdadera
print("not(x > 3 and y < 10):", not(x > 3 and y < 10)) # Invierte el resultado, devuelve False si el resultado es verdadero

print("\n") # Salto de línea

print("5.- Ejemplos de operadores de identidad:")
x = 5 # Asignar un valor a la variable x
y = 5 # Asignar un valor a la variable y
z = x # Asignar un valor a la variable z
print("x:", x, "y:", y, "z:", z)
print("El resultado es True si ambas variables son el mismo objeto (x is y):", x is y) # Devuelve True si ambas variables son el mismo objeto
print("El resultado es True si ambas variables no son el mismo objeto (x is not z):", x is not z) # Devuelve True si ambas variables no son el mismo objeto

print("\n") # Salto de línea

print("6.- Ejemplos de operadores de membresía:")
x = "Hola Mundo" # Asignar un valor a la variable x
y = {1: "a", 2: "b"} # Asignar un valor a la variable y
print("x:", x, "y:", y)
print("Devuelve True si un secuencia con el valor especificado se presenta en el objeto (Mundo in x):", "Mundo" in x) # Devuelve True si un secuencia con el valor especificado se presenta en el objeto
print("Devuelve True si un secuencia con el valor especificado no se presenta en el objeto (Python not in x):", "Python" not in x) # Devuelve True si un secuencia con el valor especificado no se presenta en el objeto


print("\n") # Salto de línea
print("7.- Ejemplos de operadores bitwise:")
x, y = 5, 3 # Se asignan valores a las variables x y y

print("AND (x & y):", x & y) # AND
print("OR (x | y):", x | y) # OR
print("XOR (x ^ y):", x ^ y) # XOR
print("NOT (~x):", ~x) # NOT
print("Desplazamiento a la izquierda (x << y):", x << y) # Desplazamiento a la izquierda
print("Desplazamiento a la derecha (x >> y):", x >> y) # Desplazamiento a la derecha


