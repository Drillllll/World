from Plants.Plant import Plant
class Grass(Plant):
    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "Grass", args[2], args[3], "#35ed07")
        else:
            super().__init__( args[0], args[1], "Grass", 0, 0, "#35ed07")
    
    def giveBirth(self, x, y):
        return Grass(x, y)



