from Def import Def
import random
class Organism():
    _birthNo = 0

    def __init__(self, x, y, name, strength, initiative, color):
        self._y = y
        self._x = x
        self._name = name
        self._strength = strength
        self._initiative = initiative
        self._color = color

        self._birthRound = self._world.getRound()
        self._birthNo = Organism._birthNo
        Organism._birthNo = Organism._birthNo + 1
        self._didMove = True
        self._isDead = False

    #returns [Def.UNDEFINED,Def.UNDEFINED] if there is no free position
    def _findPos (self, forbiddenX, forbiddenY):

        newX = Def.UNDEFINED; newY = Def.UNDEFINED
        tried = [False, False, False, False]

        x = self._x
        y = self._y
        
        if x - 1 < 0 or self._world.isPosTaken(x-1, y) or (x-1 == forbiddenX and y==forbiddenY):
            tried[Def.LEFT] = True
        if x + 1 > self._world.getSizeX() - 1 or self._world.isPosTaken(x+1, y) or (x+1 == forbiddenX and y==forbiddenY):
            tried[Def.RIGHT] = True
        if y - 1 < 0 or self._world.isPosTaken(x, y-1) or (x == forbiddenX and y-1==forbiddenY):
            tried[Def.UP] = True
        if y + 1 > self._world.getSizeY() - 1 or self._world.isPosTaken(x, y+1) or (x == forbiddenX and y+1==forbiddenY):
            tried[Def.DOWN] = True

        while True:
            if tried[Def.LEFT] == True and tried[Def.RIGHT] == True and tried[Def.UP] == True and tried[Def.DOWN] == True:
                break

            i = random.randint(0, 3)
            while tried[i] == True:
                i = random.randint(0, 3) 

            if i == Def.UP:
                newX = self._x; newY = self._y -1
                break
            elif i == Def.DOWN:
                newX = self._x; newY = self._y +1
                break
            elif i == Def.RIGHT:
                newX = self._x +1; newY = self._y
                break
            elif i == Def.LEFT:
                newX = self._x -1; newY = self._y
                break

        newPos = [newX, newY]
        return newPos

    def printInfo(self):
        print(self._name, "pos:", self._x, self._y, "str:", self._strength,"init & nr:", self._initiative, self._birthNo, end=' ')

    def printToSave(self):
        return str(self._x) +" "+ str(self._y) +" "+ str(self._name) +" "+ str(self._strength) +" "+ str(self._initiative) + " \n" 

    def didReflect(self, attacker):
        return False
    def didEscape(self):
        return False
    def deathwish(self, attacker):
        return False
    def isImmortal(self):
        return False

    def setWorld(world):
        Organism._world = world
    def setDidMove(self, value):
        self._didMove = value
    def setIsDead(self, value):
        self._isDead = value
    def setStrength(self, value):
        self._strength = value

    def getY(self):
        return self._y
    def getX(self):
        return self._x
    def getColor(self):
        return self._color
    def getDidMove(self):
        return self._didMove  
    def getIsDead(self):
        return self._isDead
    def getInitiative(self):
        return self._initiative
    def getBirthNo(self):
        return self._birthNo
    def getBirthRound(self):
        return self._birthRound
    def getStrength(self):
        return self._strength