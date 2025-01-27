"""
SISTEMA DE RESERVAS DE VUELOS
Imagina que estás desarrollando un sistema de reservas de vuelos para una
aerolínea. Crea un sistema de clases que permita a los usuarios realizar
reservas de vuelos. Aquí tienes una posible estructura:

- Clase base: `Vuelo`
 - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de
pasajeros

 - Métodos: agregar pasajero, verificar disponibilidad de asientos

- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)

 - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones,
trabajo)

Resuelve el problema creando instancias de estas clases y realizando
reservas para diferentes vuelos y tipos de vuelos especiales.
"""


class Vuelo:
    def __init__(self,numero_vuelo,origen,destino,capacidad_maxima):
        self.numero_vuelo=numero_vuelo
        self.origen_vuelo=origen
        self.destino_vuelo=destino
        self.capacidad_vuelo=capacidad_maxima
        self.pasajeros=[]
    
    def agregar_pasajero(self,nombre_pasajero):
        if self.capacidad_vuelo >=1:
            self.pasajeros.append(nombre_pasajero)
            self.capacidad_vuelo-=1
        else:
            print("vuelo con capasidad maxima")

    def verificar_asientos(self):
        print(f"quedan {self.capacidad_vuelo} asientos")
        if self.capacidad_vuelo <20:

            for nombres in self.pasajeros:

                print(f"los pasajeros son \n{nombres}")

class VuelosEspeciales(Vuelo):
    def __init__(self, numero_vuelo, origen, destino, capacidad_maxima, motivo):
        super().__init__(numero_vuelo, origen, destino, capacidad_maxima)
        self.motivo = motivo


vuelo1=Vuelo(110,"santiago","arica",20)
vuelo1.agregar_pasajero("jake")
vuelo1.verificar_asientos()
vuelo2=VuelosEspeciales(111,"santiago","arica",20,"vacaciones")
vuelo2.verificar_asientos()
vuelo2.agregar_pasajero("eduardo")
vuelo2.verificar_asientos()
    
