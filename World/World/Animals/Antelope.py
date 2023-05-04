from Animals.Animal import Animal
import random

class Antelope(Animal):

    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "Antelope", args[2], args[3], "#a6593f")
        else:
            super().__init__( args[0], args[1], "Antelope", 4, 4, "#a6593f")

    def giveBirth(self, x, y):
         return Antelope(x, y)

    def action(self):
        for i in range(2):
            super().action()
    
    def didEscape(self):
        i = random.randint(0, 1)
        if i == 0:
            super().action()
            self.printInfo(); print("escaped")
            self.collision()
            return True
        return False




