# 1) Programa para verificar si un usuario es mayor de edad
edad = int(input("Por favor, ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# 2) Programa para determinar si un alumno está aprobado o desaprobado
nota = float(input("Por favor, ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Programa para ingresar solo números pares
numero = int(input("Por favor, ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Programa para clasificar a una persona por su edad
edad_persona = int(input("Por favor, ingrese su edad: "))
if edad_persona < 12:
    print("Niño/a")
elif edad_persona >= 12 and edad_persona < 18:
    print("Adolescente")
elif edad_persona >= 18 and edad_persona < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Programa para verificar la longitud de una contraseña
contrasena = input("Por favor, ingrese su contraseña: ")
longitud_contrasena = len(contrasena)

if 8 <= longitud_contrasena <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Uso del paquete statistics, calculo de moda, mediana y media
import random
import statistics

# Define la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcula la moda, mediana y media

moda = statistics.mode(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)

# Determina el tipo de sesgo
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")


if media > mediana > moda:
    print("La distribución tiene un sesgo positivo o a la derecha.")
elif media < mediana < moda:
    print("La distribución tiene un sesgo negativo o a la izquierda.")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("No se puede determinar el sesgo claramente con los criterios dados.")


# 7) Programa para añadir un signo de exclamación si la frase termina en vocal
frase = input("Por favor, ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"

if frase and frase[-1] in vocales:
    frase_modificada = frase + "!"
    print(frase_modificada)
else:
    print(frase)

# 8) Programa para transformar el nombre según la opción del usuario
nombre = input("Por favor, ingrese su nombre: ")
opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para capitalizar: ")

if opcion == "1":
    nombre_transformado = nombre.upper()
    print(nombre_transformado)
elif opcion == "2":
    nombre_transformado = nombre.lower()
    print(nombre_transformado)
elif opcion == "3":
    nombre_transformado = nombre.title()
    print(nombre_transformado)
else:
    print("Opción inválida. Por favor, ingrese 1, 2 o 3.")


# 9) Programa para clasificar la magnitud de un terremoto
magnitud = float(input("Por favor, ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud < 3:
    categoria = "Muy leve"
elif 3 <= magnitud < 4:
    categoria = "Leve"
elif 4 <= magnitud < 5:
    categoria = "Moderado"
elif 5 <= magnitud < 6:
    categoria = "Fuerte"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte"
else:
    categoria = "Extremo"

print(f"La magnitud del terremoto es {magnitud}, clasificada como '{categoria}'.")

# 10) Programa para determinar la estación del año según el hemisferio y la fecha
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = input("¿Qué mes del año es?: ").lower()
dia = int(input("¿Qué día del mes es?: "))

if hemisferio == 'N':
    if mes == 'marzo' and dia >= 21 or mes == 'abril' or mes == 'mayo' or mes == 'junio' and dia < 20:
        estacion = "Primavera"
    elif mes == 'junio' and dia >= 21 or mes == 'julio' or mes == 'agosto' or mes == 'septiembre' and dia < 20:
        estacion = "Verano"
    elif mes == 'septiembre' and dia >= 21 or mes == 'octubre' or mes == 'noviembre' or mes == 'diciembre' and dia < 20:
        estacion = "Otoño"
    else:  # Diciembre >= 21 o enero o febrero o marzo < 20
        estacion = "Invierno"
elif hemisferio == 'S':
    if mes == 'marzo' and dia >= 21 or mes == 'abril' or mes == 'mayo' or mes == 'junio' and dia < 20:
        estacion = "Otoño"
    elif mes == 'junio' and dia >= 21 or mes == 'julio' or mes == 'agosto' or mes == 'septiembre' and dia < 20:
        estacion = "Invierno"
    elif mes == 'septiembre' and dia >= 21 or mes == 'octubre' or mes == 'noviembre' or mes == 'diciembre' and dia < 20:
        estacion = "Primavera"
    else:  # Diciembre >= 22 o enero o febrero o marzo < 20
        estacion = "Verano"
else:
    estacion = "Hemisferio inválido"

print(f"En el hemisferio {hemisferio}, en el mes de {mes} y el día {dia}, la estación es: {estacion}")