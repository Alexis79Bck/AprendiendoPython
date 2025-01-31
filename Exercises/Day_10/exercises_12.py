"""
Ejercicios

Crear un archivo de modulos, puedes llamarlo como quieras, por ejemplo: exercise_module.py

1.- En el archivo de modulos, crear una funcion que genere un nombre de usuario de 6 caracteres
    alfanumericos aleatorios. El nombre puede contener mayusculas, minusciulas y digitos. 
    No se acepta simbolos especiales.
        Salida esperada:
            print(user_id_random()) # 3a5Gh7
        
2.- Declarar una funcion user_id_gen_by_user(). No acepta ningún parámetro, pero acepta dos 
    entradas mediante input(). 
            * Una de las entradas es la cantidad de caracteres 
            * La segunda es la cantidad de ids que se supone que se generarán
        Salida esperada:
            print(user_id_gen_by_user()) 
                # inputs: 8 5
                # 3a5TrGh7
                # L1bB4Gh7
                # xZx86Ju0
                # QppTr5As
                # 98bTxGzH
            
3.- Escriba una función llamada rgb_color_gen. Generará colores RGB (tres valores que 
    van de 0 a 255 cada uno).
        Salida esperada:
            print(rgb_color_gen()) 
            # rgb(20, 128, 76)
            
4.- Llama a tu función shuffle_list, toma una lista como parámetro y devuelve una 
    lista aleatoria.

5.- Escriba una función que devuelva una arreglo de siete números aleatorios en 
    un rango de 0 a 9. Todos los números deben ser únicos.
    
6.- Escriba una función list_of_hexa_colors que devuelva cualquier número de colores 
    hexadecimales en una matriz (seis números hexadecimales escritos después de #. 
    El sistema de numeración hexadecimal está formado por 16 símbolos, del 0 al 9 y 
    las primeras 6 letras del alfabeto, af.)

7.- Escriba una función list_of_rgb_colors que devuelva cualquier número de 
    colores RGB en un lista.

8.- Escriba una función generate_colors que pueda generar cualquier cantidad de 
    colores hexadecimales o rgb.
"""


import exercise_module

print(f"1.- Id random de 6 caracteres: {exercise_module.user_id_random()}")
print("2.- Lista de Ids generado por el Usuario: ")

ids_generated = exercise_module.user_id_gen_by_user()
for id_element in ids_generated:
    print(f"{id_element}", end="\n")

print(f"3.- El color generado aleatorioamente es: {exercise_module.rgb_color_gen()}")

qty_item_list_to_input = exercise_module.get_quantity("Ingrese la cantidad de items que tendrá la lista:")
the_user_list = exercise_module.list_generated_by_user_input(
    qty_item_list_to_input)

print(f"4.- la lista original es: {the_user_list}")
print(f"La lista mezclada es: {exercise_module.shuffle_list(the_user_list)}")
print("\n")
print(f"5.- Lista de 7 números aleatorios únicos: {exercise_module.list_of_seven_unique_random_numbers()}")
print("\n")

qty_colors_to_gen = exercise_module.get_quantity("Ingrese la cantidad de colores a generar:")

print(f"6.- Listado de {qty_colors_to_gen} colores hexadicimales generados: {exercise_module.list_of_hexa_colors(qty_colors_to_gen)}")

qty_colors_to_gen = exercise_module.get_quantity("Ingrese la cantidad de colores a generar:")

print(f"7.- Listado de {qty_colors_to_gen} colores RGB generados: {exercise_module.list_of_rgb_colors(qty_colors_to_gen)}")

qty_colors_to_gen = exercise_module.get_quantity("Ingrese la cantidad de colores a generar:")
color_format = exercise_module.select_colors_format()

print(f"8.- Listado de {qty_colors_to_gen} colores generados: {exercise_module.generate_colors(qty_colors_to_gen, color_format)}")
