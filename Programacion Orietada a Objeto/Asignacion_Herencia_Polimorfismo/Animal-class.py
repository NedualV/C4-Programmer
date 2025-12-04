class Animal:
    def hablar(self):
        pass  # Método vacío, definido en las hijas

class Perro(Animal):
    def hablar(self):
        return "¡Guau guau!"

class Gato(Animal):
    def hablar(self):
        return "¡Miau miau!"

# --- Prueba de Polimorfismo ---
animales = [Perro(), Gato()]

for animal in animales:
    print(f"El animal dice: {animal.hablar()}")