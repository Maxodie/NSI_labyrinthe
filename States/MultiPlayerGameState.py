from States.gameState import GameState
from player import PlayerState
from States.multiEndState import MultiEndState

#le jeu avec plusieurs joueurs 
class MultiPlayerGameState(GameState):
    #Constructors / Destructors
    def __init__(self, grid_size, textures, current_states, player_number, player_inputs_map, root):
        super().__init__(grid_size, textures, current_states, player_number, player_inputs_map, root)

    def __del__(self):
        return super().__del__()
    
    #Functions
    def update(self):
        #verifie pour chaque joueur dans le jeu si il a gagne ou si il est mort
        for i in range(len(self.playersData["player"])):
            if(self.playersData["player"][i].playerState == PlayerState.WIN):
                self.win(self.playersData["player"][i])
            elif(self.playersData["player"][i].playerState == PlayerState.DEAD):
                self.loose(self.playersData["player"][i])
                break
    
    def endGame(self):
        #le menu de fin en multi (on calcule le gagnant notament) et on quit le state
        self.currentStates.insert(-1, MultiEndState(self.gridSize, self.textures, self.currentStates, self.playersData, self.root))
        self.quitState()