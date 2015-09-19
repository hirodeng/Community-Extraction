import random

def seqExt(g):
	n = g.size
	ex = set([])
	part = []
	while len(ex) < n:
		comm = extract(g,ex)
		ex = ex | comm
		part.append(comm)
		#print(comm)
		#print(ex)
	return part
	
def extract(g, ex=set([])):
	nodes = set(g.getVertices())
	nodes = nodes - ex;
	node = random.sample(nodes,1)[0]
	comm = set([node])
	front = set(g.getVertex(node).getNeighbors()) - ex
	ind = 0.0
	total = g.outDegree(node)
	r = 0.0
	stop = False
	while stop == False:
		stop = True
		# expand
		best_r = r
		for node in front:
			new_ind = ind + g.e([node], comm)
			new_total = total + g.outDegree(node)
			new_r = new_ind * 1.0 / new_total
			if new_r > best_r:
				best_r = new_r
				best_ind = new_ind
				best_total = new_total
				best_add = node
		if best_r > r:
			comm.add(best_add)
			r = best_r
			ind = best_ind
			total = best_total
			stop = False
			front = g.updateFront(front, best_add, ex | comm)
		if len(comm) == 1:
			continue
		# prune
		for node in comm:
			new_ind = ind - g.e([node], comm)
			new_total = total - g.outDegree(node)
			new_r = new_ind * 1.0 / new_total
			if new_r > best_r:
				best_r = new_r
				best_ind = new_ind
				best_total = new_total
				best_prune = node
		if best_r > r:
			comm.discard(best_prune)
			r = best_r
			ind = best_ind
			total = best_total
			stop = False
			front.add(best_prune)
	return comm




