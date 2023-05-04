from Animals.Animal import Animal

class Sheep(Animal):
    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "Sheep", args[2], args[3], "#ffffff")
        else:
            super().__init__( args[0], args[1], "Sheep", 4, 4, "#ffffff")

    def giveBirth(self, x, y):
         return Sheep(x, y)




