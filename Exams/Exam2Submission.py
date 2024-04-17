#Exam 2 is a code completion exam.
#You will write the code needed to finish the program
#as described in the handout.
#Begin by adding your name to these comments
#Markus Jesse

from graphics import *
from math import sqrt
win = GraphWin("Wind Chill", 500,500)
win.setCoords(-50,-50,50,50)
headText = Text(Point(0,45), "Wind Chill Calculator")
headText.draw(win)
instText = Text(Point(0,35),"Enter the temperature and wind speed \n click on Go to calculate the wind chill")
instText.draw(win)
tempText = Text(Point(-25,25),"Fahrenheit temperature")
tempText.draw(win)
windText = Text(Point(-20,20), "Wind Speed")
windText.draw(win)
tempEntry = Entry(Point(5,25),10)
tempEntry.setFill('orchid')
tempEntry.draw(win)
windEntry = Entry(Point(5,20),10)
windEntry.setFill('orchid')
windEntry.draw(win)
goButton = Circle(Point(25,22.5),5)
goButton.setFill('light green')
goButton.draw(win)
goText = Text(Point(25,22.5),'Go')
goText.draw(win)
#Your code will go here

#Defines location of output text for try again and final product.
output = Text(Point(-20,-20),'')
output.draw(win)




#This function computes the distance between two Point
#objects 
def distance(p1,p2):
    """Assumes p1 and p2 are graphics.Point objects"""
    from math import sqrt
    dx = p1.getX()-p2.getX()
    dy = p1.getY()-p2.getY()
    dist = sqrt(dx**2+dy**2)
    return dist


#Predefines finished for use in WHILE
finished = False

#While used for constantly finding user click locations.
while not finished:
    click = win.getMouse()
    
    
    #Determines if click is within go button, and if so computes equation using given numbers.
    if distance(click,goButton.getCenter())<=5:
        Temp = int(tempEntry.getText())
        Vel = int(windEntry.getText())
        formula = round(35.74 + 0.6215*Temp - 35.75*(Vel**0.16) + 0.4275*Temp * (Vel**0.16),2)
        formula = str(formula)
        output.setText('The wind chill is '+formula+' degrees.')
        finished = True

    #Tells the user to try again if click is outside of go button location.
    else:
        output.setText('You must click in the Go button. Try again')
        
        
#Closes window after the user clicks again inside the window.
win.getMouse()
win.close()































