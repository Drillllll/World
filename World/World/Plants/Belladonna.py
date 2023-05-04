from Plants.Plant import Plant
class Belladonna(Plant):
    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "Belladonna", args[2], args[3], "#171acf")
        else:
            super().__init__( args[0], args[1], "Belladonna", 99, 0, "#171acf")
    
    def giveBirth(self, x, y):
        return Belladonna(x, y)

    def deathwish(self, attacker):
        if attacker.isImmortal() == False:
            attacker.setIsDead(True)
            self._isDead = True
            attacker.printInfo(); print("died because of Belladonna")
        return True


