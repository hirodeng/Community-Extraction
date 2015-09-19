import math

def nmi(x, y):
	nx = len(x)
	ny = len(y)
	n = []
	s = 0.0
	for i in range(nx):
		n.append([])
		s = s + len(x[i])
		for j in range(ny):
			n[i].append(len(x[i] & y[j]))
	numerator = 0.0
	for i in range(nx):
		for j in range(ny):
			if n[i][j] > 0:
				numerator = numerator + n[i][j] * math.log(n[i][j] * s / len(x[i]) / len(y[j]))
	numerator = -2 * numerator
	denominator = 0.0
	for i in range(nx):
		denominator = denominator + len(x[i]) * math.log(len(x[i]) / s)
	for i in range(ny):
		denominator = denominator + len(y[i]) * math.log(len(y[i]) / s)
	if numerator == denominator:
		return 1.0
	return numerator / denominator