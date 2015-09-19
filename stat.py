import measure
import statistics
import gio

network = './1000/mu4/d10/2/'
true = gio.readPart(network + 'community.dat')
num = 10
nmi = [0] * num

for i in range(1,num+1):
	part = gio.readPart(network + 'part%d.dat' % i)
	nmi[i-1] = measure.nmi(part, true)

print(network)
print('%d partitions')
print('Average NMI:\t %.4f' % statistics.mean(nmi))
print('Standard deviation:\t %.4f' % statistics.stdev(nmi))