from animal import Animal

class Mamifero(Animal):
    listado = []
    numMamiferos = 0
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas

        Mamifero.listado.append(self)
        Mamifero.numMamiferos += 1

    @classmethod
    def cantidadMamifero():
        return Mamifero.numMamiferos

    @classmethod
    def crearCaballo(nombre,edad,genero):
        caballo = Mamifero(nombre,edad,"pradera",genero,True,4)
        Mamifero.caballos += 1

    @classmethod
    def crearLeon(nombre,edad,genero):
        leon = Mamifero(nombre,edad,"selva",genero,True,4)
        Mamifero.leones += 1
    
    def getPelaje(self):
        return self.pelaje

    def getPatas(self):
        return self.patas

