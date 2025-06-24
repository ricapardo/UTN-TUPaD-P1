# Ejercicio 1: Factorial recursivo
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Ejercicio 2: Serie de Fibonacci recursiva
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Ejercicio 3: Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Ejercicio 4: Conversión de decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# Ejercicio 5: Verificar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejercicio 6: Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

# Ejercicio 7: Contar bloques para construir pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Ejercicio 8: Contar ocurrencias de un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

# Función principal para demostrar el funcionamiento
def main():
    print("Factoriales del 1 al 5:")
    for i in range(1, 6):
        print(f"{i}! = {factorial(i)}")

    print("\nSerie de Fibonacci hasta la posición 7:")
    for i in range(8):
        print(f"F({i}) = {fibonacci(i)}")

    print("\nPotencia 2^5:", potencia(2, 5))
    print("Binario de 10:", decimal_a_binario(10) or "0")
    print("¿'reconocer' es palíndromo?:", es_palindromo("reconocer"))
    print("Suma de dígitos de 1234:", suma_digitos(1234))
    print("Bloques para pirámide de base 4:", contar_bloques(4))
    print("Cantidad de dígitos '2' en 12233421:", contar_digito(12233421, 2))

if __name__ == "__main__":
    main()
