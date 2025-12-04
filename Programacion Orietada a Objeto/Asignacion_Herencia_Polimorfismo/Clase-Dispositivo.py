class Dispositivo:
    def encender(self):
        print("Encendiendo dispositivo...")

class Laptop(Dispositivo):
    def encender(self):
        print("Laptop: Iniciando sistema operativo Windows...")

class Telefono(Dispositivo):
    def encender(self):
        print("Teléfono: Mostrando logo de Android...")

# --- Prueba ---
mis_aparatos = [Laptop(), Telefono()]

for aparato in mis_aparatos:
    aparato.encender()