from coche import Coche
class Camioneta(Coche):
    def __init__(self, color, ruedas, carga, velocidad, cilindrada):
        super().__init__(color, ruedas,velocidad, cilindrada)    #duda
        self.carga = carga
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Camioneta de color {self.color} con {self.ruedas} ruedas, velocidad {self.velocidad} km/h, cilindrada {self.cilindrada} cc y carga {self.carga} kg"