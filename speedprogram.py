from graphics import *
win = GraphWin('Fine Calculator',350,500)
win.setCoords(-35,-50,35,50)

def distance(p1,p2):
    """Assumes p1 and p2 are graphics.Point objects"""
    from math import sqrt
    dx = p1.getX()-p2.getX()
    dy = p1.getY()-p2.getY()
    dist = sqrt(dx**2+dy**2)
    return dist

quitButton = Rectangle(Point(-32,42),Point(-25,47))
quitButton.setFill('Crimson')
quitButton.draw(win)

quitText = Text(Point(-28.5,44.5),'Quit')
quitText.draw(win)

limitAsk = Text(Point(-15,10),'The speed limit is')
limitInput = Entry(Point(3,10),5)
limitAsk2 = Text(Point(12,10),'mph.')

clockedAsk = Text(Point(-11,5),'I was going')
clockedInput = Entry(Point(3,5),5)
clockedAsk2 = Text(Point(12,5),'mph.')

limitAsk.draw(win)
limitAsk2.draw(win)

clockedAsk.draw(win)
clockedAsk2.draw(win)


clockedInput.setFill('lightgray')
clockedInput.draw(win)

limitInput.setFill('lightgray')
limitInput.draw(win)






finished = False
while not finished:
    
    pt = win.getMouse()
    if -32 < pt.getX() < -25 and 42 < pt.getY() < 47:
        finished = True
    else:
        
        speedLimit = int(limitInput.getText())
        clockedSpeed = int(clockedInput.getText())
        x = clockedSpeed - speedLimit
        fine90 = str(float((x*5)+200))
        fine = str(float(x*5))
        if x<=0:
            if clockedSpeed>=90:
                print("You weren't speeding but still fined $200")
            else:
                print("You weren't speeding.")
        else:
            if clockedSpeed>=90:
                print('$'+fine90+' is the fine.')
            else:
                print('$'+fine+' is the fine.')

win.close()






                
                