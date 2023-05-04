from Animals.Animal import Animal
from Def import Def
import math

class CyberSheep(Animal):
    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "CyberSheep", args[2], args[3], "#a090ad")
        else:
            super().__init__( args[0], args[1], "CyberSheep", 11, 4, "#a090ad")

    def action(self):
        from Plants.SosnowskysHogweed import SosnowskysHogweed
        newX = Def.UNDEFINED; newY = Def.UNDEFINED
        preyDistance = Def.UNDEFINED;

        organisms = self._world.getOrganisms()
        for o in organisms:
            if isinstance(o, SosnowskysHogweed) == True and o.getIsDead() == False:
                dx = abs(o.getX() - self._x)
                dy = abs(o.getY() - self._y)
                distance = math.sqrt(dy ** 2 + dx ** 2)
                if preyDistance == Def.UNDEFINED:
                    preyDistance = distance; preyX = o.getX(); preyY= o.getY()
                elif distance < preyDistance:
                    preyDistance = distance; preyX = o.getX(); preyY= o.getY()
    
        if preyDistance != Def.UNDEFINED:
            if preyX > self._x:
                self._x = self._x+1
            elif preyX < self._x:
                self._x = self._x-1
            elif preyY > self._y:
                self._y = self._y+1
            elif preyY < self._y:
                self._y = self._y-1
        else:
            super().action()

