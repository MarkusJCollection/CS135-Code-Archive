# Volume and serface area of a sphere
# by Sabine Wren
# September 15, 2023

from math import pi
from graphics import *

win = GraphWin('Sphere Calculator',500,500)
win.setCoords(-50,-50,50,50)

headText=Text(Point(0,40),"This program computes volume + surface area")
headText.draw(win)
entryText=Text(Point(0,30),"Please enter radius of the sphere.")
entryText.draw(win)
entryBox = Entry(Point(0,20),10)
entryBox.setFill('lightblue')
entryBox.draw(win)
win.getKey()
r = float(entryBox.getText())
print(r)

volume = 4.0/3.0 * pi * r**3
area = 4 * pi * r**2
vol = round(volume,2)
a = round(area,2)

volText=Text(Point(0,10),"The volume is "+str(vol)+" cubic units.")
areaText=Text(Point(0,0),"The area is "+str(a)+" square units.")
volText.draw(win)
areaText.draw(win)




win.getMouse()
win.close()



