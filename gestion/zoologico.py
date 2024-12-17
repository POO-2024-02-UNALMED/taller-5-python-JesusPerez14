class Zoologico:
    def __init__(self,nombre,ubicacion,zonas):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = zonas
        pass
    
    def agregarZonas(self,zona):
        self.zonas.append(zona)

    def cantidadTotalAnimales():
        print("devuelve cantidad total de animales")

    def getNombre(self):
        return self.nombre
    
    def getUbicacion(self):
        return self.ubicacion
    
    def getZonas(self):
        return self.zonas