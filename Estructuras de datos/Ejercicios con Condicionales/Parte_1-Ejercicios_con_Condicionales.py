# --- 1. Edad ---
edad = int(input("1. Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("-" * 20)

# --- 2. Positivo, Negativo o Cero ---
num = float(input("2. Introduce un número: "))
if num > 0:
    print("Es positivo")
elif num < 0:
    print("Es negativo")
else:
    print("Es cero")

print("-" * 20)

# --- 3. Par o Impar ---
num_par = int(input("3. Introduce un número entero: "))
if num_par % 2 == 0:
    print("Es par")
else:
    print("Es impar")

print("-" * 20)

# --- 4. Calificaciones ---
nota = int(input("4. Introduce una nota (0-100): "))
if nota >= 90:
    print("Aprobado con A")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

print("-" * 20)

# --- 5. Descuento en compra ---
monto = float(input("5. Ingresa el monto de la compra: "))
if monto > 500:
    descuento = monto * 0.10
    total = monto - descuento
    print(f"Descuento aplicado. Total a pagar: {total}")
else:
    print(f"Sin descuento. Total a pagar: {monto}")