from math import pi

    #Variables

di = float(input("Enter interior diameter here in inches: "))             #Asks for interior diameter and saves for later.
h = float(input("Enter interior height here in inches: "))                #Asks for interior height and saves for later.
prc = float(input("Enter how full you'd like the tank as a percent: "))   #Asks for how full it should be and saves for later.



print()

    #Calculations

vol = float((di/2)**2 * pi * h / 231)                                     #Calculates full volume based off of given values.
print("Full tank capacity is",round(vol,2),"gallons of water.")           #Prints volume while rounding at 2 decimal places.

cap = float(vol * prc * .01)                                              #Calculates how full they'd like it based off their %.
print("Filled to",str(prc)+"%","capacity requires",round(cap,2),"gallons of water.")                                                       #Prints with a rounding of 2.