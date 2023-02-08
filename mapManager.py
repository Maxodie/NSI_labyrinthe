import tkinter as tk
import os
from chest import Chest
from enemy import Enemy

#gère le spawn des sprite et de la map
class MapManager:
    #Constructor/Destructor
    def __init__(self, grid_size, textures):
        self.gridSize = grid_size
        self.textures = textures
        self.lvls = []
        self.mapConfigs = {}
        self.currentLvl = {}
        self.loadMapsFromFile()

    #Functions
    def loadFile(self, file_name):
        #ouvre un fichier
        try:
            file = open(f"Resources\\{file_name}")
        except IOError:
            print("Impossible d'ouvrir le fichier !")
            os._exit(1)
        
        return file

    def loadMapsFromFile(self):
        #charge tout les config de la map
        #===Config_maps __format__
        #lvl number
        #colliderChar 
        #winChar
        #chestChars
        #EnemyChar
        mapsConfigFile = self.loadFile("config_maps")
        configContent = mapsConfigFile.readlines()

        col = configContent[1].replace('\n', '')
        spawnChar = configContent[2].replace('\n', '')
        winChar = configContent[3].replace('\n', '')
        chestChars = [i for i in configContent[4].replace('\n', '').split(' ')]
        enemyChar = configContent[5].replace('\n', '')
        self.mapConfigs = {"spawnChar" : spawnChar, "winChar" : winChar, "chestChars" : chestChars, "enemyChar" : enemyChar}

        mapsConfigFile.close()
        #load les maps et les met dans self.lvls avec les paramètres chagé avant
        #===lvls __format__
        #map 
        # \n 
        #spawn x y
        lvlsFile = self.loadFile("lvls")
        lvlsContent = lvlsFile.readlines()
        i = 0
        for j in range(int(configContent[0])):
            lvl = []
            while(lvlsContent[i] != "\n"):
                lvl.append(lvlsContent[i])
                i += 1
            i += 1
            self.lvls.append({"map": lvl, "spawn" : [], "win" : [], "col" : col, "chests" : [], "enemies" : []})
        lvlsFile.close()

    def loadMap(self, lvl_id, canvas):
        #load la map avec l'id lvl_id dans self.lvls et créé selon les chars: des enemies, les murs, des coffres
        self.currentLvl = self.lvls[lvl_id]
        for y in range(len(self.lvls[lvl_id]["map"])):
            for x in range(len(self.lvls[lvl_id]["map"][y])):
                if(self.lvls[lvl_id]["map"][y][x] == self.mapConfigs["spawnChar"]):
                    self.lvls[lvl_id]["spawn"].append((x, y))
                elif(self.lvls[lvl_id]["map"][y][x] == self.lvls[lvl_id]["col"]):
                    canvas.create_image(x*self.gridSize, y*self.gridSize, anchor=tk.NW, image=self.textures["brick"])
                elif(self.lvls[lvl_id]["map"][y][x] == self.mapConfigs["enemyChar"]):
                    enemy = Enemy(200, 25, self.textures["enemy"], canvas, x, y, self.currentLvl, self.gridSize)
                    self.currentLvl["enemies"].append(enemy)
                elif(self.lvls[lvl_id]["map"][y][x] == self.mapConfigs["winChar"]):
                    winDoor = canvas.create_image(x*self.gridSize, y*self.gridSize, anchor=tk.NW, image=self.textures["win"])
                    self.currentLvl["win"] = winDoor
                else:
                    for i in self.mapConfigs["chestChars"]:
                        if(self.lvls[lvl_id]["map"][y][x] == i):
                            chest = Chest(i, self.textures["chest"], canvas, x, y, self.currentLvl, self.gridSize)
                            self.currentLvl["chests"].append(chest)