from Plants.Plant import Plant
class Guarana(Plant):
    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "Guarana", args[2], args[3], "#cf1742")
        else:
            super().__init__( args[0], args[1], "Guarana", 0, 0, "#cf1742")
    
    def giveBirth(self, x, y):
        return Guarana(x, y)

    def deathwish(self, attacker):
        oldStr = attacker.getStrength()
        attacker.setStrength(oldStr + 3)
        self._isDead = True
        return True


