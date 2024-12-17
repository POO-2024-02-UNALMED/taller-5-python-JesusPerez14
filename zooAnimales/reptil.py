from animal import Animal

class Reptil(Animal):
    listado = []
    numReptiles = 0
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas,largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola

        Reptil.listado.append(self)
        Reptil.numReptiles += 1

    @classmethod
    def cantidadReptiles():
        return Reptil.numReptiles

    def movimiento():
        return "reptar"

    @classmethod
    def crearIguana(nombre,edad,genero):
        iguana = Reptil(nombre,edad,"humedal",genero,"verde",3)
        Reptil.numReptiles += 1

    @classmethod
    def crearSerpientes(nombre,edad,genero):
        serpiente = Reptil(nombre,edad,"jungla",genero,"blanco",1)
        Reptil.numReptiles += 1
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getLargoCola(self):
        return self.largoCola

