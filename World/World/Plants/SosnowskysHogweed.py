from Plants.Plant import Plant
from Animals.Animal import Animal
from Animals.CyberSheep import CyberSheep

class SosnowskysHogweed(Plant):
    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "SosnowskysHogweed", args[2], args[3], "#f5eba6")
        else:
            super().__init__( args[0], args[1], "SosnowskysHogweed", 10, 0, "#f5eba6")
    
    def giveBirth(self, x, y):
        return SosnowskysHogweed(x, y)

    def action(self):
        organisms = self._world.getOrganisms()
        for org in organisms:
            x = self._x; y = self._y; orgX = org.getX(); orgY = org.getY()
            if (orgX == x and orgY == y+1) or (orgX == x and orgY == y-1) or (orgX == x+1 and orgY == y) or (orgX == x-1 and orgY == y):
                if isinstance(org, Animal) == True and isinstance(org, CyberSheep) == False:
                    if org.isImmortal() == False:
                        org.setIsDead(True)
                        org.printInfo; print("is killed by SosnowskysHogweed")

        super().action()

    def deathwish(self, attacker):
        if attacker.isImmortal() == False:
            if isinstance(attacker, CyberSheep) == True:
                return False
            else:
                attacker.setIsDead(True)
                self._isDead = True
                attacker.printInfo(); print("died because of SosnowskysHogweed")
        return True


