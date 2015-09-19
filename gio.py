import csv
from graph import Graph 

def readGraph(filename, head=0, symmetric=True):
	f = open(filename, 'r')
	g = Graph()
	for line in f:
		if head > 0:
			head = head - 1
			continue
		else:
			data = line.split()
			if len(data) < 2:
				return None
			if len(data) > 2:
				w = double(data[3])
			else:
				w = 1
			g.addEdge(data[0], data[1], w)
			if symmetric == True:
				g.addEdge(data[1], data[0], w)
	return g

def writePart(filename, part):
	f = open(filename, 'w')
	i = 0
	for comm in part:
		i = i + 1
		for node in comm:
			f.write(node + '\t' + str(i) + '\n')

def readPart(filename, head=0):
	part = {}
	f = open(filename, 'r')
	for line in f:
		if head > 0:
			head = head - 1
			continue
		else:
			data = line.split()
			if len(data) != 2:
				return None
			[node, comm] = data
			if comm not in part:
				part[comm] = set([node])
			else:
				part[comm].add(node)
	return list(part.values())


