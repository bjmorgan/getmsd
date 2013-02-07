#! /usr/bin/python

# http://en.wikipedia.org/wiki/Simple_linear_regression

import sys
from string import split

x = []
y = []
xx = []
xy = []

while 1:
	thisline = sys.stdin.readline()
	if thisline != '':
		data = split(thisline)
		x.append(float(data[0]))
		y.append(float(data[1]))
	else:
		sys.stdout.flush()
		break

n = len(x)
for i in range(n):
	xx.append(x[i]*x[i])
	xy.append(x[i]*y[i])

sx = sum(x)
sy = sum(y)
sxx = sum(xx)
sxy = sum(xy)

slope = (n*sxy - sx*sy) / (n*sxx - sx*sx)
intercept = (sy - slope*sx)/n

print intercept, slope

