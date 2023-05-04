from Def import Def
from fileHandler import fileHandler
from Organism import Organism
from Animals.Sheep import Sheep
from Animals.Wolf import Wolf
from Animals.Antelope import Antelope
from Animals.Turtle import Turtle
from Animals.Fox import Fox
from Animals.CyberSheep import CyberSheep
from Animals.Human import Human
from Plants.Grass import Grass
from Plants.Sonchus import Sonchus
from Plants.Guarana import Guarana
from Plants.Belladonna import Belladonna
from Plants.SosnowskysHogweed import SosnowskysHogweed

class World:

    def __init__(self, sizeX, sizeY, window):
        self._sizeY = sizeY
        self._sizeX = sizeX
        self._round = 0
        self._window = window
        self._organisms = []
        self._fileHandler = fileHandler(self)
        staticmethod(Organism.setWorld(self))
    
    def addOrganism(self, organism):
        self._organisms.append(organism)
    
    def addOrganismFromName(self, name, x, y):
        if name == "Sheep":
            self._organisms.append(Sheep(x, y))
        if name == "Wolf":
            self._organisms.append(Wolf(x, y))
        if name == "Antelope":
            self._organisms.append(Antelope(x, y))
        if name == "Turtle":
            self._organisms.append(Turtle(x, y))
        if name == "Fox":
            self._organisms.append(Fox(x, y))
        if name == "CyberSheep":
            self._organisms.append(CyberSheep(x, y))
        if name == "Grass":
            self._organisms.append(Grass(x, y))
        if name == "Sonchus":
            self._organisms.append(Sonchus(x, y))
        if name == "Guarana":
            self._organisms.append(Guarana(x, y))
        if name == "Belladonna":
            self._organisms.append(Belladonna(x, y))    
        if name == "SosnowskysHogweed":
            self._organisms.append(SosnowskysHogweed(x, y))
        if name == "Human":
            self._organisms.append(Human(x, y))
    
    def loadOrganism(self, x, y, name, strength, initiative, immortalRounds, cooldown):
        if name == "Sheep":
            self._organisms.append(Sheep(x, y, strength, initiative))
        if name == "Wolf":
            self._organisms.append(Wolf(x, y, strength, initiative))
        if name == "Antelope":
            self._organisms.append(Antelope(x, y, strength, initiative))
        if name == "Turtle":
            self._organisms.append(Turtle(x, y, strength, initiative))
        if name == "Fox":
            self._organisms.append(Fox(x, y, strength, initiative))
        if name == "CyberSheep":
            self._organisms.append(CyberSheep(x, y, strength, initiative))
        if name == "Grass":
            self._organisms.append(Grass(x, y, strength, initiative))
        if name == "Sonchus":
            self._organisms.append(Sonchus(x, y, strength, initiative))
        if name == "Guarana":
            self._organisms.append(Guarana(x, y, strength, initiative))
        if name == "Belladonna":
            self._organisms.append(Belladonna(x, y, strength, initiative))    
        if name == "SosnowskysHogweed":
            self._organisms.append(SosnowskysHogweed(x, y, strength, initiative))
        if name == "Human":
            self._organisms.append(Human(x, y, strength, initiative, immortalRounds, cooldown))
 
    def handleRound(self, key):
        self._round = self._round + 1
        print("New round: ", self._round)
        self._key = key
        self._window.hideSeleciton()
       
        #sort
        self._organisms.sort(key = lambda x: (-1*x.getInitiative(), x.getBirthNo()))
        #self._organisms.sort(key = lambda x: (x._initiative, x._birthNo))


        for o in self._organisms:
            o.setDidMove(False)

        for o in self._organisms:
            if o.getIsDead() == False:
                if o.getDidMove() == False:
                    #printing info about move
                    o.printInfo(); print("makes move")
                    o.action()
                    o.setDidMove(True)
                o.collision()



        #deleting dead organisms
        self._organisms = [o for o in self._organisms if o.getIsDead() == False]

        #printing number of organisms on board
        print("nr of organisms: ",len(self._organisms))

        self.printWorld()
    
    def handleSave(self):
        self._fileHandler.saveWorld()
    def handleLoad(self):
        self._organisms.clear()
        self._fileHandler.loadWorld()
        self.printWorld()

    def printWorld(self):
        self._window.clearButtons()
        length = len(self._organisms)
        for i in range(length):
            y = self._organisms[i].getY()
            x = self._organisms[i].getX()
            self._window.changeButtonColor(y, x, self._organisms[i].getColor())
    
    def isPosTaken(self, x, y):
        for o in self._organisms:
            if o.getX() == x and o.getY() == y:
                return True
        return False

    def printToSave(self):
        return str(self._sizeX) + " " + str(self._sizeY) + " " + "World " + str(self._round) + " " + "0" + " \n"

    def setRound(self, value):
        self._round = value

    def getOrganisms(self):
        return self._organisms
    def getRound(self):
        return self._round
    def getSizeX(self):
        return self._sizeX
    def getSizeY(self):
        return self._sizeY
    def getKey(self):
        return self._key
  