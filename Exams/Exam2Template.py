#Exam 2 is a code completion exam.
#You will write the code needed to finish the program
#as described in the handout.
#Begin by adding your name to these comments
#

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
         
    
win.getMouse()
win.close()



