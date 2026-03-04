# Tema: Condicionales

# Ejercicio 1: Escribe un programa que verifique si la variable 'numero' es positiva, negativa o cero.
# Imprime un mensaje indicando el resultado.
numero = 7
# Escribe tu código debajo de esta línea:

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")


# Ejercicio 2: Dada la variable 'edad', escribe una condición que imprima "Mayor de edad" 
# si es 18 o mayor, y "Menor de edad" en caso contrario.
edad = 20
# Escribe tu código debajo de esta línea:

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")


# Ejercicio 3: Determina si un número es par o impar usando el operador módulo (%) 
# y muestra un mensaje acordemente.
numero_secreto = 14
# Escribe tu código debajo de esta línea:

if numero_secreto % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

