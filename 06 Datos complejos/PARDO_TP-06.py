# 1. Agrega nuevas frutas al diccionario
def agregar_frutas(precios):
    precios.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})
    return precios

# 2. Actualiza los precios de algunas frutas
def actualizar_precios(precios):
    precios.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})
    return precios

# 3. Devuelve una lista con solo los nombres de las frutas
def obtener_nombres_frutas(precios):
    return list(precios.keys())

# 4. Agenda telefónica: carga contactos y permite consultar uno
def agenda_telefonica():
    contactos = {}
    for i in range(5):
        nombre = f"Ricardo{i+1}"  # Simulación de entrada
        numero = f"351-1234-567{i}"  # Simulación de entrada
        contactos[nombre] = numero
    nombre_busqueda = "Contacto3"  # Simulación de búsqueda
    return contactos.get(nombre_busqueda, "Contacto no encontrado")

# 5. Palabras únicas y conteo de palabras
def analizar_frase(frase):
    palabras = frase.lower().split()
    unicas = set(palabras)
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return unicas, conteo

# 6. Promedio de notas de 3 alumnos
def promedio_alumnos():
    alumnos = {
        'Ana': (8, 7, 9),
        'Luis': (6, 5, 7),
        'Sofía': (9, 8, 10)
    }
    promedios = {nombre: sum(notas)/len(notas) for nombre, notas in alumnos.items()}
    return promedios

# 7. Operaciones con sets de estudiantes aprobados
def analizar_aprobados():
    parcial1 = {1, 2, 3, 4, 5}
    parcial2 = {4, 5, 6, 7}
    ambos = parcial1 & parcial2
    uno_solo = parcial1 ^ parcial2
    al_menos_uno = parcial1 | parcial2
    return ambos, uno_solo, al_menos_uno

# 8. Gestión de stock de productos
def gestionar_stock():
    stock = {'Yerba': 10, 'Azúcar': 5}
    producto = 'Yerba'
    cantidad = 3
    if producto in stock:
        stock[producto] += cantidad
    else:
        stock[producto] = cantidad
    return stock

# 9. Agenda con tuplas (día, hora)
def agenda_eventos():
    agenda = {
        ('Lunes', '10:00'): 'Reunión',
        ('Martes', '15:00'): 'Clase de Python'
    }
    consulta = agenda.get(('Lunes', '10:00'), 'No hay actividad')
    return consulta

# 10. Invertir diccionario país → capital a capital → país
def invertir_diccionario(dic):
    return {capital: pais for pais, capital in dic.items()}


# Función principal para probar todos los ejercicios
def main():
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    
    precios_frutas = agregar_frutas(precios_frutas)
    precios_frutas = actualizar_precios(precios_frutas)
    print("Frutas disponibles:", obtener_nombres_frutas(precios_frutas))

    print("Teléfono de Contacto3:", agenda_telefonica())

    frase = "Hola soy Ricardo y soy de Cordoba."
    unicas, conteo = analizar_frase(frase)
    print("Palabras únicas:", unicas)
    print("Frecuencia:", conteo)

    print("Promedios de alumnos:", promedio_alumnos())

    ambos, uno_solo, alguno = analizar_aprobados()
    print("Aprobaron ambos parciales:", ambos)
    print("Solo uno:", uno_solo)
    print("Al menos uno:", alguno)

    print("Stock actualizado:", gestionar_stock())

    print("Actividad en Lunes 10:00:", agenda_eventos())

    paises = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago'}
    print("Diccionario invertido:", invertir_diccionario(paises))


if __name__ == "__main__":
    main()
