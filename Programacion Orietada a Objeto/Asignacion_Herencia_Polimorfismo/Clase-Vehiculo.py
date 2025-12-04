class Vehiculo:
    def mover(self):
        print("El vehículo se está moviendo.")

class Carro(Vehiculo):
    def mover(self):
        print("El carro está conduciendo por la carretera.")

class Bicicleta(Vehiculo):
    def mover(self):
        print("La bicicleta está pedaleando por la ciclovía.")

# --- Prueba ---
mi_carro = Carro()
mi_bici = Bicicleta()

mi_carro.mover()
mi_bici.mover()