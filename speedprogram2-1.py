    #Enables the use of the graphics module.
from graphics import *



    #Sets the size of the window, and its coordinate values.
win = GraphWin('Fine Calculator',350,250)
win.setCoords(-35,0,35,50)



    #Defines y and x values for use in text and rectangle transformations.
    ##Mainly for ease of moving text around.
yL = 35
yC = yL-5
yO = yL-15

xCalc = 18
yCalc = 10

xQuit = -32
yQuit = 42



    #Creates rectangles with the text 'Quit' and 'Calculate' inside of them.
quitButton = Rectangle(Point(xQuit,yQuit),Point(xQuit+7,yQuit+5))
quitText = Text(Point(xQuit+3.5,yQuit+2.5),'Quit')

calcButton = Rectangle(Point(xCalc,yCalc),Point(xCalc+14,yCalc+5))
calcText = Text(Point(xCalc+7,yCalc+2.5),'Calculate')


    #Creates the input text and box for the speed limit and clocked speed.
limitAsk = Text(Point(0,yL),'The speed limit is             mph.')
limitInput = Entry(Point(9,yL),5)

clockedAsk = Text(Point(0,yC),'I was going             mph.')
clockedInput = Entry(Point(4.5,yC),5)


    #Sets the positioning for the output text, and is blank for filler.
outputFine = Text(Point(0,yO),'')
outputFlavor = Text(Point(0,yO-5),'')

tryAgain = Text(Point(0,5),'')



    #Drawing of each button, and their colorations.
quitButton.setFill('crimson')
quitButton.draw(win)
quitText.draw(win)

calcButton.setFill('lightGreen')
calcButton.draw(win)
calcText.draw(win)


    #Drawing of question text and their boxes with coloration.
limitAsk.draw(win)
limitInput.setFill('lightgray')
limitInput.draw(win)

clockedAsk.draw(win)
clockedInput.setFill('lightgray')
clockedInput.draw(win)


    #Drawing of the output texts.
outputFine.draw(win)
outputFlavor.draw(win)

tryAgain.draw(win)



    #Predefines finished as a boolean for later use in the WHILE function.
finished = False


    #While function used to determine where the user clicks, and what operation should be done next.
while not finished:
    
        #Function used to determine where the user clicked.
    pt = win.getMouse()
    

        #First IF statement, which looks to see if the user pressed within the region of the 'Quit' button.
        ##If so, it terminates the WHILE program by making finished = true.
    if xQuit < pt.getX() < xQuit+7 and yQuit < pt.getY() < yQuit+5:
        finished = True
        
        #Second part of the IF statement, checks to see if the user has pressed within the region of the 'Calculate' button.
    elif xCalc < pt.getX() < xCalc+14 and yCalc < pt.getY() < yCalc+5:
        
            #Sets the inputs as integers to allow for use in mathematical expressions.
        speedLimit = float(limitInput.getText())
        clockedSpeed = float(clockedInput.getText())
        
            #Determines whether the clocked speed is higher, while also calculating a fine value for the difference.
        x = clockedSpeed - speedLimit
        fine90 = str(float((x*5)+200))
        fine = str(float(x*5))
        
            #IF statement based off the determination whether the clocked speed is higher than the speed limit.
        if x<=0:
            
            outputFine.setText("You weren't speeding.")
            outputFlavor.setText('Great work!')
                
                
            #Secondary ELIF statement based on whether or not the speed is over 90mph for the extra $200.
        elif clockedSpeed>=90:
            
            outputFine.setText('Your fine is $'+fine90)
            outputFlavor.setText('')
            
            
            #Final ELSE statement where it shows the fine for a speed over the limit but under 90mph.
        else:
            
            outputFine.setText('Your fine is $'+fine)
            outputFlavor.setText('')
    
        #Ending ELSE statement if the user clicks in anywhere other than an input box, or the buttons.      
    else:
        tryAgain.setText('Click a button or text box to continue!')
        
        
             
    #Closes window after the termination of WHILE, which is from the pressing of the 'Quit' button.
win.close() 