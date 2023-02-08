#parent état du jeu
class State:
    #Constructors / Destructors
    def __init__(self, grid_size, textures, current_states, root):
        self.gridSize = grid_size
        self.textures = textures
        self.currentStates = current_states
        self.root = root
        self.canvasState = None

    def __del__(self):
        if(self.canvasState):
            self.canvasState.destroy()
            self.canvasState = None

    def update(self):#virtual
        pass

    #functions
    def quitState(self):
        #pour quitter ce state
        self.currentStates[-1].__del__()
        self.currentStates.pop()
        print("après avoir quitter le state actuel", self.currentStates)
        
        if(len(self.currentStates) == 0):
            self.root.destroy()