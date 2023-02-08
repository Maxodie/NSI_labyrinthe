from colliderComponent import *
import tkinter as tk
from PIL import ImageTk

#le sprite est le parent des objets avec le quel on peut interagir
class Sprite:
    #Constructor/Destructor
    def __init__(self, texture, canvas, spawn_x, spawn_y, current_lvl, grid_size):
        self.canvas = canvas
        self.gridSize = grid_size
        self.currentLvl = current_lvl
        self.texture = texture
        self.sprite = self.canvas.create_image(spawn_x*grid_size, spawn_y*grid_size, anchor=tk.NW, image=texture)

    def __del__(self):
        pass

    #Functions
    def delSprite(self):
        self.canvas.delete(self.sprite)