from Organism import Organism
from Def import Def
import random

class Animal(Organism):
    
    def __init__(self, x, y, name, strength, initiative, color):
         super().__init__(x, y, name, strength, initiative, color)
         self._prevX = x
         self._prevY = y

    def action(self):
        tried = [False, False, False, False]


        if self._x - 1 < 0:
            tried[Def.LEFT] = True
        if self._x + 1 > self._world.getSizeX() - 1:
            tried[Def.RIGHT] = True
        if self._y - 1 < 0:
            tried[Def.UP] = True
        if self._y + 1 > self._world.getSizeY() - 1:
            tried[Def.DOWN] = True;

        i = random.randint(0, 3)
        while tried[i] == True:
             i = random.randint(0, 3) 

        if i == Def.UP:
            newX = self._x; newY = self._y -1
        elif i == Def.DOWN:
            newX = self._x; newY = self._y +1
        elif i == Def.RIGHT:
            newX = self._x +1; newY = self._y
        elif i == Def.LEFT:
            newX = self._x -1; newY = self._y

        self._prevX = self._x
        self._prevY = self._y
        self._y = newY
        self._x = newX
    
    def goBack(self):
        self._x = self._prevX
        self._y = self._prevY

    def collision(self):
        organisms = self._world.getOrganisms()
        for defender in organisms:
            #same object
            if defender == self:
                pass
            #collision
            elif defender.getX() == self._x and defender.getY() == self._y and defender.getIsDead() == False:
                #same species
                if type(self) == type(defender):
                    #if are mature enough
                    if self._world.getRound() - self._birthRound >= 5 \
                        and self._world.getRound() - defender.getBirthRound() >= 5:

                        childPos = self._findPos(self._prevX, self._prevY)
                        if childPos[0] != Def.UNDEFINED:
                            child = self.giveBirth(childPos[0], childPos[1])
                            self._world.addOrganism(child) 
                            child.printInfo(); print("is born")
                    self.goBack()
                #different species
                else:
                    if defender.didReflect(self) == True:
                        pass
                    elif self.didEscape() == True or defender.didEscape() == True:
                        pass
                    elif defender.deathwish(self) == True:
                        pass

                    elif defender.getStrength() > self._strength:
                        if self.isImmortal() == False:
                            self.setIsDead(True)
                            defender.printInfo(); print("defeated", end=' '); self.printInfo()
                    elif defender.getStrength() < self._strength:
                        if defender.isImmortal() == False:
                            defender.setIsDead(True)
                            self.printInfo(); print("defeated", end=' '); defender.printInfo()
                    #eq strength
                    else:
                        if defender.isImmortal() == False:
                            #attacker wins
                            defender.setIsDead(True)
                            self.printInfo(); print("defeated", end=' '); defender.printInfo()
                return
                       




