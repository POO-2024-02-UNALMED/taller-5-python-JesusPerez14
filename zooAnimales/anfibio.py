from animal import Animal

class Anfibio(Animal):
    listado = []
    numAnfibios = 0
    ranas = 0
    salamandras = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso

        Anfibio.listado.append(self)
        Anfibio.numAnfibios += 1
    
    @classmethod
    def cantidadAnfibios():
        return Anfibio.numAnfibios
    
    def movimiento():
        return "saltar"
    
    @classmethod
    def crearRana(nombre,edad,genero):
        rana = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        Anfibio.ranas += 1
    
    @classmethod
    def crearSalamandra(nombre,edad,genero):
        salamandra = Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        Anfibio.salamandras += 1

    def getColorPiel(self):
        return self.colorPiel
    
    def isVenenoso(self):
        return self.venenoso