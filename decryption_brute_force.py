from graphics import *

win = GraphWin('Bruteforce Shift Decryption',1250,500)
win.setCoords(-125,-50,125,50)


quitX = -120
quitY = 40

buttonX = 60
buttonY = 25

plusX = 65
plusY = 23

minusX = plusX-7
minusY = plusY

outputX = 0
outputY = 20









quitButton = Rectangle(Point(quitX,quitY),Point(quitX+12,quitY+5))
quitButton.setFill('crimson')
quitButton.draw(win)






decrpytText = Text(Point(0,38),"Enter the text you'd like to decrpyt:")
decrpytText.draw(win)



decryptEntry = Entry(Point(0,32),80)
decryptEntry.setFill('lightgray')
decryptEntry.draw(win)


"""
decryptHelp1 = Text(Point(buttonX,buttonY),'Shift Right Once')
decryptHelp1.draw(win)

decryptHelp2 = Text(Point(buttonX,buttonY-7),'Shift Left Once')
decryptHelp2.draw(win)
"""







buttonPlus = Rectangle(Point(plusX,plusY),Point(plusX+5,plusY+5))
buttonPlus.setFill('lightgray')
buttonPlus.draw(win)

plus1 = Line(Point(plusX+2.5,plusY+1),Point(plusX+2.5,plusY+4))
plus1.setWidth(2)
plus1.draw(win)

plus2 = Line(Point(plusX+1,plusY+2.5),Point(plusX+4,plusY+2.5))
plus2.setWidth(2)
plus2.draw(win)









buttonMinus = Rectangle(Point(minusX,minusY),Point(minusX+5,minusY+5))
buttonMinus.setFill('lightgray')
buttonMinus.draw(win)

minus2 = Line(Point(minusX+1,minusY+2.5),Point(minusX+4,minusY+2.5))
minus2.setWidth(2)
minus2.draw(win)


"""
buttonMinus = Rectangle(Point(buttonX-2,buttonY-2),Point(buttonX+3,buttonY+3))
buttonMinus.setFill('lightgray')
buttonMinus.draw(win)

minus = Line(Point(buttonX-1,buttonY+.5),Point(buttonX+2,buttonY+.5))
minus.setWidth(2)
minus.draw(win)
"""







decryptOut = Text(Point(outputX,outputY),'Output')
decryptOut.draw(win)



shiftAmount=0
finished = False

while not finished:
    click = win.getMouse()
    x = click.getX()
    y = click.getY()
    
    encryptString = str(decryptEntry.getText())
    
    decryption = ''
    if quitX <= x <= quitX+12 and quitY <= y <= quitY+5:
        finished = True
     
    elif plusX <= x <= plusX+5 and plusY <= y <= plusY+5:
        
        shiftAmount = shiftAmount + 1
        
        
        
        
        
        
    elif minusX <= x <= minusX+5 and plusY <= y <= plusY+5:
        
        shiftAmount = shiftAmount - 1
        
        
        
        
        
        
    else:
        for letter in encryptString:
            
            decryptString = ord(letter)
            newLetter = decryptString + shiftAmount
            decryption = decryption + chr(newLetter)
        decryptOut.setText(decryption)
        
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
win.close()