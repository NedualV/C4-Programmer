class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones # Esto debe ser una lista de números

    def calcular_promedio(self):
        suma = sum(self.calificaciones)
        cantidad = len(self.calificaciones)
        if cantidad > 0:
            return suma / cantidad
        else:
            return 0

# --- Prueba ---
# Pasamos las notas como una lista entre corchetes []
alumno = Estudiante("Nedual Vargas", [99, 95, 95, 100]) 
promedio = alumno.calcular_promedio()

print(f"El promedio de {alumno.nombre} es: {promedio}")