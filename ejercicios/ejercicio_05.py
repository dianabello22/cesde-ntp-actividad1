# Tema: Ciclos

# Ejercicio 1: Escribe un programa que utilice un ciclo (for o while) para imprimir todos 
# los números del 1 al 10.
# Escribe tu código debajo de esta línea:

print("Números del 1 al 10:")
for numero in range(1, 11):
    print(numero)


# Ejercicio 2: Utiliza un ciclo for para imprimir todos los números pares del 2 al 10 inclusive.
# Escribe tu código debajo de esta línea:

print("Números pares del 2 al 10:")
for numero in range(2, 11, 2):
    print(numero)


# Ejercicio 3: Usa un ciclo while para calcular la suma de los números del 1 al 5. 
# Imprime el resultado final (debe ser 15).
# Escribe tu código debajo de esta línea:

contador = 1
suma_acumulativa = 0

while contador <= 5:
    suma_acumulativa += contador
    contador += 1

print("La suma acumulativa del 1 al 5 es:", suma_acumulativa)