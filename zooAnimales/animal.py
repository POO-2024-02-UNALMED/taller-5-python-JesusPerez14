from anfibio import Anfibio
from ave import Ave
from mamifero import Mamifero
from pez import Pez
from reptil import Reptil

class Animal:
    totalAnimales = 0

    def __init__(self,nombre,edad,habitat,genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero

        Animal.totalAnimales += 1
        pass

    def movimiento():
        return "desplazarse"

    def totalPorTipo():
        return "Mamiferos : {}\nAves : {}\nReptiles : {}\nPeces : {}\nAnfibios : {}".format(Mamifero.numMamiferos,Ave.numAves,Reptil.numReptiles,Pez.numPeces,Anfibio.numAnfibios)

    def toString(self):
        return "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}".format(self.nombre,self.edad,self.habitat,self.genero)

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getHabitat(self):
        return self.habitat

    def getGenero(self):
        return self.genero
