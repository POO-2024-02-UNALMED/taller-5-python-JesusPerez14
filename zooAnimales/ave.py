from animal import Animal

class Ave(Animal):
    listado = []
    numAves = 0
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPlumas = colorPlumas

        Ave.listado.append(self)
        Ave.numAves += 1

    @classmethod
    def cantidadAves():
        return Ave.numAves
    
    def movimiento():
        return "volar"
    
    @classmethod
    def crearHalcon(nombre,edad,genero):
        halcon = Ave(nombre,edad,"montañas",genero,"cafe glorioso")
        Ave.halcones += 1
    
    @classmethod
    def crearAguila(nombre,edad,genero):
        aguila = Ave(nombre,edad,"montañas",genero,"blanco y amarillo")
    
    def getColorPlumas(self):
        return self.colorPlumas

