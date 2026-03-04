# Tema: Input y Casting (Conversión de tipos)

# Ejercicio 1: Pide al usuario que ingrese su nombre usando input() y luego imprime un saludo 
# personalizado que incluya su nombre.
# Escribe tu código debajo de esta línea:

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}, ¡Bienvenido al programa!")


# Ejercicio 2: Pide al usuario que ingrese su edad como texto.
# Convierte esa edad a un número entero y calcula cuántos años tendrá en 2050.
# Escribe tu código debajo de esta línea:

edad_texto = input("Ingresa tu edad: ")
edad = int(edad_texto)  # Conversión a entero

edad_2050 = edad + 26   # Cálculo
print(f"En el año 2050 tendrás {edad_2050} años.")


# Ejercicio 3: Pide al usuario que ingrese el precio de un producto.
# Convierte el valor ingresado a float y calcula el precio con 20% de descuento.
# Escribe tu código debajo de esta línea:

precio_texto = input("Ingresa el precio del producto: ")
precio = float(precio_texto)  # Conversión a decimal

descuento = precio * 0.20
precio_final = precio - descuento

print(f"El precio con 20% de descuento es: {precio_final}")