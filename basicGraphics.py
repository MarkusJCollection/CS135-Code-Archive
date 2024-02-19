#Basic graphics
from graphics import *

#make a window
win=GraphWin("My Window",500,500)
#set the coordinates of the window
win.setCoords(-10,-10,10,10)


"""
#Defines p1 where you click your mouse on the window,
#then draws it in the window.
p1 = win.getMouse()
p1.draw(win)

#Defines p2 as the center of the window (0,0)
#and draws it in the window.
p2 = Point(0,0)
p2.draw(win)

#Defines the starting and ending points of a line,
#then draws the line in the window.
l1= Line(p1,p2)
l1.draw(win)

l2 = Line(Point(0,-10),Point(0,10))
l2.draw(win)
"""

"""
#Defines each corner of the rectangle
#then draws it in the window.
p1 = win.getMouse()     #Lower left corner
p2 = win.getMouse()     #Upper right corner
p3 = win.getMouse()

#r1 = Rectangle(p1,p2)
#r1.draw(win)

poly1 = Polygon(p1,p2,p3)
poly1.setFill('navy blue')
poly1.draw(win)
"""



c1=Circle(Point(0,0),5)
c1.draw(win)
c1.setFill('green')

c2=Circle(Point(0,0),4)
c2.draw(win)
c2.setFill('blue')

    #Center point of text
      #       v       String drawn
t1 = Text(Point(0,0),'hello world')
t1.draw(win)
t1.setTextColor('yellow')

p1 = win.getMouse()
t2 = Text(p1,'hi')
t2.draw(win)

for i in range(1000):
    c2.move(1/100,0)


#Wait for mouse click
win.getMouse()
#close the window
win.close()
