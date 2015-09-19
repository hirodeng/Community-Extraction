from graph import Graph

class ConGraph(Graph):
	def addComm(self, comm):
		for i in range(0,len(comm)-1):
			for j in range(i+1,len(comm)):
				increase(comm[i], comm[j])

	def increase(self, a, b):
		if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(t, w)
