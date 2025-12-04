class CuentaBancaria:
    def __init__(self, titular, balance):
        self.titular = titular
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Depositado: ${cantidad}. Nuevo balance: ${self.balance}")

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Retirado: ${cantidad}. Nuevo balance: ${self.balance}")
        else:
            print("Fondos insuficientes.")

# --- Prueba ---
cuenta = CuentaBancaria("Maria Lopez", 1000)
cuenta.depositar(500)  # Saldo sube a 1500
cuenta.retirar(200)    # Saldo baja a 1300