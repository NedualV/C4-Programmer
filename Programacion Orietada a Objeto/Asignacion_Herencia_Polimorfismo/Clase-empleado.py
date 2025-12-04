class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bono(self):
        return 0

class Gerente(Empleado):
    def calcular_bono(self):
        return self.salario * 0.20  # Bono del 20%

class Tecnico(Empleado):
    def calcular_bono(self):
        return self.salario * 0.10  # Bono del 10%

# --- Prueba ---
empleado1 = Gerente("Carlos", 50000)
empleado2 = Tecnico("Nedual", 30000)

print(f"Bono de {empleado1.nombre}: ${empleado1.calcular_bono()}")
print(f"Bono de {empleado2.nombre}: ${empleado2.calcular_bono()}")