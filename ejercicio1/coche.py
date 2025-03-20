from vehiculo import Vehiculo   
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Coche de color {self.color} con {self.ruedas} ruedas, velocidad {self.velocidad} km/h y cilindrada {self.cilindrada} cc"