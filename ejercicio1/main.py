
from vehiculo import Vehiculo
from coche import Coche 
from bicicleta import Bicicleta
from camioneta import Camioneta
from motocicleta import Motocicleta

def main():
    vehiculos = {
        "vehiculo": Vehiculo("rojo", 4),
        "coche": Coche("azul", 4, 150, 2000),
        "bicicleta": Bicicleta("verde", 2, "urbana"),
        "camioneta": Camioneta(color="blanca", ruedas=4, velocidad=1000, cilindrada=4000, carga=2000),
        "motocicleta": Motocicleta(color="negra", ruedas=2, velocidad=200, cilindrada=1000)
    }

    print("Vehículos disponibles:")
    for key in vehiculos.keys():
        print(f"- {key}")

    eleccion = input("Elige un vehículo para obtener información: ").strip().lower()

    if eleccion in vehiculos:
        print(vehiculos[eleccion])
    else:
        print("Opción no válida. Por favor, elige un vehículo de la lista.")

if __name__ == "__main__":
    main()