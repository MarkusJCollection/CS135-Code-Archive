#Basic graphics 2
from graphics import *
from math import sqrt

#This program uses a GUI.  The program (1) accepts two mouse clicks, (2) draws the points clicked,
#(3)draws a line segment between the points, (4)calculates the length of
#that line segment,(5)displays that length in the window, (6) calculates the slope of the line segment,
#(7) displays the slope in the window, and (8) closes the window at a mouse click.

#make a window
win=GraphWin("Line Segment Information",500,500)
#set the coordinates of the window
win.setCoords(-50,-50,50,50)

p1 = win.getMouse()
p2 = win.getMouse()
line = Line(p1,p2)
line.draw(win)
p1.draw(win)
p2.draw(win)

length = float(sqrt((p2.getX()-p1.getX())**2+(p2.getY()-p1.getY())**2))
length = round(length,2)

lenText = Text(Point(0,-30),'The length is '+str(length))
lenText.draw(win)

slope = (p2.getY()-p1.getY())/(p2.getX()-p1.getX())
slope = round(slope,2)
slText = Text(Point(0,-35),'The slope is '+str(slope))
slText.draw(win)

#Wait for mouse click
win.getMouse()
#close the window
win.close()
