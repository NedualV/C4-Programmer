class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

# --- Prueba ---
rect = Rectangulo(10, 5)
print(f"El área del rectángulo es: {rect.calcular_area()}")