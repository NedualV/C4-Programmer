class Coche:
    def __init__(self, marca, velocidad_inicial):
        self.marca = marca
        self.velocidad = velocidad_inicial

    def acelerar(self, aumento):
        self.velocidad += aumento
        print(f"El {self.marca} aceleró. Nueva velocidad: {self.velocidad} km/h")

# --- Prueba ---
mi_auto = Coche("Toyota", 60)
mi_auto.acelerar(20) # Aumentamos 20 km/h