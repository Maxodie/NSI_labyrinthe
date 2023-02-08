import tkinter as tk

#Le gui du joueur en jeu
class PlayerGUIManager:
    #Constructor/Destructors
    def __init__(self, root, game, players_data, player_number, textures, grid_size):
        self.game = game
        self.playersData = players_data
        self.playerNumber = player_number
        self.textures = textures
        self.gridSize = grid_size
        self.initGui(root)

    def __del__(self):
        try:
            if(self.mainCanvas):
                self.mainCanvas.destroy()
                self.mainCanvas = None
            if(self.canvas):
                for i in range(len(self.canvas)):
                    if(self.canvas[i]):
                        self.canvas[i].destroy()
                        self.canvas[i] = None
        except:
            print("arrêt forcé GUIMANAGER")

    #Functions
    def initGui(self, root):
        #initialise les liste des texts et graphics pour le gui des joueurs
        self.mainCanvas = tk.Canvas(root, width=20*self.gridSize, height=4*self.gridSize, highlightthickness=0)
        self.mainCanvas.pack()
        self.mainCanvas.place(x=0, y=2*(len(self.playersData["player"])*self.gridSize))

        self.modelLifeFormat = "vie: {}"
        self.modelPoFormat = "argent: {}"
        self.canvas = []
        self.playerLifeBackground = []
        self.playerLifeFill = []
        self.playerLifeText = []
        self.playerPoText = []
        self.currentLvlText = None

    def createPlayerGUI(self, player):
        #créé un gui pour les joueurs avec les donnés de self.playerData et du joueur concerné
        self.canvas.append(tk.Canvas(self.mainCanvas, width=20*self.gridSize, height=2*self.gridSize, highlightthickness=0, bg='#D1D1D1'))
        self.canvas[-1].pack()
        if(self.playerNumber > 1):
            self.canvas[-1].place(x=0, y=2*(len(self.playersData["player"])*self.gridSize))
        else:
            self.canvas[-1].place(x=0, y=self.gridSize)

        self.playerLifeBackground.append(self.canvas[-1].create_rectangle(0.2*self.gridSize, 0.2*self.gridSize, 8.5*self.gridSize, 1.8*self.gridSize, fill="grey"))
        self.playerLifeFill.append(self.canvas[-1].create_rectangle(0.2*self.gridSize, 0.2*self.gridSize, 8.5*self.gridSize, 1.8*self.gridSize, fill="red"))
        width = abs(8.5*self.gridSize - 0.2*self.gridSize)+0.2*self.gridSize
        height = abs(1.8*self.gridSize - 0.2*self.gridSize)+0.2*self.gridSize

        self.playerLifeText.append(self.canvas[-1].create_text(width/2, height/2, anchor=tk.CENTER, text=self.modelLifeFormat.format(player.currentLife), fill="black", font=(f'Arial {self.gridSize}')))
        self.playerPoText.append(self.canvas[-1].create_text(20*self.gridSize, 0, anchor=tk.NE, text=self.modelPoFormat.format(player.po), fill="black", font=(f'Arial {self.gridSize}')))
        if(not self.currentLvlText):
            self.currentLvlText = self.canvas[-1].create_text(10*self.gridSize, 0, anchor=tk.N, text=(f"lvl:{self.game.currentLvlId}"), fill="black", font=(f'Arial {int(self.gridSize/2)}'))

        self.canvas[-1].create_image(0.5*self.gridSize, self.gridSize, anchor=tk.W, image=self.textures["player{}".format(len(self.playersData["player"]))])

        if(len(self.canvas) > 1):
            self.canvas[-1].create_line(0, 0, 20*self.gridSize, 0)

    def updatePlayersGUI(self):
        #update le text des stats et le fill de la vie de chaques joueurs
        for i in range(len(self.playersData["player"])):
            x0, y0, x1, y1 = self.canvas[i].coords(self.playerLifeBackground[i])
            x1 = (x1-x0)*(self.playersData["player"][i].currentLife/self.playersData["player"][i].startLife)+x0
            self.canvas[i].coords(self.playerLifeFill[i], x0, y0, x1, y1)

            self.canvas[i].itemconfig(self.playerLifeText[i], text=self.modelLifeFormat.format(self.playersData["player"][i].currentLife))
            self.canvas[i].itemconfig(self.playerPoText[i], text=self.modelPoFormat.format(self.playersData["player"][i].po))

    def clearPlayerGUI(self):
        #clear le gui de tout les joueurs et reset les listes
        for i in range(len(self.canvas)):
            if(self.canvas[i]):
                self.canvas[i].delete("all")
        
        self.canvas = []
        self.playerLifeBackground = []
        self.playerLifeFill = []
        self.playerLifeText = []
        self.playerPoText = []
        self.currentLvlText = None