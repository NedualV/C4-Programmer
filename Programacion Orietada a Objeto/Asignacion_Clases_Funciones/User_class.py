class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Usuario: {self.nombre}")
        print(f"Edad: {self.edad} años")

# --- Prueba ---
persona = Usuario("Nedual Vargas", 23)
persona.mostrar_datos()