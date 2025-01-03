'''
  Las variables son contenedores que almacenan valores. 
  En Python, las variables no necesitan ser declaradas con un tipo de dato específico y pueden cambiar de tipo en tiempo de ejecución. 

  Para las buenas practicas, es importante y muy recomendado seguir las siguientes reglas al nombrar las variables: 
  - En ingles, por convención y legibilidad. Por ejemplo, en lugar de usar "nombre" se debe usar "name".
  - Usar nombres en singular para las variables. Por ejemplo, en lugar de "nombres" se debe usar "name".
  - Escribir en minúsculas y separar las palabras con guiones bajos (snake_case). Por ejemplo, en lugar de "nombreCompleto" se debe usar "full_name".
  - Deben ser descriptivos y representar el valor que almacenan. Por ejemplo, en lugar de "x" se debe usar "age".
  - Evitar palabras reservadas de Python y caracteres especiales. Por ejemplo, en lugar de "class" se debe usar "class_name".
  - No utilizar espacios en los nombres de las variables. Por ejemplo, en lugar de "nombre completo" se debe usar "full_name".
  - Usar nombres cortos y concisos. Por ejemplo, en lugar de "estaEsUnaVariableMuyLarga" se debe usar "variable".
  - No utilizar nombres de variables que comiencen con números. Por ejemplo, en lugar de "1numero" se debe usar "numero1".
  
  Interpolacion de cadenas:
    - Se puede combinar texto y variables en una cadena de texto utilizando el operador de formato (%). Por ejemplo:
            name = "Alice"
            age = 30
            print("My name is %s and I am %d years old." % (name, age))
    
    - Se puede utilizar el método format() para insertar variables en una cadena de texto. Por ejemplo:
            name = "Alice"
            age = 30
            print("My name is {} and I am {} years old.".format(name, age))
    
    - Se puede utilizar f-strings para insertar variables en una cadena de texto.
            name = "Alice"
            age = 30
            print(f"My name is {name} and I am {age} years old.")
'''


# Ejemplos de variables siguiendo las buenas prácticas:
first_name = "Alice"
last_name = "Smith"
email_address = "alice.smith@example.com"
user_age = 30
is_student = True
height_in_cm = 165.5

# Imprimir las variables en consola:
print("First Name:", first_name)
print("Last Name:", last_name)
print("Email Address:", email_address)
print("Age:", user_age)
print("Is Student:", is_student)
print("Height in cm:", height_in_cm)

# Interpolación de cadenas:
# Combinando texto y variables utilizando el operador de formato (%)
print("My name is %s and I am %d years old." % (first_name, user_age))

# Utilizando el método format() para insertar variables en una cadena de texto
print("My name is {} and I am {} years old.".format(first_name, user_age))

# Utilizando f-strings para insertar variables en una cadena de texto
print(f"My name is {first_name} and I am {user_age} years old.")


