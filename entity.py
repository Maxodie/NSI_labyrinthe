from sprite import *
from mouvementComponent import *

#les entites avec notament un mouvementComponent
class Entity(Sprite):
    #Constructor/Destructor
    def __init__(self, reactivity_ms, speed, texture, canvas, spawn_x, spawn_y, current_lvl, grid_size):
        super().__init__(texture, canvas, spawn_x, spawn_y, current_lvl, grid_size)
        self.tkAfters = {}
        self.reactivityMS = reactivity_ms
        self.speed = speed
        self.mouvementComponent = MouvementComponent(speed, spawn_x, spawn_y, canvas, self.sprite, texture, current_lvl, grid_size)

    def __del__(self):
        super().__del__()