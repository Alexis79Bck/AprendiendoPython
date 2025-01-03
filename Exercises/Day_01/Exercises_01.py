'''
Ejercicios del día 01:

1.- Comprueba la versión de Python en la terminal. (Versión que se está utilizando)
2.- Realice las siguientes operaciones. Los operandos son 3 y 4.
        - adición(+)
        - sustracción(-)
        - multiplicación(*)
        - módulo(%)
        - división(/)
        - exponencial(**)
        - operador de división de piso(//)
3.- Imprimir un texto que muestre Su Nombre, Su Apellido, Su Edad y El Pais de Nacimiento. 
4.- Compruebe los tipos de datos de los siguientes datos:
        - 10
        - 9.8
        - 3.14
        - ['Asabeneh', 'Python', 'Finlandia']
        - Su nombre
        - Tu apellido
        - Tu país de nacimiento
        - Tu edad 
5.- Encuentra el valor del area de un triángulo, donde la base es 5cm y la altura es 4cm.
'''

# 1.- Comprueba la versión de Python en la terminal. (Versión que se está utilizando)
import sys

print("1.- Comprobando la versión de Python en la terminal:", sys.version)


# 2.- Realice las siguientes operaciones. Los operandos son 3 y 4.
print("2.- Operaciones:") 
print("Suma (3 + 4):", 3 + 4)
print("Resta (3 - 4):", 3 - 4)
print("Multiplicación (3 * 4):", 3 * 4)
print("División (3 / 4):", 3 / 4)
print("Exponencial (3 ** 4):", 3 ** 4)
print("Módulo (3 % 4):", 3 % 4)
print("División de piso (3 // 4):", 3 // 4)


# 3.- Imprimir un texto que muestre Su Nombre, Su Apellido, Su Edad y El Pais de Nacimiento.
nombre = "Juanito"
apellido = "Nieves"
edad = 32
pais_nacimiento = "Narnia"
print("3.- Mi nombre es:", nombre, apellido, "y tengo", edad, "años. Nací en", pais_nacimiento)


# 4.- Compruebe los tipos de datos de los siguientes datos:
print("4.- Comprobando Tipos de datos:")
print("Tipo de dato de 10:", type(10))
print("Tipo de dato de 9.8:", type(9.8))
print("Tipo de dato de 3.14:", type(3.14))
print("Tipo de dato de ['Asabeneh', 'Python', 'Finlandia']:", type(['Asabeneh', 'Python', 'Finlandia']))
print("Tipo de dato de mi nombre", nombre, ":", type(nombre))
print("Tipo de dato de mi apellido", apellido, ":", type(apellido))
print("Tipo de dato de mi pais de nacimiento", pais_nacimiento, ":", type(pais_nacimiento))
print("Tipo de dato de mi edad", edad, ":", type(edad))


# 5.- Encuentra el valor del area de un triángulo, donde la base es 5cm y la altura es 4cm.
base = 5
altura = 4
area = (base * altura) / 2
print("5.- El área de un triángulo con base", base, "cm y altura", altura, "cm es:", area)
