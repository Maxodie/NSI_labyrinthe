from enum import Enum
from entity import Entity
from colliderComponent import ColliderComponent
from playerController import PlayerController
import random

class Player(Entity):
    #Constructor/Destructor
    def __init__(self, reactivity_ms, start_life, player_input, speed, texture, canvas, spawn_x, spawn_y, start_po, gui_manager, current_lvl, grid_size):
        super().__init__(reactivity_ms, speed, texture, canvas, spawn_x, spawn_y, current_lvl, grid_size)
        self.guiManager = gui_manager
        self.startLife = start_life
        self.currentLife = start_life
        self.po = start_po
        self.playerState = PlayerState.IN_GAME
        self.colliderComponent = ColliderComponent(reactivity_ms, canvas, self.sprite, grid_size)
        self.playerController = PlayerController(self, player_input)
        self.guiManager.createPlayerGUI(self)
        self.update()

    def __del__(self):
        self.canvas.after_cancel(self.tkAfters["update"])
        super().__del__()

    #Functions
    def death(self):
        self.playerState = PlayerState.DEAD

    def takeDamage(self, damage):
        #les domages reçus par le joueur
        self.currentLife -= damage
        if(self.currentLife <= 0):
            self.currentLife = 0
            self.death()
        self.guiManager.updatePlayersGUI()

    def update(self):
        #update les inputs, les components et l'état de victoire
        self.playerController.updateInput()
        self.colliderComponent.update()

        if(self.colliderComponent.triggeredColliders):
            for i in self.colliderComponent.triggeredColliders:
                self.onTrigger(i)

        self.checkWinState()
        self.tkAfters["update"] = self.canvas.after(self.reactivityMS, self.update)

    def onTrigger(self, col_sprite):
        #verifie pour chaques collisions si c'est le sprite de la porte de fin ouun enemie ou un coffre
        if(col_sprite == self.currentLvl["win"]):
            self.playerState = PlayerState.WIN
            return
        
        for i in self.currentLvl["enemies"]:
            if(i.sprite == col_sprite):
                self.startFight(i)
                return
        
        for i in self.currentLvl["chests"]:
            if(i.sprite == col_sprite):
                self.addPo(i.calculeGain())
                return
    
    def checkWinState(self):
        #verifie si toujours sur le sprite de la porte
        if(self.playerState == PlayerState.WIN):
            if(self.colliderComponent.triggeredColliders):
                if(not self.currentLvl["win"] in self.colliderComponent.triggeredColliders):
                    self.playerState = PlayerState.IN_GAME
            else:
                self.playerState = PlayerState.IN_GAME

    def addPo(self, number):
        #ajoute l'argent au joueur
        self.po += number
        self.guiManager.updatePlayersGUI()

    def startFight(self, enemy):
        #démare un combat et calcule les dégâts reçus par le joueur
        attack = random.randint(1, 10)
        if(attack == 1):
            self.takeDamage(random.randint(5, 10))
        elif(attack >= 2 and attack <= 4):
            self.takeDamage(random.randint(1, 5))
        enemy.death()

    def respawn(self, pos_x, pos_y):
        #fait réaparaitre le joueur au spawn en cas de mort par exemple
        self.mouvementComponent.setPos(pos_x, pos_y)
        self.playerState = PlayerState.IN_GAME
        self.currentLife = self.startLife
        self.guiManager.updatePlayersGUI()

class PlayerState(Enum):
    IN_GAME = 0
    WIN = 1
    DEAD = 2