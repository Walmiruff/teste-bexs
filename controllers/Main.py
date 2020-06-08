import sys
import os
import time

from models.Vertex import *
from models.Edge import *

from services.file_service import FileService
from services.graph_service import GraphService


class Main(object):

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.fileService = FileService(self.input_file)
        self.graphService = GraphService()

    def initGraph(self):
        return self.fileService.readFile()

    def drawGraph(self):
        for fileData in self.fileService.input_data:
            for i in range(0, 2):
                v = Vertex(fileData[i])
                self.addVertex(v)
            self.addEdge(fileData)

    def addVertex(self, vertex):
        existVertex = self.graphService.findVertex(vertex.getId())
        if (existVertex):
            return False
        else:
            self.graphService.newVertex(vertex.getId())

    def addEdge(self, row):
        A = Vertex(row[0])
        B = Vertex(row[1])
        existEdge = self.graphService.findEdge(A, B)
        if existEdge is None:
            self.graphService.newEdge(A.getId(), B.getId(), int(row[2]))

    def refreshGraph(self, origin, destiny, cost):
        A = Vertex(origin)
        self.addVertex(A)
        B = Vertex(destiny)
        self.addVertex(B)
        self.addEdgeAgain(A, B, cost)

    def addEdgeAgain(self, origin, destiny, cost):
        existEdge = self.graphService.findEdge(origin, destiny)
        if existEdge is None:
            self.graphService.newEdge(origin.getId(), destiny.getId(), int(cost))
        
    def getRoute(self, origin, destiny):
        response = self.graphService.fncDijkstra(origin)
        route, cost = self.graphService.printRouterDijsktra(response, destiny)
        return route, cost
