# Python Tutorial

## Descripción
Este proyecto documenta mi camino de aprendizaje de Python desde cero, siguiendo los tutoriales de varios profesionales de desarrollo como lo es Brais Moure, Hola Mundo. Aquí encontrarás ejemplos de código, explicaciones y comentarios que me han ayudado a entender mejor este lenguaje de programación.

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Instalación](#instalación)
3. [Primeros Pasos](#primeros-pasos)
4. [Estructuras de Datos](#estructuras-de-datos)
5. [Funciones](#funciones)
6. [Módulos y Paquetes](#módulos-y-paquetes)
7. [Conclusiones](#conclusiones)

## Introducción
En esta sección, se proporciona una visión general del proyecto y los objetivos de mi aprendizaje de Python.
Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Fue creado por Guido van Rossum y lanzado por primera vez en 1991. Python es conocido por su sintaxis clara y legible, lo que lo hace ideal tanto para principiantes como para desarrolladores experimentados.

### Características Principales de Python
- **Sintaxis Sencilla y Clara**: La sintaxis de Python está diseñada para ser fácil de leer y escribir, lo que facilita el aprendizaje y la colaboración.
- **Tipado Dinámico**: Python es un lenguaje de tipado dinámico, lo que significa que no es necesario declarar el tipo de una variable al definirla.
- **Interpretado**: Python se ejecuta línea por línea, lo que permite una rápida iteración y prueba de código.
- **Multiplataforma**: Python se puede ejecutar en diferentes sistemas operativos como Windows, macOS y Linux.
- **Gran Biblioteca Estándar**: Python viene con una extensa biblioteca estándar que proporciona módulos y paquetes para realizar diversas tareas, desde manipulación de archivos hasta desarrollo web.

### Conceptos Básicos
- **Variables y Tipos de Datos**: En Python, las variables se utilizan para almacenar datos y pueden contener diferentes tipos de datos como enteros, flotantes, cadenas y booleanos.
- **Estructuras de Control**: Python utiliza estructuras de control como condicionales (`if`, `elif`, `else`) y bucles (`for`, `while`) para controlar el flujo del programa.
- **Funciones**: Las funciones en Python se definen utilizando la palabra clave `def` y se utilizan para encapsular bloques de código reutilizables.
- **Módulos y Paquetes**: Python permite organizar el código en módulos y paquetes, facilitando la reutilización y el mantenimiento del código.

Con esta base, estarás listo para comenzar tu viaje en el aprendizaje de Python y explorar sus diversas aplicaciones en el desarrollo de software.

## Instalación
Instrucciones sobre cómo instalar Python y las herramientas necesarias para seguir los tutoriales.
### Instalación de Python

#### Windows
1. Ve al sitio web oficial de Python: [python.org](https://www.python.org/).
2. Haz clic en "Downloads" y selecciona "Windows".
3. Descarga el instalador ejecutable.
4. Ejecuta el instalador y asegúrate de marcar la opción "Add Python to PATH".
5. Haz clic en "Install Now" y sigue las instrucciones del instalador.

#### macOS
1. Ve al sitio web oficial de Python: [python.org](https://www.python.org/).
2. Haz clic en "Downloads" y selecciona "macOS".
3. Descarga el instalador `.pkg`.
4. Abre el archivo descargado y sigue las instrucciones del instalador.

#### Linux
1. Abre una terminal.
2. Actualiza el índice de paquetes:
    ```bash
    sudo apt update
    ```
3. Instala Python con el siguiente comando:
    ```bash
    sudo apt install python3
    ```

### Instalación de Visual Studio Code

#### Windows y macOS
1. Ve al sitio web oficial de Visual Studio Code: [code.visualstudio.com](https://code.visualstudio.com/).
2. Haz clic en "Download" y selecciona tu sistema operativo.
3. Descarga el instalador y ejecútalo.
4. Sigue las instrucciones del instalador para completar la instalación.

#### Linux
1. Abre una terminal.
2. Descarga el paquete `.deb` desde el sitio web oficial de Visual Studio Code: [code.visualstudio.com](https://code.visualstudio.com/).
3. Instala el paquete con el siguiente comando:
    ```bash
    sudo apt install ./<nombre_del_paquete>.deb
    ```

### Extensiones de VS Code para Python
1. Abre Visual Studio Code.
2. Ve a la pestaña de extensiones (icono de cuadrados en la barra lateral izquierda).
3. Busca "Python" y selecciona la extensión oficial de Microsoft.
4. Haz clic en "Install".
5. Opcionalmente, instala otras extensiones útiles como "Pylint" para análisis de código y "Jupyter" para trabajar con notebooks.

Con estas herramientas instaladas, estarás listo para comenzar a escribir y ejecutar código en Python.

## Primeros Pasos
Aquí se documentan mis primeros scripts en Python, incluyendo comentarios y explicaciones sobre la sintaxis básica y los conceptos fundamentales.
### Hola Mundo
El primer programa que se suele escribir en cualquier lenguaje de programación es el clásico "Hola Mundo". En Python, esto se hace de la siguiente manera:
```python
print("Hola Mundo")
```
Este simple programa imprime la cadena "Hola Mundo" en la consola.

### Variables y Tipos de Datos
En Python, no es necesario declarar el tipo de una variable antes de usarla. Aquí hay algunos ejemplos de cómo se pueden definir diferentes tipos de variables:
```python
# Definición de variables
entero = 10
flotante = 10.5
cadena = "Hola"
booleano = True

# Imprimir variables
print(entero)
print(flotante)
print(cadena)
print(booleano)
```

### Operaciones Básicas
Python soporta varias operaciones aritméticas básicas como suma, resta, multiplicación y división:
```python
# Operaciones aritméticas
suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 5

# Imprimir resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
```

### Estructuras de Control
Las estructuras de control permiten dirigir el flujo del programa. Aquí hay ejemplos de condicionales y bucles:
```python
# Condicionales
if entero > 5:
    print("El número es mayor que 5")
elif entero == 5:
    print("El número es igual a 5")
else:
    print("El número es menor que 5")

# Bucles
# Bucle for
for i in range(5):
    print("Iteración", i)

# Bucle while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

### Funciones
Las funciones en Python se definen utilizando la palabra clave `def`. Aquí hay un ejemplo de una función simple que suma dos números:
```python
# Definición de una función
def sumar(a, b):
    return a + b

# Llamada a la función
resultado = sumar(10, 5)
print("Resultado de la suma:", resultado)
```

Estos son los primeros pasos básicos para comenzar a programar en Python. Con esta base, puedes empezar a explorar más características avanzadas del lenguaje.

## Estructuras de Datos
Ejemplos y explicaciones sobre las diferentes estructuras de datos en Python, como listas, tuplas, diccionarios y conjuntos.

## Funciones
Descripción y ejemplos de cómo definir y utilizar funciones en Python, incluyendo funciones lambda y recursivas.

## Módulos y Paquetes
Explicación sobre cómo organizar el código en módulos y paquetes, y cómo importar y utilizar bibliotecas externas.

## Conclusiones
Reflexiones finales sobre mi experiencia de aprendizaje y los próximos pasos en mi camino para dominar Python.
