import math

# Ejercicio 1: Imprimir "Hola Mundo!"
# Esta función imprime el mensaje "Hola Mundo!".
def imprimir_hola_mundo():
    print("Hola Mundo!")


# Ejercicio 2: Saludar a un usuario
# Esta función toma un nombre como parámetro y devuelve un saludo personalizado.
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


# Ejercicio 3: Mostrar información personal
# Esta función toma nombre, apellido, edad y residencia como parámetros e imprime la información personal.
def informacion_personal(nombre, apellido, edad, residencia): # 
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}") # 


# Ejercicio 4: Calcular área y perímetro de un círculo
# Esta función calcula el área de un círculo dado su radio.
def calcular_area_circulo(radio): # 
    return math.pi * (radio ** 2) # 

# Esta función calcula el perímetro de un círculo dado su radio.
def calcular_perimetro_circulo(radio): # 
    return 2 * math.pi * radio # 


# Ejercicio 5: Convertir segundos a horas
# Esta función convierte una cantidad de segundos a horas.
def segundos_a_horas(segundos): # 
    return segundos / 3600 # 


# Ejercicio 6: Imprimir tabla de multiplicar
# Esta función imprime la tabla de multiplicar de un número dado del 1 al 10.
def tabla_multiplicar(numero): # 
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}") # 


# Ejercicio 7: Operaciones básicas con dos números
# Esta función recibe dos números y devuelve una tupla con la suma, resta, multiplicación y división.
def operaciones_basicas(a, b): # 
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Indefinido (división por cero)"
    return (suma, resta, multiplicacion, division) # 

# Ejercicio 8: Calcular IMC
# Esta función calcula el Índice de Masa Corporal (IMC) dados el peso en kg y la altura en metros.
def calcular_imc(peso, altura): # 
    return peso / (altura ** 2) # 

# Ejercicio 9: Convertir Celsius a Fahrenheit
# Esta función convierte una temperatura de grados Celsius a Fahrenheit.
def celsius_a_fahrenheit(celsius): 
    return (celsius * 9/5) + 32 


# Ejercicio 10: Calcular promedio de tres números
#Esta función calcula el promedio de tres números dados como parámetros.
def calcular_promedio(a, b, c): # 
    return (a + b + c) / 3 # 



def main():
    print("--- Ejercicio 1: Hola Mundo ---")
    imprimir_hola_mundo() 
    print("-" * 30)

    print("--- Ejercicio 2: Saludar Usuario ---")
    nombre_ej2 = input("Introduce tu nombre para el saludo: ") 
    print(saludar_usuario(nombre_ej2)) 
    print("-" * 30)

    print("--- Ejercicio 3: Información Personal ---")
    nombre_ej3 = input("Introduce tu nombre: ") 
    apellido_ej3 = input("Introduce tu apellido: ")
    edad_ej3 = input("Introduce tu edad: ") 
    residencia_ej3 = input("Introduce tu residencia: ") 
    informacion_personal(nombre_ej3, apellido_ej3, edad_ej3, residencia_ej3) 
    print("-" * 30)

    print("--- Ejercicio 4: Círculo (Área y Perímetro) ---")
    radio_ej4 = float(input("Introduce el radio del círculo: "))  
    area = calcular_area_circulo(radio_ej4) 
    perimetro = calcular_perimetro_circulo(radio_ej4)  
    print(f"El área del círculo es: {area:.2f}") 
    print(f"El perímetro del círculo es: {perimetro:.2f}") 
    print("-" * 30)

    print("--- Ejercicio 5: Segundos a Horas ---")
    segundos_ej5 = int(input("Introduce una cantidad de segundos: "))  
    horas = segundos_a_horas(segundos_ej5) 
    print(f"{segundos_ej5} segundos equivalen a {horas:.2f} horas.")  
    print("-" * 30)

    print("--- Ejercicio 6: Tabla de Multiplicar ---")
    numero_ej6 = int(input("Introduce un número para ver su tabla de multiplicar: ")) 
    tabla_multiplicar(numero_ej6)  
    print("-" * 30)

    print("--- Ejercicio 7: Operaciones Básicas ---")
    num1_ej7 = float(input("Introduce el primer número para operaciones básicas: "))
    num2_ej7 = float(input("Introduce el segundo número para operaciones básicas: "))
    suma, resta, multiplicacion, division = operaciones_basicas(num1_ej7, num2_ej7) 
    print(f"Suma: {suma}") 
    print(f"Resta: {resta}") 
    print(f"Multiplicación: {multiplicacion}") 
    print(f"División: {division}") 
    print("-" * 30)

    print("--- Ejercicio 8: Calcular IMC ---")
    peso_ej8 = float(input("Introduce tu peso en kilogramos: ")) 
    altura_ej8 = float(input("Introduce tu altura en metros: "))  
    imc = calcular_imc(peso_ej8, altura_ej8)
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

    print("--- Ejercicio 9: Celsius a Fahrenheit ---")
    celsius_ej9 = float(input("Introduce la temperatura en grados Celsius: ")) 
    fahrenheit = celsius_a_fahrenheit(celsius_ej9)  
    print(f"{celsius_ej9}°C son {fahrenheit:.2f}°F.") 
    print("-" * 30)

    print("--- Ejercicio 10: Calcular Promedio ---")
    num1_ej10 = float(input("Introduce el primer número para el promedio: "))  
    num2_ej10 = float(input("Introduce el segundo número para el promedio: ")) 
    num3_ej10 = float(input("Introduce el tercer número para el promedio: ")) 
    promedio_val = calcular_promedio(num1_ej10, num2_ej10, num3_ej10) 
    print(f"El promedio de los tres números es: {promedio_val:.2f}") 
    print("-" * 30)

if __name__ == "__main__":
    main()