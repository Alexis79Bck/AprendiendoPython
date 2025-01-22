'''
Ejercicios
1.- Obtenga la entrada del usuario mediante input(“Ingrese su edad: ”). Si el usuario tiene 18 años o más, proporcione comentarios: Tiene la edad suficiente para conducir. Si es menor de 18 años, proporcione comentarios para esperar la cantidad de años faltantes.

2.- Compara los valores de my_age y your_age usando if … else. ¿Quién es mayor (tú o yo)? Usa input(“Ingresa tu edad: ”) para obtener la edad como entrada. Puedes usar una condición anidada para imprimir 'año' para una diferencia de edad de 1 año, 'años' para diferencias mayores y un texto personalizado si my_age = your_age.

3.- Ingresado dos números por el usuario mediante el mensaje de entrada. Si a es mayor que b, devolver a es mayor que b; si a es menor que b, devolver a es menor que b; de lo contrario, a es igual a b.

4.- Escriba un código que califique a los estudiantes según sus puntuaciones, valide que el valor ingresados esté dentro de los limites (0 - 100):
        90-100 -> A
         70-89 -> B
         60-69 -> C
         50-59 -> D
          0-49 -> F
          
5.- Comprueba si la estación es Otoño, Invierno, Primavera o Verano. Segun el mes introducido por el usuario es: 
        Septiembre, Octubre o Noviembre -->  Otoño. 
        Diciembre, Enero o Febrero -->  Invierno. 
        Marzo, Abril o Mayo -->  Primavera. 
        Junio, Julio o Agosto -->  Verano.
    
    Realiza una validacion si el usuario ingresa algun valor diferente a los meses del año.

6.- La siguiente lista contiene algunas frutas: 
        fruits = ['banana', 'manzana', 'fresa', 'mora', 'pera']
        
    Se le solicita al usuario que ingrese una fruta. Si esa fruta no existe, se agrega a la lista, de lo contrario mostrar un mensaje indicando que la fruta ya existe en la lista.
'''

# 1.- Comprobacion de edad

age = int(input('Ingrese su edad: '))
age_border = 18
is_older = True if age >= age_border else False

if is_older:
    print(f'Felicitaciones!!! Eres mayor de edad con tus {age} años.')
else:
    age_diff = age_border - age
    print(f'Aun eres menor de edad!!! Tienes {age} años y te falta {age_diff} años para cumplir {age_border} años.')

print('\n')

# 2.-  ¿Quién es mayor (tú o yo)?
your_age = int(input('Cual es tu edad? '))
my_age = 45

if your_age > my_age:
    your_diff = your_age - my_age
    unit = "año" if your_diff == 1 else "años"
    print(f'Tu eres mayor a mi por una diferencia de {your_diff} {unit}')
elif your_age < my_age:
    my_diff =  my_age - your_age
    unit = "año" if my_diff == 1 else "años"
    print(f'Yo soy mayor a ti por una diferencia de {my_diff} {unit}')
else:
    print('Los dos tenemos la misma edad')
    
print('\n')

# 3.- Comnparar 2 numeros
a = int(input('Ingrese el valor de A: '))
b = int(input('Ingrese el valor de B: '))

if a > b:
    print(f'{a} es mayor que {b}')
elif a < b:
    print(f'{b} es mayor que {a}')
else:
    print(f'{a} y {b} son iguales')
    
# 4.- Calificaciones de un grupo de alumnos
student_name = input('Ingrese el nombre del alumno: ')
calification = int(input('Ingrese la calificación del alumno (0 - 100): '))

if calification.isalpha():
    print('Debe ingresar un valor númerico.')
elif calification < 0 or calification > 100:
    print('Calificación fuera de rango.')
else:
    if calification >= 90:
        print(f'El estudiante {student_name} tuvo la calificación de A.')
    elif calification >= 70:
        print(f'El estudiante {student_name} tuvo la calificación de B.')
    elif calification >= 60:
        print(f'El estudiante {student_name} tuvo la calificación de C.')
    elif calification >= 50:
        print(f'El estudiante {student_name} tuvo la calificación de D.')
    else:
        print(f'El estudiante {student_name} tuvo la calificación de F.')    

# 5.- Mostrar la estación segun el mes introducido
     
month_entered = input('Ingrese el mes: ').capitalize()
month_list = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
]
seassons = {
    'otonio': ['Septiembre', 'Octubre', 'Noviembre'],
    'invierno': ['Diciembre', 'Enero', 'Febrero'], 
    'primavera': ['Marzo', 'Abril', 'Mayo'],
    'verano': ['Junio', 'Julio', 'Agosto']
}

if month_entered not in month_list:
    print('Debe ingresar un mes válido.')
else:
    if month_entered in seassons['otonio']:
        print(f'{month_entered} esta en la estacion de Otoño')
    elif month_entered in seassons['invierno']:
        print(f'{month_entered} esta en la estacion de Invierno')
    elif month_entered in seassons['primavera']:
        print(f'{month_entered} esta en la estacion de primavera')
    else:
        print(f'{month_entered} esta en la estacion de verano')
        
# 6.- Lista de frutas
fruits = ['banana', 'manzana', 'fresa', 'mora', 'pera']

fruit_entered = input('Ingrese una fruta: ').lower()

if fruit_entered in fruits:
    print(f'La fruta {fruit_entered} existe dentro de la lista de frutas: {fruits}')
else:
    fruits.append(fruit_entered)
    print(f'La nueva fruta {fruit_entered} se agregó de la lista de frutas: {fruits}')
    

    