import math

class MouvementComponent:
    #Constructor/Destructor
    def __init__(self, speed, pos_x, pos_y, canvas, sprite, texture, current_lvl, grid_size):
        self.speed = speed
        self.posX = pos_x
        self.posY = pos_y
        self.canvas = canvas
        self.sprite = sprite
        self.texture = texture
        self.currentLvl = current_lvl
        self.gridSize = grid_size

    #Functions
    def setPos(self, pos_x, pos_y):
        self.canvas.move(self.sprite, -self.canvas.coords(self.sprite)[0], -self.canvas.coords(self.sprite)[1])
        self.canvas.move(self.sprite, pos_x*self.gridSize, pos_y*self.gridSize)
        self.posX = pos_x
        self.posY = pos_y

    def move(self, dir_x, dir_y):
        #créé une velocity et vérifie si le déplacement est possible et donc le déplace 
        vel = self.calculeVel(dir_x, dir_y)
        if(self.checkNextMoveCol(vel)):
            self.canvas.move(self.sprite, vel[0]*self.gridSize, vel[1]*self.gridSize)
            self.posX += vel[0]
            self.posY += vel[1]
            return True
        else:
            return False

    def calculeVel(self, dir_x, dir_y):
        #calcule la vélocité d'un déplacement
        return (dir_x*self.speed/100, dir_y*self.speed/100)

    def checkNextMoveCol(self, vel):
        #verifie si le déplacement est possible (si le joueur sera dans un mur ou pas)
        try:
            if(self.currentLvl["map"][math.floor(self.posY+vel[1])][math.floor(self.posX+vel[0])] == self.currentLvl["col"] or
            self.currentLvl["map"][math.ceil(self.posY+vel[1])][math.ceil(self.posX+vel[0])] == self.currentLvl["col"] or
            self.currentLvl["map"][math.floor(self.posY+vel[1])][math.ceil(self.posX+vel[0])] == self.currentLvl["col"] or
            self.currentLvl["map"][math.ceil(self.posY+vel[1])][math.floor(self.posX+vel[0])] == self.currentLvl["col"]):
                return False
        except:
            return False
        return True