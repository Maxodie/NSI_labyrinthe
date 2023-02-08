from States.State import State
import tkinter as tk

#à la fin d'une partie (parent de la fin solo et multi)
class EndState(State):
    def __init__(self, grid_size, textures, current_states, players_data, root):
        super().__init__(grid_size, textures, current_states, root)
        self.playersData = players_data
        self.initWinPanel()
        self.initPlayerWidgets()

    def __del__(self):
        try:
            while(self.canvas):
                self.canvas[0].destroy()
                del self.canvas[0]
        except:
            print("arrêt forcé ENDSTATE")
        return super().__del__()

    def initWinPanel(self):
        #créé le panel de victoire
        self.canvasState = tk.Canvas(self.root, bg="#4D4D4D", width=self.root.winfo_width(), height=self.root.winfo_height(), highlightthickness=0)
        self.canvasState.pack()
        self.canvasState.place(y=0, x=0)

        self.pixel = tk.PhotoImage(width=1, height=1)

        self.returnToMenuButton = tk.Button(self.canvasState, width=self.gridSize*7, height=self.gridSize*2.5, 
            text ="Retour au menu", font=f'Arial {int(self.gridSize/1.5)}', image=self.pixel, compound="center", anchor=tk.CENTER, command=self.quitState)
        self.returnToMenuButton.pack()
        self.returnToMenuButton.place(x=self.gridSize*10, y=self.gridSize*7, anchor=tk.CENTER)

        self.modelPoFormat = "{} : {}"
        self.canvas = []

    def initPlayerWidgets(self):
        #créé les widgets de tout les playerset affiche leur score
        for i in range(len(self.playersData["playerPo"])):
            self.canvas.append(tk.Canvas(self.canvasState, width=20*self.gridSize, height=2*self.gridSize, highlightthickness=0, bg='#727272'))
            self.canvas[-1].pack()
            self.canvas[-1].place(x=0, y=(10+i*2)*self.gridSize)

            self.canvas[-1].create_text(self.gridSize, self.gridSize, anchor=tk.W, text=self.modelPoFormat.format(": argent", self.playersData["playerPo"][i]), fill="white", font=f'Arial {int(self.gridSize/1.5)}')
            self.canvas[-1].create_text(10*self.gridSize, self.gridSize, anchor=tk.CENTER, text=self.modelPoFormat.format("Victoire(s)", self.playersData["playerWin"][i]), fill="white", font=f'Arial {int(self.gridSize/1.5)}')
            self.canvas[-1].create_text(19*self.gridSize, self.gridSize, anchor=tk.E, text=self.modelPoFormat.format("Mort(s)", self.playersData["playerDeath"][i]), fill="white", font=f'Arial {int(self.gridSize/1.5)}')

            self.canvas[-1].create_image(0, self.gridSize, anchor=tk.W, image=self.textures[f"player{i}"])

            if(len(self.canvas) > 1):
                self.canvas[-1].create_line(0, 0, 20*self.gridSize, 0)

    