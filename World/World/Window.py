from tkinter import *
from World import World
from Def import Def
import os

class Window():

    def __init__(self, x, y):
        self._world = World(x, y, self)
        self._sizeY = y
        self._sizeX = x
        self._master = Tk()
        self._master.title("symulator 188945")
        self._master.geometry("700x500")
        self._master.resizable(0, 0)
        self.__addButtons()
        self.__addSelectionButtons()

        self._world.addOrganismFromName("Human", 0, 0)
        self._world.printWorld()

        mainloop()

    def __addButtons(self):
        marginLeft = 200
        marginTop = 10
        size = 20

        saveButton = Button(self._master, text="Save", command=lambda:self.__handleSave())
        saveButton.place(bordermode=OUTSIDE, height=size, width=size*3,\
                   x=10, y=300)
        loadButton = Button(self._master, text="Load", command=lambda:self.__handleLoad())
        loadButton.place(bordermode=OUTSIDE, height=size, width=size*3,\
                   x=10, y=300 + size)

        self._buttons = [[Button(self._master) for j in range(self._sizeX)] for i in range(self._sizeY)]

        for i in range(self._sizeY):
            for j in range(self._sizeX):
                self._buttons[i][j].place(bordermode=OUTSIDE, height=size, width=size,\
                   x=marginLeft+size*j, y=marginTop+size*i)
                self._buttons[i][j].config(command=lambda y= i, x=j :self.__handleSelection(y, x))

        self._master.bind('<Left>', lambda ev: self.__handleNextRound(Def.LEFT))
        self._master.bind('<Right>', lambda ev: self.__handleNextRound(Def.RIGHT))
        self._master.bind('<Up>', lambda ev: self.__handleNextRound(Def.UP))
        self._master.bind('<Down>', lambda ev: self.__handleNextRound(Def.DOWN))
        self._master.bind('q', lambda ev: self.__handleNextRound(Def.ABILITY))

    def __handleNextRound(self, key):
        #clears console
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()

        self._world.handleRound(key)

    def __handleLoad(self):
        self.hideSeleciton()
        self._world.handleLoad()

    def __handleSave(self):
        self.hideSeleciton()
        self._world.handleSave()

    def __addSelectionButtons(self):
        self._selectionButtons = []
        species = ["Sheep", "Wolf", "Fox", "Antelope", "Turtle",\
                "Grass", "Sonchus", "Belladonna", "SosnowskysHogweed", "Guarana", "CyberSheep"]
        color = ["#ffffff","#797d7f","#ff7700","#a6593f","#07731f","#35ed07","#ffff1f","#171acf","#f5eba6","#cf1742","#a090ad"]
        for i in range(len(species)):
            self._selectionButtons.append(Button(self._master, text=species[i], bg=color[i], \
                command = lambda n=species[i]: self.__handleSelected(n)))
          
    
    def __handleSelected(self, species):
        self._world.addOrganismFromName(species, self._selectedX, self._selectedY)
        self._world.printWorld()
        self.hideSeleciton()
    
  
    def hideSeleciton(self):
        for i in range(len(self._selectionButtons)):
            self._selectionButtons[i].place_forget()

    def __handleSelection(self, y, x):
        if self._world.isPosTaken(x, y) == False:
            self._selectedY = y
            self._selectedX = x
            w, h, marginTop, marginLeft = 120, 25, 10, 10
            for i in range(len(self._selectionButtons)):
                 self._selectionButtons[i].place(bordermode=OUTSIDE, height=h, width=w,\
                       x=marginLeft, y=marginTop+h*i)
        else:
            print("Position is occupied")
    
    def changeButtonColor(self, y, x, color):
        self._buttons[y][x].configure(bg = color)

    #clears board
    def clearButtons(self):
         for i in range(self._sizeY):
            for j in range(self._sizeX):
                self._buttons[i][j].configure(bg = "#000000")