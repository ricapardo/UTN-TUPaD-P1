# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
multiplos_de_cuatro = list(range(4, 101, 4))
print(f"Lista de múltiplos de 4 entre 1 y 100: {multiplos_de_cuatro}")

# 2) Crear una lista con cinco elementos y mostrar el penúltimo.
mi_lista = ["ford", "fiat", "chevrolet", "VW", "toyota"]
penultimo_elemento = mi_lista[-2]
print(f"El penúltimo elemento de mi lista favorita es: {penultimo_elemento}")

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante.
lista_vacia = []
lista_vacia.append("hielo")
lista_vacia.append("fernet")
lista_vacia.append("coca")
print(f"Lista con palabras agregadas: {lista_vacia}")

# 4) Reemplazar el segundo y último valor de la lista “animales”.
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(f"Lista de animales modificada: {animales}")

# 5) Analizar el siguiente programa y explicar qué realiza.

str = "Explicacion del siguiente codigo: \n numeros = [8, 15, 3, 22, 7] \n numeros.remove(max(numeros)) \n print(numeros)"
print (str)
respuesta = 'Este programa define una lista llamada numeros. ' \
'Luego con la función max(numeros) encuentra el valor más grande dentro de esa lista, ' \
'que en este caso es 22. Luego, usa el método remove() que elimina la primera ocurrencia ' \
'de ese valor máximo de la lista. Por ultimo, imprime la lista numeros con los numeros que quedaron.' \
'La salida será [8, 15, 3, 7].'
print (respuesta)
# 6) Crear una lista con números del 10 al 30 (incluído), con saltos de 5 en 5 y mostrar los dos primeros.
lista_saltos = list(range(10, 31, 5))
dos_primeros = lista_saltos[:2]
print(f"Lista con saltos de 5: {lista_saltos}")
print(f"Los dos primeros elementos son: {dos_primeros}")

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos”.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "corsa"
autos[2] = "megane"
print(f"Lista de autos modificada: {autos}")

# 8) Crear una lista vacía "dobles" y agregar el doble de 5, 10 y 15 directamente con append.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(f"Lista de dobles: {dobles}")

# 9) Dada la lista “compras” realizar las siguientes modificaciones.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente.
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla.
print(f"Lista de compras modificada: {compras}")

# 10) Elaborar una lista anidada llamada “lista_anidada” con los elementos especificados.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(f"Lista anidada resultante: {lista_anidada}")