# Tema: Funciones

# Ejercicio 1: Crea una función llamada 'saludar' que imprima por pantalla el mensaje 
# "¡Hola! Bienvenido al curso de Python.".
# Luego, llama o invoca a la función para que el mensaje se muestre.
# Escribe tu código debajo de esta línea:

def saludar():
    mensaje = "¡Hola! Bienvenido al curso de Python."
    print(mensaje)

saludar()


# Ejercicio 2: Crea una función llamada 'sumar' que reciba dos parámetros (a y b).
# La función debe retornar la suma de estos dos números.
# Luego, llama a la función pasándole dos números e imprime el resultado.
# Escribe tu código debajo de esta línea:

def sumar(a, b):
    resultado = a + b
    return resultado

resultado_suma = sumar(5, 3)
print("Resultado de la suma:", resultado_suma)


# Ejercicio 3: Crea una función llamada 'es_par' que reciba un número entero como parámetro.
# La función debe retornar True si el número es par, o False si es impar.
# Imprime el resultado de llamar a la función con el número 7 y con el número 10.
# Escribe tu código debajo de esta línea:

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print("¿7 es par?", es_par(7))
print("¿10 es par?", es_par(10))