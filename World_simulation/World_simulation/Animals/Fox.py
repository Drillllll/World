from Animals.Animal import Animal
from Def import Def
import random

class Fox(Animal):
    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "Fox", args[2], args[3], "#ff7700")
        else:
            super().__init__( args[0], args[1], "Fox", 3, 7, "#ff7700")

    def giveBirth(self, x, y):
         return Fox(x, y)

    def action(self):
        tried = [False, False, False, False]
        x = self._x; y = self._y
        newX = x; newY = y

        if x - 1 < 0:
            tried[Def.LEFT] = True
        if x + 1 > self._world.getSizeX() - 1:
            tried[Def.RIGHT] = True
        if y - 1 < 0:
            tried[Def.UP] = True
        if y + 1 > self._world.getSizeY() - 1:
            tried[Def.DOWN] = True;

        while True:
            if tried[Def.LEFT] == True and tried[Def.RIGHT] == True and tried[Def.UP] == True and tried[Def.DOWN] == True:
                break

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
            
            #check if pos is occupied by a stronger organism
            organisms = self._world.getOrganisms()
            for o in organisms:
                if o.getX() == newX and o.getY() == newY and o.getIsDead() == False and o.getStrength() > self._strength:
                    tried[i] = True
                    break
            
            if tried[i] == False:
                self._prevX = self._x
                self._prevY = self._y
                self._y = newY
                self._x = newX
                return


        


