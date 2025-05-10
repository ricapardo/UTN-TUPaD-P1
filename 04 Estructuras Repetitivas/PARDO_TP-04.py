#1) Números del 0 al 100 en orden creciente:
for numero in range(101):
    print(numero)

#2) Cantidad de dígitos de un número entero:
numero_str = input("Ingresa un número entero: ")
cantidad_digitos = len(numero_str)
print(f"El número ingresado tiene {cantidad_digitos} dígitos.")

#3) Suma de números entre dos valores (excluyéndolos):
valor1 = int(input("Ingresa el primer número entero: "))
valor2 = int(input("Ingresa el segundo número entero: "))

suma = 0
if valor1 < valor2:
    for numero in range(valor1 + 1, valor2):
        suma += numero
elif valor2 < valor1:
    for numero in range(valor2 + 1, valor1):
        suma += numero
else:
    print("Los números ingresados son iguales, no hay números entre ellos.")

if valor1 != valor2:
    print(f"La suma de los números entre {valor1} y {valor2} (excluyéndolos) es: {suma}")

#4) Suma de números ingresados hasta que se ingrese 0:
suma_total = 0
numero = int(input("Ingresa un número entero (ingresa 0 para detener): "))
while numero != 0:
    suma_total += numero
    numero = int(input("Ingresa un número entero (ingresa 0 para detener): "))
print(f"La suma total de los números ingresados es: {suma_total}")

#5) Juego de adivinar un número aleatorio:
import random

numero_aleatorio = random.randint(0, 9)
intentos = 1
intento = int(input("Adivina el número (entre 0 y 9): "))
while intento != numero_aleatorio:
    if intento < numero_aleatorio:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
print(f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")

#6) Números pares del 100 al 0 en orden decreciente:
for numero in range(100, -1, -2):
    print(numero)

#7) Suma de números del 0 a un número entero positivo:
numero_limite = int(input("Ingresa un número entero positivo: "))

if numero_limite < 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    suma = 0
    for numero in range(numero_limite + 1):
        suma += numero
    print(f"La suma de los números desde 0 hasta {numero_limite} es: {suma}")

#8) Conteo de números pares, impares, positivos y negativos (para 100 números):
CANTIDAD_NUMEROS = 5  # Cambiar a 100 para la versión final
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Por favor, ingresa {CANTIDAD_NUMEROS} números enteros:")

for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Ingresa el número {i + 1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"\nDe los {CANTIDAD_NUMEROS} números ingresados:")
print(f"  - {pares} son pares.")
print(f"  - {impares} son impares.")
print(f"  - {positivos} son positivos.")
print(f"  - {negativos} son negativos.")

#9) Cálculo de la media de 100 números:
CANTIDAD_NUMEROS = 5  # Cambiar a 100 para la versión final
suma = 0
contador = 0

print(f"Por favor, ingresa {CANTIDAD_NUMEROS} números enteros:")
for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"\nLa media de los {contador} números ingresados es: {media}")
else:
    print("No se ingresaron números para calcular la media.")

#10) Inversión del orden de los dígitos de un número:
numero = int(input("Ingresa un número entero: "))
numero_original = abs(numero)  # Trabajamos con el valor absoluto para la inversión
numero_invertido = 0

while numero_original > 0:
    ultimo_digito = numero_original % 10
    numero_invertido = (numero_invertido * 10) + ultimo_digito
    numero_original //= 10

if numero < 0:
    print(f"El número invertido es: -{numero_invertido}")
else:
    print(f"El número invertido es: {numero_invertido}")