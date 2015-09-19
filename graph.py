class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.outDegree = 0

    def addNeighbor(self,nbr,weight=1):
        if nbr not in self.connectedTo:
            self.outDegree = self.outDegree + 1
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getNeighbors(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        if (nbr in self.connectedTo):
            return self.connectedTo[nbr]
        return 0

class Graph:
    def __init__(self):
        self.vertList = {}
        self.size = 0

    def addVertex(self,key):
        self.size = self.size + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,w=1):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(t, w)

    def getVertices(self):
        return self.vertList.keys()

    def outDegree(self, n):
        if n in self.vertList:
            return self.vertList[n].outDegree
        return 0

    def e(self, a, b):
        num = 0
        for i in a:
            for j in b:
                num = num + self.weightOf(i,j)
        return num

    def weightOf(self, f, t):
        if f not in self.vertList:
            return 0
        if t not in self.vertList:
            return 0
        return self.vertList[f].getWeight(t)

    def findFront(self, c):
        front = {}
        for i in c:
            for j in self.vertList[i].getNeighbors():
                front[j] = True
        for i in c:
            if i in front:
                del front[i]
        return front.keys()

    def updateFront(self, front, node, ex):
        for i in self.vertList[node].getNeighbors():
            front.add(i)
        return front - ex


    def __iter__(self):
        return iter(self.vertList.values())


