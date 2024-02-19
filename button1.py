#Building a button into a GUI

from graphics import *

#This function computes the distance between two Point
#objects 
def distance(p1,p2):
    """Assumes p1 and p2 are graphics.Point objects"""
    from math import sqrt
    dx = p1.getX()-p2.getX()
    dy = p1.getY()-p2.getY()
    dist = sqrt(dx**2+dy**2)
    return dist

def main():
    win =GraphWin('Buttons', 500,500)
    win.setCoords(-50,-50,50,50)

    goButton = Circle(Point(20,10),5)
    goButton.setFill('pink')
    goButton.draw(win)
    goLabel = Text(Point(20,10),'Go')
    goLabel.draw(win)
    quitButton = Circle(Point(-20,10),5)
    quitButton.setFill('pink')
    quitButton.draw(win)
    quitLabel = Text(Point(-20,10),'Quit')
    quitLabel.draw(win)
    
    finished = False
    
    while not finished:
        pt = win.getMouse()
        if distance(pt,goButton.getCenter()) < goButton.getRadius():
            print("You've pressed go!")
        elif distance(pt,quitButton.getCenter()) < quitButton.getRadius():
            print("You've pressed quit!")
            finished = True
        else:
            retry = Text(Point(0,30),'Press a button to do stuff!')
            retry.draw(win)
            print('no button')
            
    win.close()
    
main()