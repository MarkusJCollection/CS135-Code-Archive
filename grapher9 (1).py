#Grapher: graphs the points in a data file
from graphics import *
from math import inf
def bigSmall(x,y,maxX, minX,maxY,minY):
    if x > maxX:
        maxX=x
    if x < minX:
        minX = x
    if y > maxY:
        maxY = y
    if y < minY:
        minY = y
    return maxX, minX,maxY,minY

def drawAxes(window,maxX,maxY,minX,minY):
    xAxis = Line(Point(minX,0),Point(maxX,0))
    xAxis.draw(window)
    yaxis = Line(Point(0,maxY),Point(0,minY))
    yaxis.draw(window)
    
    
    
def grapher(filename):
    maxX, maxY = -inf,-inf
    minX, minY = inf, inf
    infile = open(filename,'r')
    for line in infile:
        if line != 'EOF':
            linelist = line[:-1].split(',')
            x = float(linelist[0])
            y = float(linelist[1])
            maxX, minX,maxY,minY = bigSmall(x,y,maxX, minX,maxY,minY)
    infile.close()
    #Draw the graph!
    win = GraphWin(filename,600,600)
    win.setCoords(minX,minY-0.1,maxX,maxY+0.1)
    infile = open(filename,'r')
    for line in infile:
        if line != 'EOF':
            linelist = line[:-1].split(',')
            x = float(linelist[0])
            y = float(linelist[1])
            pt = Point(x,y)
            
            pt.draw(win)
    infile.close()
    drawAxes(win,maxX,maxY,minX,minY)
    win.getMouse()
    win.close()
    
def main():
    filename = input('Enter the file to be graphed: ')
    grapher(filename)
    
main()   
    
    
    
    
    
    
    
    
    
   