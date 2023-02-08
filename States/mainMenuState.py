from PIL import ImageTk, Image
from States.State import State
import tkinter as tk
import tkinter.font as tkFont
from States.soloPlayerGameState import SoloPlayerGameState
from States.MultiPlayerGameState import MultiPlayerGameState

#le menu principal 
class MainMenuState(State):
    #Constructors / Destructors
    def __init__(self, grid_size, textures, current_states, root):
        super().__init__(grid_size, textures, current_states, root)
        self.initMenu()

    def __del__(self):
        return super().__del__()

    #functions
    def initMenu(self):
        #créé tout les widgets et les graphics du menu
        self.canvasState = tk.Canvas(self.root, bg="#199AC0", highlightthickness=0)
        self.canvasState.pack(fill=tk.BOTH, expand=tk.YES)

        helv36 = tkFont.Font(family='Veranda', size=int(self.gridSize/1.3), weight=tkFont.BOLD)
        self.pixel = tk.PhotoImage(width=1, height=1)

        self.canvasStateStartOnePlayerButton = tk.Button(self.canvasState, width=self.gridSize*7, height=self.gridSize*2.5, 
            text ="1 joueur", font=helv36, image=self.pixel, compound="center", anchor=tk.CENTER, command=self.playSoloGame)
        self.canvasStateStartTwoPlayerButton = tk.Button(self.canvasState, width=self.gridSize*7, height=self.gridSize*2.5, 
            text ="2 joueur", font=helv36, image=self.pixel, compound="center", anchor=tk.CENTER, command=self.playMultiGame)

        self.canvasStateStartOnePlayerButton.pack()
        self.canvasStateStartTwoPlayerButton.pack()
        
        self.canvasStateStartOnePlayerButton.place(x=self.gridSize*2, y=self.gridSize*8)
        self.canvasStateStartTwoPlayerButton.place(x=self.gridSize*2, y=self.gridSize*12)
    
        self.playerMenuTexture = []
        for i in range(2):
            img = Image.open(f"Resources\\Images\\player{i}.png")
            img = img.resize((self.gridSize*6, self.gridSize*6))
            self.playerMenuTexture.append(ImageTk.PhotoImage(img))
        self.canvasState.create_image(self.gridSize*12, self.gridSize*5, anchor=tk.NW, image=self.playerMenuTexture[0])
        self.canvasState.create_image(self.gridSize*12, self.gridSize*12, anchor=tk.NW, image=self.playerMenuTexture[1])

    def playSoloGame(self):
        #lancer une partie solo
        self.currentStates.append(SoloPlayerGameState(self.gridSize, self.textures, self.currentStates, 
            1, [("left arrow", "right arrow", "up arrow", "down arrow")], self.root))

    def playMultiGame(self):
        #lancer une partie à deux
        self.currentStates.append(MultiPlayerGameState(self.gridSize, self.textures, self.currentStates, 
            2, [("left arrow", "right arrow", "up arrow", "down arrow"), ("q", "d", "z", "s")], self.root))