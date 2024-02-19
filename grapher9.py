#Grapher: graphs the points in a data file
from graphics import *
from math import inf
def grapher(filename):
    maxX, maxY = inf,inf
    minX, minY = -inf, -inf
    infile = open(filename,'r')
    for line in infile:
        if line != 'EOF':
            linelist = line[:-1].split(',')
        x = float(linelist[0])
        y = float(linelist[1])
        maxX, minX,maxY,minY = bigSmall(x,y,maxX, minX,maxY,minY)
        
        
    infile.close()
    return maxX,maxY