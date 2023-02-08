from entity import Entity
import random

#l'enemie
class Enemy(Entity):
    #Constructor/Destructor
    def __init__(self, reacivity_ms, speed, texture, canvas, spawn_x, spawn_y, current_lvl, grid_size):
        super().__init__(reacivity_ms, speed, texture, canvas, spawn_x, spawn_y, current_lvl, grid_size)
        self.movableDir = [False, False, False, False]#Gauche, droite, haut, bas
        self.preparDir()
        self.preparMove()

    def __del__(self):
        self.canvas.after_cancel(self.tkAfters["preparMove"])
        super().__del__()

    #Functions
    def preparDir(self):
        #calclue une dirrection random
        self.dir = random.randint(0, 3)
        if(self.dir == 0):
            self.dirX = -1
            self.dirY = 0
        elif(self.dir == 1):
            self.dirX = 1
            self.dirY = 0
        elif(self.dir == 2):
            self.dirX = 0
            self.dirY = -1
        elif(self.dir == 3):
            self.dirX = 0
            self.dirY = 1

    def preparMove(self):
        #verifie si il peut bouger pour vérifier les carfours sinon il recalcule une direction
        if(not self.mouvementComponent.move(self.dirX, self.dirY)):
            self.preparDir()
        else:
            self.checkForIntersections()

        self.tkAfters["preparMove"] = self.canvas.after(self.reactivityMS, self.preparMove)

    def checkForIntersections(self):
        #verifie si un mouvement sur les côté est possible et si les mouvements possibles changent il change de dirrection
        currentMovableDir = []
        currentMovableDir.append(self.mouvementComponent.checkNextMoveCol(self.mouvementComponent.calculeVel(-1, 0)))
        currentMovableDir.append(self.mouvementComponent.checkNextMoveCol(self.mouvementComponent.calculeVel(1, 0)))
        currentMovableDir.append(self.mouvementComponent.checkNextMoveCol(self.mouvementComponent.calculeVel(0, -1)))
        currentMovableDir.append(self.mouvementComponent.checkNextMoveCol(self.mouvementComponent.calculeVel(0, 1)))
        if(self.movableDir != currentMovableDir):
            self.movableDir = currentMovableDir
            self.preparDir()

    def death(self):
        #la mort de l'enemie (le supprime de la liste des enemies, ect..)
        self.delSprite()
        for i in range(len(self.currentLvl["enemies"])):
            if(self.currentLvl["enemies"][i] == self):
                self.currentLvl["enemies"][i].__del__()
                del self.currentLvl["enemies"][i]
                return