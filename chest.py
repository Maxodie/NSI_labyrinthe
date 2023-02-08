import random
from sprite import Sprite

class Chest(Sprite):
    #Constructor/Destructor
    def __init__(self, chest_type_id, texture, canvas, spawn_x, spawn_y, current_lvl, grid_size):
        super().__init__(texture, canvas, spawn_x, spawn_y, current_lvl, grid_size)
        self.chestTypeId = chest_type_id

    def __del__(self):
        super().__del__()

    #Functions
    def calculeGain(self):
        #calcule le gain du coffre
        if(self.chestTypeId == '1'):
            po = random.randint(1, 5)
        elif(self.chestTypeId == '2'):
            po = random.randint(5, 10)
        elif(self.chestTypeId == '3'):
            po = random.randint(0, 25)
            
        self.destructChest()

        return po

    def destructChest(self):
        #on suprime le coffre et le retire de la map actuelement load
        self.delSprite()
        for i in range(len(self.currentLvl["chests"])):
            if(self.currentLvl["chests"][i] == self):
                self.currentLvl["chests"][i].__del__()
                del self.currentLvl["chests"][i]
                return