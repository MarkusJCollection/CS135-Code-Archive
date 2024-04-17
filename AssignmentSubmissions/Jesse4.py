# CS135 Program 4
# Regression Line
# by: Markus Jesse
# 10/13/23

    
    #Imports graphics for use in creating the user interface.
from graphics import *


    #Creates a graphical window at the designated size.
win = GraphWin('Regression Line', 500, 500)
win.setCoords(0,0,10,10)
win.setBackground('lightgray')


    #Defining of multiple functions for later use within the program.
def point():
    #Gets a point clicked within a graphics window and returns the point, x value, and y value.
    pt = win.getMouse()
    x = float(pt.getX())
    y = float(pt.getY())
    return pt,x,y

def summation(val,total):
    #Calculates a total using the previous total and the new value returning the total.
    total = total + val
    return total

def mean(total,howMany):
    #Calculates the mean using a total of all elements and number of elements returning the mean
    mean = total/howMany
    return mean

def rectangledraw(x,y,h,w):
    #Defines a rectangle centered on the x and y value with a specified length and width returning the graphical rectangle and its points.
    height = 1/2*h
    width = 1/2*w
    p1 = Point(x-width,y-height)
    p2 = Point(x+width,y+height)
    return Rectangle(p1,p2),p1,p2
    
    
    
    #Definition and drawing of a rectangle using a previously defined function.
rect,r1,r2 = rectangledraw(7.5,1,.5,3.25)
rect.setFill('salmon')
rect.draw(win)



    #Definition and drawing of the text within the rectangle.
rectText = Text(Point(7.5,1),"Draw Regression Line")
rectText.draw(win)



    #Definition and drawing of the beginning text welcoming the user.
entryText = Text(Point(5,8),"This program creates a regression line.")
entryText2 = Text(Point(5,7.6),"Click anywhere in the open space to get started.")
entryText3 = Text(Point(5,7.2),"Click the rectangle button when you are done to draw the line.")

entryText.draw(win)
entryText2.draw(win)
entryText3.draw(win)
    
    
    
    
   
    #Predefining of variables used later in the program.
finished = False
totalX,totalXX,totalY,totalXY,howMany = 0,0,0,0,0


    #While function established to allow the user to click within the window multiple times.
while not finished:
    
        #Grabs materials from previously defined point function for use in the program.
    pt,x,y = point()
    
        #Removes the welcome text to allow the user more room to add points.
    entryText.setText('')
    entryText2.setText('')
    entryText3.setText('')
    
    
    
    
    
        #If function used to determine where the user clicks, and what should be done next.
    if r1.getX() < x < r2.getX() and r1.getY() < y < r2.getY():
        
        
            #Calculation of the final mean and slope of all x values.
        meanX = mean(totalX,howMany)
        meanY = mean(totalY,howMany)
        slope = (totalXY - howMany * meanX * meanY)/(totalXX - howMany * meanX * meanX)
        
        
            #Calculation of f(0) and f(10) for drawing the regression line.
        f0 = meanY + slope*(0-meanX)
        f10 = meanY + slope*(10-meanX)
        
        
            #Defining and drawing the regression line at previously defined points.
        regressLine = Line(Point(0,f0),Point(10,f10))
        regressLine.draw(win)
        
        
            #Output of the slope within the rectangular button in the beginning.
        slopeOutput = str(round(slope,2))+' x '+str(round(f0,2))
        rectText.setText('y ='+slopeOutput)
        
        
            #Redefinition of finished to true to end the while program.
        finished = True
       
       
       
    else:
        
            #Accumulation functions using the previously defined summation.
        totalX = summation(x,totalX)
        totalXX = summation(x**2,totalXX)
        totalY = summation(y,totalY)
        totalXY = summation(x*y,totalXY)
        
        
            #Draws where the user clicks as a visual aid.
        pt.draw(win)
        
            #After every click outside the text it adds another value to the total number of clicks that have been made.
        howMany += 1
        
        

    #After the user chosen to draw the regression line program waits for another click before closing.
win.getMouse()
win.close()

