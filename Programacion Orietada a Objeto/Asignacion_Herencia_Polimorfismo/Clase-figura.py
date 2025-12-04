import math

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

# --- Prueba ---
figuras = [Circulo(5), Cuadrado(4)]

for fig in figuras:
    # Usamos round() para limitar los decimales
    print(f"Área de la figura: {round(fig.area(), 2)}")