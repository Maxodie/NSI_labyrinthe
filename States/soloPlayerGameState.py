from States.gameState import GameState
from player import PlayerState
from States.soloEndState import SoloEndState

#le jeu en solo
class SoloPlayerGameState(GameState):
    #Constructors / Destructors
    def __init__(self, grid_size, textures, current_states, player_number, player_inputs_map, root):
        super().__init__(grid_size, textures, current_states, player_number, player_inputs_map, root)

    def __del__(self):
        return super().__del__()
    
    #Functions
    def update(self):
        #verifie l'etat du joueur (si il à gagné ou perdu)
        if(self.playersData["player"]):
            if(self.playersData["player"][0].playerState == PlayerState.WIN):
                    self.win(self.playersData["player"][0])
            elif(self.playersData["player"][0].playerState == PlayerState.DEAD):
                self.loose(self.playersData["player"][0])
    
    def endGame(self):
        #ajoute le state de la fin solo et quit le state
        self.currentStates.insert(-1, SoloEndState(self.gridSize, self.textures, self.currentStates, self.playersData, self.root))
        self.quitState()