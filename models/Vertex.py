class Vertex():
    def __init__(self, id):
        self.id = id
        self.estimation = 999999
        self.input = 0
        self.explored = False
        self.prev = []
        self.color = 'white'

    def setExplored(self, value):
        self.explored = value

    def getExplored(self):
        return self.explored

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setInput(self, inp):
        self.input = inp

    def setEstimation(self, estimation):
        self.estimation = estimation

    def getEstimation(self):
        return self.estimation

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __lt__(self, v):
        return self.estimation < v.estimation

    def __eq__(self, v):
        return self.estimation == v.estimation

    def __gt__(self, v):
        return self.estimation > v.estimation
