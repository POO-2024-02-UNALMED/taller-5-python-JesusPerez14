from zooAnimales.animal import Animal

class Zona:
    def __init__(self,nombre,zoo,animales):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = animales
        pass

    def __init__(self,nombre,zoo):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = None

    def __init__(self,nombre):
        self.nombre = nombre
        self.zoo = None
        self.animales = None 


def agregarAnimales(self,animal):
    self.animales.append(animal)

def cantidadAnimales():
    return Animal.totalAnimales