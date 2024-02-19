from graphics import *

win = GraphWin('Bruteforce Shift Decryption',1250,500)
win.setCoords(-125,-50,125,50)

#Defines bottom left corner of 'quit' button for easy calibration and use.
quitX = -120
quitY = 40

#Defines the location corner of the 'plus' button.
plusX = 65
plusY = 23

#Defines the location of the 'minus' button relative to the 'plus' button.
minusX = plusX-7
minusY = plusY

#Defines the location where the 'output' is.
outputX = 0
outputY = 20



#Defines and draws the 'quit' button.
quitButton = Rectangle(Point(quitX,quitY),Point(quitX+12,quitY+5))
quitButton.setFill('crimson')
quitButton.draw(win)

#Defines and draws the welcome text.
decrpytText = Text(Point(0,38),"Enter the text you'd like to decrpyt:")
decrpytText.draw(win)

#Defines and draws the entry box.
decryptEntry = Entry(Point(0,32),80)
decryptEntry.setFill('lightgray')
decryptEntry.draw(win)

#Defines and draws the 'plus' button.
buttonPlus = Rectangle(Point(plusX,plusY),Point(plusX+5,plusY+5))
buttonPlus.setFill('lightgray')
buttonPlus.draw(win)

plus1 = Line(Point(plusX+2.5,plusY+1),Point(plusX+2.5,plusY+4))
plus1.setWidth(2)
plus1.draw(win)

plus2 = Line(Point(plusX+1,plusY+2.5),Point(plusX+4,plusY+2.5))
plus2.setWidth(2)
plus2.draw(win)

#Defins and draws the 'minus' button.
buttonMinus = Rectangle(Point(minusX,minusY),Point(minusX+5,minusY+5))
buttonMinus.setFill('lightgray')
buttonMinus.draw(win)

minus2 = Line(Point(minusX+1,minusY+2.5),Point(minusX+4,minusY+2.5))
minus2.setWidth(2)
minus2.draw(win)

#Defines and draws an area for text output that is used later.
decryptOut = Text(Point(outputX,outputY),'Output')
decryptOut.draw(win)



#Predefines shift amount for later use.
shiftAmount = 0



#Predefines finished for use in the WHILE loop.
finished = False

while not finished:
    
    #Uses click location to determine what action should be done next.
    click = win.getMouse()
    
    
    
    #Defines the x and y value of the point for ease of use in later IF statements.
    x = click.getX()
    y = click.getY()
    
    
    
    #Defines the string that will be used to shift as what is entered in the box.
    encryptString = str(decryptEntry.getText())
    
    #Predefines decryption text for ease of redefining.
    decryption = ''
    
    
    
    #IF statement that enacts a function based on click location.
    if quitX <= x <= quitX+12 and quitY <= y <= quitY+5:
        
        #If click is within 'quit' box, WHILE loop ends.
        finished = True
    
    
    
    #ELIF statement determining if a click is within the 'plus' or 'minus' square.
    elif plusX <= x <= plusX+5 and plusY <= y <= plusY+5 or minusX <= x <= minusX+5 and plusY <= y <= plusY+5:
        
        #IF statement on if a click is within 'plus' box.
        if plusX <= x <= plusX+5 and plusY <= y <= plusY+5:
        
            #Adds 1 to shift amount due to press of 'plus' button.
            shiftAmount = shiftAmount + 1
            decryptOut.setText(decryption)
            
            
            
        else:
        
            shiftAmount = shiftAmount - 1
            decryptOut.setText(decryption)
            
        for letter in encryptString:
            
                   
                
            decryptString = ord(letter)
            if ord(letter) == 32:
               newLetter = ord(letter)
               
            elif ord(letter) + shiftAmount < 97:
                while ord(letter) + shiftAmount < 97:
                    shiftAmount = shiftAmount + 26
                newLetter = decryptString + shiftAmount
                
            elif ord(letter) + shiftAmount > 122:
                while ord(letter) + shiftAmount > 122:
                     shiftAmount = shiftAmount - 26
                newLetter = decryptString + shiftAmount
                
            else:
                newLetter = decryptString + shiftAmount
            
            newLetter = chr(newLetter)
            
            
            decryption = decryption + newLetter
            
            
        decryptOut.setText(decryption)
        
        
        
        
        
    else:
        noClick = 1
        
        
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
win.close()