from models.Vertex import *
from models.Edge import *


class GraphService:
    def __init__(self, directed=True):
        self.listEdge = []
        self.listVertex = []
        self.directed = directed
        self.exploredOrder = 0

    def newVertex(self, vertexId):
        self.listVertex.append(Vertex(vertexId))

    def newEdge(self, origin, destiny, weight):
        originAux = self.findVertex(origin)
        destinyAux = self.findVertex(destiny)
        if (originAux is not None) and (destinyAux is not None):
            self.listEdge.append(Edge(originAux, destinyAux, weight))
        if self.directed == False:
            self.listEdge.append(Edge(destinyAux, originAux, weight))

    def findVertex(self, vertexId):
        for i in self.listVertex:
            if vertexId == i.getId():
                return i
        else:
            return None

    def findEdge(self, A, B):
        for i in self.listEdge:
            origin = i.getOrigin()
            destiny = i.getDestiny()
            if origin.getId() == A.getId() and destiny.getId() == B.getId():
                return i

    def fncDijkstra(self, origin):
        fonte = self.findVertex(origin)
        self.changeValuesSourceinRelationAllVertex(fonte)
        newListVertex = []
        response = []
        for i in self.listVertex:
            newListVertex.append(i)
        while len(newListVertex) != 0:
            newListVertex.sort()
            A = newListVertex[0]
            B = self.findNeighbors(A)
            if B is None:
                for i in self.listVertex:
                    i.setExplored(False)
                self.exploredOrder += 1
                A.setInput(self.exploredOrder)
                response.append(newListVertex[0])
                newListVertex.pop(0)
            else:
                u = self.findEdge(A, B)
                if u is not None:
                    self.relaxVertex(A, B, u)
        return response

    def findNeighbors(self, A):
        for i in range(len(self.listEdge)):
            origin = self.listEdge[i].getOrigin()
            destiny = self.listEdge[i].getDestiny()
            if (A.getId() == origin.getId()) and (destiny.getExplored() == False):
                destiny.setExplored(True)
                return destiny
        else:
            return None

    def changeValuesSourceinRelationAllVertex(self, fonte):
        for i in self.listVertex:
            i.setEstimation(99999)
            i.setExplored(False)
            i.setColor('white')
        fonte.setEstimation(0)
        fonte.setColor('grey')

    def relaxVertex(self, A, B, u):
        if B.getEstimation() > (A.getEstimation() + u.getWeight()):
            B.setEstimation(A.getEstimation() + u.getWeight())
            B.prev.append(A.getId())

    def printRouterDijsktra(self, response, destiny):
        route = []
        route.clear()
        for vertex in response:
            if(vertex.getId() == destiny):
                route = vertex.prev
                route.append(destiny)
                return route, vertex.getEstimation()
        return route
