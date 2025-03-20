
from vehiculo import Vehiculo
from coche import Coche 
from bicicleta import Bicicleta
from camioneta import Camioneta
from motocicleta import Motocicleta

def main():
    vehiculo = Vehiculo("rojo", 4)
    coche = Coche("azul", 4, 150, 2000)
    bicicleta= Bicicleta("verde", 2, "urbana")
    camioneta = Camioneta(color="blanca",ruedas= 4, velocidad=1000,cilindrada=4000,carga=2000) 
    motocicleta= Motocicleta(color="negra",ruedas=2,velocidad=200,cilindrada=1000)
    print(vehiculo)
    print(coche)
    print(bicicleta)
    print(camioneta)
    print(motocicleta)

if __name__ == "__main__":
    main()