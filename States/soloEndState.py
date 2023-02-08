from States.endState import EndState, tk
import os

#la fin en mode solo
class SoloEndState(EndState):
    #Constructors / Destructors
    def __init__(self, grid_size, textures, current_states, players_data, root):
        super().__init__(grid_size, textures, current_states, players_data, root)
        self.saveScore()

    #Functions
    def drawBestScore(self, best_score):
        #affiche le best_score
        bestScoreText = best_score.split(' ')
        bestScoreText = " : ".join(bestScoreText)
        self.currentLvlText = self.canvasState.create_text(10*self.gridSize, 19*self.gridSize, anchor=tk.N, text=f"Meilleur score : {bestScoreText}", fill="white", font=(f'Arial {self.gridSize}'))

    def openFile(self, path, flag):
        #pour ouvrir des fichier avec le chemin et le flag correspondant
        try:
            scoreFile = open(f"Resources\\{path}", flag)
        except IOError:
            print("Impossible d'ouvrir le fichier !")
            os._exit(1)
        return scoreFile

    def saveScore(self):
        #sauvegarder le score du joueur dans player.save
        scorStr = self.loadScore()
        scoreFile = self.openFile("player.save", 'w')
        self.drawBestScore(scorStr)
        scoreFile.write(scorStr)
        scoreFile.close()

    def loadScore(self):
        #load le meilleur score depuis player.save
        scoreFile = self.openFile("player.save", 'r')

        scoreContent = scoreFile.readlines()
        scoreFile.close()

        if(scoreContent):#verifie si le contenu est vide (si premiere partie)
            lastScore = [i for i in scoreContent[0].split(' ')]
        else:
            lastScore = ""
        bestScore = self.calculateScore(lastScore)

        return bestScore 

    def calculateScore(self, last_score):
        #calcule le score selon les stats du joueur et renvoie un str du score et le compare au dernier score
        isNewBestScore = 0
        if(len(last_score) > 2):
            if(int(last_score[0]) <= self.playersData["playerPo"][0]):
                isNewBestScore += 1
            if(int(last_score[1]) <= self.playersData["playerWin"][0]):
                isNewBestScore += 1
            if(int(last_score[2]) >= self.playersData["playerDeath"][0]):
                isNewBestScore += 1

            if(isNewBestScore < 3):
                return " ".join(last_score)

        return ("{} {} {}".format(self.playersData["playerPo"][0], self.playersData["playerWin"][0], self.playersData["playerDeath"][0]))