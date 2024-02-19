# Series with GUI
# by Bellatrix Lastrange
# September 4, 2023

#The function F approximates PI using the series x/1-x/3+x/5-x/7+...

#import the math library value for pi
from math import pi
from graphics import *

#The function does the work
def main():
    win =GraphWin('PI',600,600)
    win.setCoords(-100,-100,100,100)
    head=Text(Point(0,90),"This program approximates pi using the series 4 - 4/3 + 4/5 - 4/7 + ...")
    head.draw(win)
    entryText=Text(Point(0,70),  "How many terms should I use to calculate? ")
    entryText.draw(win)
    entryBox = Entry(Point(0,60),10)
    entryBox.setFill('orchid')
    entryBox.draw(win)
    win.getMouse()
    terms = entryBox.getText()
    n=int(terms)
    
    total=0
    for i in range(n):
        total = 4*(-1)**i/(2*i+1) +total
    
    rtotal = round(total,12)
    rpi = round(pi,12)
    outText1 = Text(Point(0,0),"The approximation to pi using "+str(n)+ " terms is " + str(rtotal))
    outText1.draw(win)
    outText2 = Text(Point(0,-10),"The math library says pi is "+str(rpi))
    outText2.draw(win)
    diff = round(pi - total,12)
    outText3 = Text(Point(0,-30),"The approximation differs from the math library value by "+str(diff))
    outText3.draw(win)
    win.getMouse()
    win.close()
main()    