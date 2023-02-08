from States.endState import EndState, tk
import math

#le state de fin en multi
class MultiEndState(EndState):
    #Constructors / Destructors
    def __init__(self, grid_size, textures, current_states, players_data, root):
        super().__init__(grid_size, textures, current_states, players_data, root)
        self.calculateWinner()

    #Functions
    def calculateWinner(self):
        #calcule le score du joueur
        winConditions = [[-1, 0, False], [-1, 0, False], [-1, math.inf, False]]#id joueur, value, si c'est égalité| et po, wins, morts
        winnerOfCategories = []

        for i in range(len(self.playersData["playerPo"])):#self.playersData["playerPo"] donne le nombre de joueurs
            winnerOfCategories.append(0)
            if(self.playersData["playerPo"][i] > winConditions[0][1]):
                winConditions[0][0] = i
                winConditions[0][1] = self.playersData["playerPo"][i]
                winConditions[0][2] = False
            elif(self.playersData["playerPo"][i] == winConditions[0][1]):
                winConditions[0][2] = True

            if(self.playersData["playerWin"][i] > winConditions[1][1]):
                winConditions[1][0] = i
                winConditions[1][1] = self.playersData["playerWin"][i]
                winConditions[1][2] = False
            elif(self.playersData["playerWin"][i] == winConditions[1][1]):
                winConditions[1][2] = True

            if(self.playersData["playerDeath"][i] < winConditions[2][1]):
                winConditions[2][0] = i
                winConditions[2][1] = self.playersData["playerDeath"][i]
                winConditions[2][2] = False
            elif(self.playersData["playerDeath"][i] == winConditions[2][1]):
                winConditions[2][2] = True

        for i in winConditions:
            if(not i[2]):
                winnerOfCategories[i[0]] += 1
        
        winner = -1
        #donne l'id du winner
        for i in winnerOfCategories:
            for j in range(len(winnerOfCategories)):
                if(winnerOfCategories[j] > i):
                    winner = j

        winnerText = self.canvasState.create_text(self.gridSize*10, self.gridSize*20, anchor=tk.CENTER, text=self.modelPoFormat.format("Gagnant", f"J{winner+1}"), fill="white", font=f'Arial {int(self.gridSize/1.5)}')
        if(winner == -1):
            self.canvasState.itemconfig(winnerText, text="Égalité")