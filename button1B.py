#button1.py
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
    
    messageText = Text(Point(0,-10), 'Click a button')
    messageText.draw(win)
    
    finished = False
    while not finished:
        pt=win.getMouse()
        if distance(pt, goButton.getCenter()) < goButton.getRadius():
            messageText.setText('Go')
            messageText.setTextColor('green')
        elif distance(pt,quitButton.getCenter())<quitButton.getRadius():
            print('quit')
            finished = True
        else:
            messageText.setText('no button')
            messageText.setTextColor('red')

    
    win.close()