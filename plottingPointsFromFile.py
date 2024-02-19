from graphics import *
from math import inf

def minMax(list):
    
    
    
    
    
    
    
    
    
    return minX,minY,maxX,maxY
    








def grapher(fileName):
    maxX, maxY = inf,inf
    minX, minY = -inf,-inf
    infile = open(fileName, 'r')
    print(infile.readline())
    numbersList = []
    for line in infile:
        if line != 'EOF':
            linelist = line[:-1].split(',')
        x = float(linelist[0])
        y = float(linelist[1])
    infile.close()
    return 









