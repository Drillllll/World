from Organism import Organism
from Def import Def
import random 

class Plant(Organism):

    def __init__(self, x, y, name, strength, initiative, color):
         super().__init__(x, y, name, strength, initiative, color)
    
    def action(self):
         i = random.randint(0, 19) #5% chance
         if i == 0:
            childPos = self._findPos(Def.UNDEFINED, Def.UNDEFINED)
            if childPos[0] != Def.UNDEFINED:
                child = self.giveBirth(childPos[0], childPos[1])
                self._world.addOrganism(child)
                      
    def collision(self):
        pass
    def goBack(self):
        pass





