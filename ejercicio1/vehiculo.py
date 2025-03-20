

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Vehiculo de color {self.color} con {self.ruedas} ruedas"

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for v in vehiculos_filtrados:
            print(v)
            
    else:
       print("no se han encontrado vehículos con ese número de ruedas")


