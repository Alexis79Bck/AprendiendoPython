'''
Ejercicios:
1.- Crear una tupla vacía
2.- Crea una tupla que contenga los nombres de tus hermanas y otra tupla 
    con los nombres de tus hermanos (los nombres de personas allegadas están bien)
3.- Unir tuplas de hermanos y hermanas y asignarlas a hermanos
4.- ¿Cuantos hermanos tienes?
5.- Modifica la tupla de hermanos y agrega el nombre de tu padre y madre y asígnalo a family_members
6.- Desempaquetar hermanos y padres de family_members
7.- Crea tuplas de frutas, verduras y productos animales. 
8.- Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
9.- Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
10.- Extraiga el elemento o los elementos del medio de la tupla food_stuff_tp o de la lista food_stuff_lt.
11.- Separa los tres primeros elementos y los tres últimos elementos de la lista food_staff_lt
12.- Eliminar la tupla food_staff_tp por completo
13.- Dada la siguiente tupla:
        nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    13.1.- Comprueba si 'Estonia' es un país nórdico
    13.2.- Comprueba si 'Islandia' es un país nórdico
'''

# 1.-
print("\nCreando una tupla vacía.")
my_empty_tuple = ()
print(f"Mi tupla vacía: {my_empty_tuple}")

# 2.-
print("\nCreando las tuplas hermanas y hermanos.")
sisters = ('Mary', 'Alice', 'Rose', 'Shadowkitty')
brothers = ('Eddie', 'Peter', 'Bob')
print(f'Mis hermanas se llaman: {sisters}')
print(f'Mis hermanos se llaman: {brothers}')

# 3.- 
print("\nCombinando las tuplas hermanas y hermanos.")
siblings = sisters + brothers
print(f"Todos mis hermanos se llaman: {siblings}")

# 4.-
print("\n¿Cuantos hermanos tienes?")
print(f"Tengo un total de: {len(siblings)} hermanos")

# 5.-
print("\nMiembros de la familia")
family_members = ('John', 'Grace') + siblings
print(f"Los miembros de la familia son:\n{family_members}")

# 6.-
dad, mom, *sisters_brothers = family_members
print(f"El nombre de papá es: {dad}")
print(f"El nombre de mamá es: {mom}")
print(f"Los nombres de mis hermanos son: {sisters_brothers}")

# 7.-
print("\nCreando las tuplas frutas, verduras y animales")
fruits = ('Fresa', 'Cereza', 'Uva', 'Naranja', 'Limon', 'Mango', 'Piña', 'Banana')
vegetables = ('Papa', 'Cebolla', 'Yuca', 'Zanahoria', 'Tomate', 'Pimiento')
products_from_animals = ('Queso', 'Mantequilla', 'Tocineta', 'Leche', 'Huevos')
print(f"La tupla frutas contiene: {fruits}")
print(f"La tupla verduras contiene: {vegetables}")
print(f"La tupla animales contiene: {products_from_animals}")

# 8.- 
print("\nCombinando las tuplas anteriores en una nueva tupla")
food_stuff_tp = fruits + vegetables + products_from_animals
print(f"Cosas relacionadas con comida: {food_stuff_tp}")

# 9.- 
print("\nCambiando la tupla food_stuff_tp a lista")
food_stuff_lst = list(food_stuff_tp)
print(f'La tupla food_stuff_tp:\n{food_stuff_tp}\nse ha cambiado a lista food_stuff_lst:\n{food_stuff_lst}')

# 10.-
print("\nExtraer los elementos del medio de la tupla food_stuff_tp")
middle_index = len(food_stuff_tp) // 2
middle_items = food_stuff_tp[middle_index]
print(f'La tupla food_stuff_tp tiene un total de: {len(food_stuff_tp)} elementos.')
print(f'La mitad de la tupla tupla food_stuff_tp es: {middle_index + 1}.')
print(f'los elementos del medio son: {middle_items}')

# 11.-
print("\nSeparar los 3 primeros y 3 últimos elementos de la lista food_stuff_lst")
print(f"La lista: {food_stuff_lst}")
print(f'Los 3 primeros elementos de la lista son: {food_stuff_lst[:3]}')
print(f'Los 3 últimos elementos de la lista son: {food_stuff_lst[-3:]}')

# 12.-
print("\nEliminación total de la tupla")
del food_stuff_tp

# 13.-
nordic_countries = ('Dinamarca', 'Finlandia','Islandia', 'Noruega', 'Suecia')
print(f"\nDada la siguiente tupla: nordic_countries {nordic_countries}")
print(f'Comprueba si "Estonia" es un país nórdico: {'Estonia' in nordic_countries}')
print(f'Comprueba si "Islandia" es un país nórdico: {'Islandia' in nordic_countries}')
