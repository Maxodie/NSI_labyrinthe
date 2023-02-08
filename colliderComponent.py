#permet de detecter 
class ColliderComponent:
    #Constructor/Destructor
    def __init__(self, reactivity_ms, canvas, sprite, grid_size):
        self.tkAfterUpdate = None
        self.reactivityMS = reactivity_ms
        self.canvas = canvas
        self.sprite = sprite
        self.gridSize = grid_size
        self.triggeredColliders = ()

    #Functions
    def update(self):
        #update les colliders qui sont triggered
        self.triggeredColliders = self.updateCheckCurrentTriggerCols()

    def updateCheckCurrentTriggerCols(self):
        #return tout les collider qui sont sur le sprite du component
        try:
            cols = list(self.canvas.find_overlapping(
                self.canvas.coords(self.sprite)[0],
                self.canvas.coords(self.sprite)[1],
                self.canvas.coords(self.sprite)[0]+self.gridSize,
                self.canvas.coords(self.sprite)[1]+self.gridSize))
            del cols[-1]
            return tuple(cols)
        except:
            print(f"COLLIDERCOMPONENT::ERROR::colliderComponent: {self} non détruit/arrêté sur le sprite: {self.sprite}")
            return ()