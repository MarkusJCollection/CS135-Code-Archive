#Triangle Exercise
#Write a program with a graphics window that
#(1) takes three mouse clicks
#(2) draws the points clicked
#(3) draws a triangle connecting the points
#(4) calculates the area and perimeter of the triangle
# Note: if a, b, c are the lengths of the sides of the triangle,
# area = sqrt(s*(s-a)*(s-b)*(s-c)), s = (a + b + c)/2
#(5) writes the results in the window
#(6) closes the window with a mouse click


#Imports necessary modules required.
from graphics import *
from math import sqrt

win=GraphWin('Triangle Excersize',500,500)
win.setCoords(-10,-10,10,10)

p1 = win.getMouse()
p2 = win.getMouse()
p3 = win.getMouse()
triangle = Polygon(p1,p2,p3)


p1.draw(win)
p2.draw(win)
p3.draw(win)
triangle.draw(win)


sideA = sqrt(((p1.getX()+p2.getX())**2) + ((p1.getY()+p2.getY())**2))
sideB = sqrt(((p2.getX()+p3.getX())**2) + ((p2.getY()+p3.getY())**2))
sideC = sqrt(((p1.getX()+p3.getX())**2) + ((p1.getY()+p3.getY())**2))
perimeter = round(sideA+sideB+sideC,2)

s = perimeter/2
area = sqrt(abs(s*(s-sideA)*(s-sideB)*(s-sideC)))
areaF = round(area,2)

textArea = Text(Point(0,-8),'Area = '+str(areaF))
textPerim = Text(Point(0,-9),'Perimeter = '+str(perimeter))


print(sideA)
print(sideB)
print(sideC)
print(perimeter)
print(areaF)
textArea.draw(win)
textPerim.draw(win)


win.getMouse()
win.close()