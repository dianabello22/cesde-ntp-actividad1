# Tema: Uso Avanzado de input() y Formateo de Strings

# Ejercicio 1: Pide al usuario que ingrese su color favorito usando input().
# Luego, imprime un mensaje que diga "Tu color favorito es [color]".
# Escribe tu código debajo de esta línea:

color = input("Ingresa tu color favorito: ")
print(f"Tu color favorito es {color}.")


# Ejercicio 2: Pide al usuario que ingrese su ciudad de residencia y su país de 
# origen (en dos variables e inputs separados).
# Luego usa f-strings para imprimir un mensaje como: 
# "Vives en [ciudad], [país]".
# Escribe tu código debajo de esta línea:

ciudad = input("Ingresa tu ciudad de residencia: ")
pais = input("Ingresa tu país de origen: ")

mensaje_ubicacion = f"Vives en {ciudad}, {pais}."
print(mensaje_ubicacion)


# Ejercicio 3: Pide al usuario que escriba una palabra sencilla y luego imprímela repetida 5 veces.
# (Multiplicación de cadenas con *)
# Escribe tu código debajo de esta línea:

palabra = input("Escribe una palabra: ")
repeticion = (palabra + " ") * 5

print("Palabra repetida 5 veces:")
print(repeticion)