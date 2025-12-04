# --- 1. Números del 1 al 10 ---
print("1. Contando del 1 al 10:")
i = 1
while i <= 10:
    print(i)
    i += 1

print("-" * 20)

# --- 2. Sumar hasta que escriba 0 ---
print("2. Suma acumulativa (escribe 0 para terminar):")
suma_total = 0
while True:
    n = int(input("Ingresa un número: "))
    if n == 0:
        break
    suma_total += n
print(f"La suma total es: {suma_total}")

print("-" * 20)

# --- 3. Adivina el número secreto ---
secreto = 7
print("3. Adivina el número secreto")
intento = int(input("¿Cuál es el número?: "))
while intento != secreto:
    intento = int(input("Incorrecto, intenta de nuevo: "))
print("¡Correcto! Adivinaste el número.")

print("-" * 20)

# --- 4. Validar contraseña ---
print("4. Validación de seguridad")
clave = input("Ingresa la contraseña: ")
while clave != "1234":
    clave = input("Contraseña incorrecta. Inténtalo de nuevo: ")
print("Acceso concedido.")

print("-" * 20)

# --- 5. Contador regresivo ---
inicio = int(input("5. Ingresa un número para la cuenta regresiva: "))
while inicio >= 1:
    print(inicio)
    inicio -= 1