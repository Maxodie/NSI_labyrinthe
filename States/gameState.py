from States.State import State
import tkinter as tk
from player import Player, PlayerState
from mapManager import MapManager
from guiManager import PlayerGUIManager

#le parent du state du jeu (il y a le solo et le multi)
class GameState(State):
    #Constructor / Destructor
    def __init__(self, grid_size, textures, current_states, player_number, player_inputs_map, root):
        super().__init__(grid_size, textures, current_states, root)
        self.playerNumber = player_number
        self.playerInputsMap: tuple(tuple) = player_inputs_map#les input des/du joueur(s)
        self.tkAfterUpdate = None#pour boucler la methode update

        self.initGame()
        self.start()

    def __del__(self):
        try:
            self.playerGUIManager.__del__()
        except:
            print("arrêt forcé GAMESTATE")
        return super().__del__()

    #Functions
    def initGame(self):
        #init les parametres du jeu, le gui, la map, ect..
        self.canvasState = tk.Canvas(self.root, width=self.gridSize*20, height=self.gridSize*20, bg="#E1B461", highlightthickness=0)
        self.canvasState.pack()
        self.canvasState.place(y=4*self.gridSize)

        self.currentLvlId = 0
        self.playersData = {"player" : [], "playerPo" : [], "playerWin" : [], "playerDeath" : []}
        for i in range(self.playerNumber):
            self.playersData["playerDeath"].append(0)
            self.playersData["playerPo"].append(0)
            self.playersData["playerWin"].append(0)

        self.playerGUIManager = PlayerGUIManager(self.root, self, self.playersData, self.playerNumber, self.textures, self.gridSize)
        self.mapManager = MapManager(self.gridSize,  self.textures)

    def clearGame(self):
        #clear tout le jeu (ne supprime pas les objet initialisés) pour relancer un niveau
        if(self.mapManager.currentLvl):
            for i in range(len(self.mapManager.currentLvl["enemies"])):
                self.mapManager.currentLvl["enemies"][0].__del__()
                del self.mapManager.currentLvl["enemies"][0]

        for i in range(len(self.playersData["player"])):
            self.playerGUIManager.clearPlayerGUI()
            self.playersData["player"][0].__del__()
            del self.playersData["player"][0]

        self.playersData["player"].clear()

        if(self.canvasState):
            self.canvasState.delete("all")
    
    def loadGame(self, lvl_id):
        #charge un niveau avec l'id lvl_id
        self.mapManager.loadMap(lvl_id, self.canvasState)
        for i in range(self.playerNumber):
            self.playersData["player"].append(Player(70, 10, self.playerInputsMap[i], 25, self.textures[f"player{i}"], self.canvasState, 
                self.mapManager.lvls[lvl_id]["spawn"][i][0], self.mapManager.lvls[lvl_id]["spawn"][i][1], self.playersData["playerPo"][i],#faire i+0 ou i+1 pour le spawn
                self.playerGUIManager, self.mapManager.currentLvl, self.gridSize))

    def start(self):
        #pour démarrer le jeu après l'init
        self.clearGame()
        self.loadGame(self.currentLvlId)

    def win(self, player_who_win):
        #quand le joueur gagne (ajoute les stats requise, termine le jeu, charge un niveau, ect..)
        for i in range(self.playerNumber):
            self.playersData["playerPo"][i] = self.playersData["player"][i].po
            if(self.playersData["player"][i] == player_who_win):
                self.playersData["playerWin"][i] += 1
        
        self.currentLvlId += 1
        if(self.currentLvlId >= len(self.mapManager.lvls)):
            self.endGame()
        else:
            self.start()

    def loose(self, player_who_dead):
        #lors de la mort d'un joueur
        for i in range(self.playerNumber):
            if(self.playersData["player"][i] == player_who_dead):
                self.playersData["playerDeath"][i] += 1
                player_who_dead.respawn(self.mapManager.lvls[self.currentLvlId]["spawn"][i][0], self.mapManager.lvls[self.currentLvlId]["spawn"][i][1])

    def endGame(self):#virtual
        pass