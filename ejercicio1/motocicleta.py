from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):    
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Motocicleta de color {self.color} con {self.ruedas} ruedas, velocidad {self.velocidad} km/h y cilindrada {self.cilindrada} cc"
