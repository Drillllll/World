from Plants.Plant import Plant
class Sonchus(Plant):
    #(x, y) or (x, y, strength, initiative)
    def __init__(self, *args):
        if len(args)>2:
            super().__init__( args[0], args[1], "Sonchus", args[2], args[3], "#ffff1f")
        else:
            super().__init__( args[0], args[1], "Sonchus", 0, 0, "#ffff1f")

    
    def giveBirth(self, x, y):
        return Sonchus(x, y)

    def action(self):
        for i in range(3):
            super().action()



