import keyboard

class PlayerController:
    #Constructor/Destructor
    def __init__(self, player, input_dir: tuple):#dir gauche, droite, haut, bas
        self.player = player
        self.left = input_dir[0]
        self.right = input_dir[1]
        self.up = input_dir[2]
        self.down = input_dir[3]

    #Functions
    def updateInput(self):
        #verifie les inputs touchés et fait des actions
        if keyboard.is_pressed(self.left):
            self.pMove(-1, 0)
        if keyboard.is_pressed(self.right):
            self.pMove(1, 0)
        if keyboard.is_pressed(self.up):
            self.pMove(0, -1)
        if keyboard.is_pressed(self.down):
            self.pMove(0, 1)

    def pMove(self, dir_x, dir_y):
        self.player.mouvementComponent.move(dir_x, dir_y)