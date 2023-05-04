from Animals.Animal import Animal
class Wolf(Animal):
    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "Wolf", args[2], args[3], "#797d7f")
        else:
            super().__init__( args[0], args[1], "Wolf", 9, 5, "#797d7f")

    def giveBirth(self, x, y):
         return Wolf(x, y)
