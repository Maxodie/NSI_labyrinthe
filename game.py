import tkinter as tk
from PIL import ImageTk, Image
from States.mainMenuState import MainMenuState

class Game(tk.Tk):
    #Constructor/Destructor
    def __init__(self, grid_size):
        super().__init__()
        self.gridSize = grid_size#gridSize est ce qui permettra au jeu de s'adapter à une taille
        self.textures = {}
        self.currentStates = []#les states sont les états du jeu ex: le state main menu ou le state game

    #Functions
    def initWindow(self):
        #initialisation de la fenêtre
        self.title("Jeu Labyrinthe")
        self.resizable(False, False)
        self.geometry(f"{self.gridSize*20}x{self.gridSize*20+4*self.gridSize}")
        
    def loadTextures(self):
        #chargement des textures dans un dict
        for i in ["brick", "enemy", "player0", "player1", "win", "chest"]:#nombre deriere player désigne le skin du j1 et j2
            img = Image.open(f"Resources\\Images\\{i}.png")
            img = img.resize((self.gridSize, self.gridSize))
            texture = ImageTk.PhotoImage(img)
            self.textures[i] = texture

    def play(self):
        #fonction appelé dupuis le main
        self.initWindow()
        self.loadTextures()
        #ajoute le state main menu 
        self.currentStates.append(MainMenuState(self.gridSize, self.textures, self.currentStates, self))
        self.update()
        self.rootEvent()
        self.mainloop()

    def update(self):
        self.currentStates[-1].update()
        self.tkAfterUpdate = self.after(100, self.update)

    def rootEvent(self):
        #les event que le jeu possède en permanence
        self.bind("<Escape>", lambda e, : self.currentStates[-1].quitState())
        self.protocol("WM_DELETE_WINDOW", self.onQuit)
    
    def onQuit(self):
        #fermeture de la fenêtre
        while self.currentStates:
            self.currentStates[0].quitState()
