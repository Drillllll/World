from Animals.Animal import Animal
import random

class Turtle(Animal):
    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "Turtle", args[2], args[3], "#07731f")
        else:
            super().__init__( args[0], args[1], "Turtle", 2, 1, "#07731f")

    def giveBirth(self, x, y):
         return Turtle(x, y)

    def action(self):
        i = random.randint(0, 3)
        if i ==0:
            super().action();

    def didReflect(self, attacker):
        if attacker.getStrength() < 5:
            attacker.goBack()
            self.printInfo(); print("reflected the attack")
            return True
        return False