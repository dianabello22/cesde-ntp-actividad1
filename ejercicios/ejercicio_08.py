# Tema: Iteración de Colecciones

# Ejercicio 1: Dada la siguiente lista de frutas, utiliza un ciclo 'for' para imprimir 
# cada fruta en mayúsculas.
frutas = ["manzana", "banana", "cereza", "naranja"]
# Escribe tu código debajo de esta línea:

for fruta in frutas:
    print(fruta.upper())


# Ejercicio 2: Tienes un diccionario con las calificaciones de un estudiante. 
# Itera sobre el diccionario e imprime un mensaje con el formato: 
# "En la materia X, la calificación es Y".
calificaciones = {"Matemáticas": 9.5, "Historia": 8.0, "Ciencias": 10.0}
# Escribe tu código debajo de esta línea:

for materia, nota in calificaciones.items():
    print("En la materia", materia, "la calificación es", nota)


# Ejercicio 3: Dada una lista de números, usa un ciclo para iterar sobre ellos y 
# crear una nueva lista llamada 'pares' que contenga solo los números que son divisibles por 2. 
# Imprime la nueva lista.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
# Escribe tu código debajo de esta línea:

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

