from Animals.Animal import Animal
from Def import Def

class Human(Animal):
    #(x, y) or (x, y, strength, initiative, immortalRounds, cooldown)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "Human", args[2], args[3], "#8c03fc")
            self._immortalRounds = args[4]
            self._cooldown = args[5]
        else:
            super().__init__( args[0], args[1], "Human", 5, 4, "#8c03fc")
            self._immortalRounds = 0
            self._cooldown = 0

    def giveBirth(self, x, y):
         return Human(x, y)

    def action(self):
        newX = Def.UNDEFINED; newY = Def.UNDEFINED

        if self._immortalRounds > 0:
            self._immortalRounds = self._immortalRounds-1
        elif self._immortalRounds == 0:
            self._cooldown = self._cooldown+1

        key = self._world.getKey()
        if key == Def.UP:
            newX = self._x; newY = self._y-1
        if key == Def.DOWN:
            newX = self._x; newY = self._y+1
        if key == Def.LEFT:
            newX = self._x-1; newY = self._y
        if key == Def.RIGHT:
            newX = self._x+1; newY = self._y
        if key == Def.ABILITY and self._cooldown > 5:
            self._immortalRounds = 5
            self._cooldown = 0
            print("Power activated, remain immortality: ", self._immortalRounds, "cooldown:", self._cooldown)
            return

        if newX<0 or newX > self._world.getSizeX()-1 or newY<0 or newY>self._world.getSizeY()-1:
            pass
        else:
            self._prevX = self._x
            self._prevY = self._y
            self._x = newX
            self._y = newY

        print("remain immortality: ", self._immortalRounds, "cooldown:", self._cooldown)

    def isImmortal(self):
        if self._immortalRounds > 0:
            print("Human evades the attack")
            newPos = self._findPos(Def.UNDEFINED, Def.UNDEFINED)
            if newPos[0] != Def.UNDEFINED:
                self._x = newPos[0]
                self._y = newPos[1]
            else:
                super().action()
                self.collision()
            return True
        else:
            return False

    def printToSave(self):
        return str(self._x) +" "+ str(self._y) +" "+ str(self._name) +" "+ str(self._strength) +" "+ str(self._initiative) \
            +" "+ str(self._immortalRounds) +" "+ str(self._cooldown)+ " \n" 

