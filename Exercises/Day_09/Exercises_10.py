'''
Ejercicios:

1.- Itera del 0 al 10 usando el bucle for, haz lo mismo usando el bucle while.
2.- Itera de 10 a 0 usando el bucle for, haz lo mismo usando el bucle while.
3.- Escriba un bucle que realice siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:
        #
        ##
        ###
        ####
        #####
        ######
        #######

4.- Utilice bucles anidados para crear lo siguiente:
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #
        # # # # # # # #

5.- Imprima el siguiente patrón:
        0 x 0 = 0
        1 x 1 = 1
        2 x 2 = 4
        3 x 3 = 9
        4 x 4 = 16
        5 x 5 = 25
        6 x 6 = 36
        7 x 7 = 49
        8 x 8 = 64
        9 x 9 = 81
        10 x 10 = 100

6.- Itere a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un bucle for e imprima los elementos.

7.- Utilice el bucle for para iterar de 0 a 100 e imprimir solo números pares

8.- Utilice el bucle for para iterar de 0 a 100 e imprimir solo números impares

9.- Utilice el bucle for para iterar de 0 a 100 e imprimir la suma total de todos los numeros, la suma de todos los numeros pares y la suma de todos los numeros impares.
'''
# 1.- Iterar los numeros de 0 a 10. Con for y while
print("1- Iteracion incremental:")
print("Mostrando los numeros de 0 a 10, usando for:")
for num in range(11):
    print(f"{num} ", end = " ")

print("\nMostrando los numeros de 0 a 10, usando while:")
num = 0
while 0 <= num <= 10:
    print(f"{num} ", end = " ")
    num += 1

print("\n")

# 2.- Iteracion decremental de numeros de 10 a 0. Con for y while
print("2- Iteracion decremental:")
print("Mostrando los numeros de 10 a 0, usando for:")
for num in range(10, -1, -1):
    print(f"{num} ", end = " ")

print("\nMostrando los numeros de 10 a 0, usando while:")
num = 10
while 10 >= num >= 0:
    print(f"{num} ", end = " ")
    num -= 1

print("\n")
    
# 3.- Dibujar un triangulo:
print("3.- Dibujando un triangulo:")
the_character = "#"
for i in range(7):
    print(the_character * i)

print("\n")

# 4.- Dibujar una matriz 8 x 8:
print("4.- Dibujando una matriz 8x8:")
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

print("\n")

# 5.- Tabla del cuadrado de un numero (0 - 10):
print("5.- Dibujando la tabla del cuadrado de un numero:")
for num in range(11):
    print(f"{num} x {num} = {num ** 2}")
    
print("\n")

# 6.- Mostrar los elementos de una lista dada:
print("6.- Mostrar todos los elementos de una lista:")
libs_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in libs_list:
    print(item)

print("\n")

# 7.- Mostrar todos los numeros impares entre 0 y 100:
print("7.- Mostrando los numeros impares entre 0 y 100:")
for num in range(101):
    if num % 2 == 0:
        continue
    print(f"{num}", end=" ")
print("\n")

# 8.- Mostrar todos los numeros pares entre 0 y 100:
print("8.- Mostrando los numeros pares entre 0 y 100:")
for num in range(101):
    if num % 2 != 0:
        continue
    print(f"{num}", end=" ")
print("\n")

# 9.- Sumar todos los numeros, sumar los numeros pares y sumar los numeros impares entre 0 y 100:
print("9.- Mostrar la suma de todos los numeros, la suma de los numeros pares y la suma de los numeros impares entre 0 y 100:")
sum_all_numbers = 0
sum_even_numbers = 0
sum_odd_numbers = 0

for num in range(101):
    sum_all_numbers += num
    if num % 2 == 0:
        sum_even_numbers += num
    else:
        sum_odd_numbers += num

print(f"La suma de todos los números es: {sum_all_numbers}")
print(f"La suma de los números pares es: {sum_even_numbers}")
print(f"La suma de los números impares es: {sum_odd_numbers}")
print("\n")