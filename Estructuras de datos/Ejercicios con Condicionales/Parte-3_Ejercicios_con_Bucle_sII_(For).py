# --- 1. Tabla de multiplicar ---
num_tabla = int(input("1. ¿De qué número quieres la tabla?: "))
for i in range(1, 11):
    print(f"{num_tabla} x {i} = {num_tabla * i}")

print("-" * 20)

# --- 2. Pedir 10 números y sumar ---
print("2. Introduce 10 números para sumar:")
suma_diez = 0
for i in range(10):
    n = float(input(f"Número {i+1}: "))
    suma_diez += n
print(f"La suma total es: {suma_diez}")

print("-" * 20)

# --- 3. Factorial ---
num_fact = int(input("3. Calcular factorial de: "))
factorial = 1
for i in range(1, num_fact + 1):
    factorial *= i
print(f"El factorial de {num_fact} es {factorial}")

print("-" * 20)

# --- 4. Pares entre 1 y 50 ---
print("4. Números pares entre 1 y 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ") # El end=" " imprime en horizontal
print() # Salto de línea final

print("-" * 20)

# --- 5. Promedio de 5 notas ---
print("5. Calculadora de promedio (5 notas):")
suma_notas = 0
for i in range(5):
    calificacion = float(input(f"Ingresa la nota {i+1}: "))
    suma_notas += calificacion
promedio = suma_notas / 5
print(f"El promedio final es: {promedio}")