from Def import Def
class fileHandler:
    def __init__(self, world):
        self._world = world

    def saveWorld(self):
        print("Saving")
        f = open("worldState.txt", "w")
            
        f.write(self._world.printToSave())

        organisms = self._world.getOrganisms()
        for o in organisms:
            f.write(o.printToSave())

        f.close
        
    def loadWorld(self):
        print("Loading")
        f = open("worldState.txt", "r")
        
        #world info
        line = f.readline()
        data = line.split(" ")
        worldRound = int(data[3])
        self._world.setRound(worldRound)

        #organisms
        for line in f:
            data = line.split(" ")
            if data[2] == "Human":
                self._world.loadOrganism(int(data[0]), int(data[1]), data[2], int(data[3]), int(data[4]), int(data[5]), int(data[6]))
            else:
                self._world.loadOrganism(int(data[0]), int(data[1]), data[2], int(data[3]), int(data[4]), Def.UNDEFINED, Def.UNDEFINED)
                
        f.close() 

