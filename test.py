import gio
import ce

network = './real/facebook/'
#network = './1000/mu4/d10/2/'
run = 10

g = gio.readGraph(network + 'network.dat')
for i in range(1,run+1):
	part = ce.seqExt(g)
	gio.writePart(network + 'part%d.dat' % i, part)


