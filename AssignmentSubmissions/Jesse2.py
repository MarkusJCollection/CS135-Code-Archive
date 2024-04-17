# CS135 Program 2
# Pi Approximation Using Infinite Series
# by: Markus Jesse
# 9/1/23


    #Intro to the program and gives explanation on what it does through use of print().
print("This program allows you to estimate the value of pi up to")
print("5 separate times using the series of 4/1 - 4/3 + 4/5 - 4/7 +...")
print()


    #Loops 5 times for multiple uses without re-running the program.
for a in range(5):
    
    
        #Asks for the number of terms the user would like to use and defines it as n.
    n = int(input("Enter the number of terms you'd like to use for approximation: "))
    print()


        #Sets the pi approximation to 0, and runs the number of terms that the user inputted.
    approxPi = 0
    for i in range(1,n+1):                                 #Sets the domain to be [1,n].
        term = float(4/(2*i-1))                            ##Redefines getting each term starting with 4/1, and so on each loop.
        approxPi = float(approxPi+term*(-1)**(i+1))        ###Using the terms calculated, it sums them up with alternating signs,
                                                           ###redefining itself each run


        #Imports pi from the math library.
    from math import pi           


        #End text giving the approximations, the given value of pi, and the difference between.
    print("Using",n,"terms, your",int(a+1),"approximation of pi is:",approxPi)
    print("The value of pi used in the math library is:",pi)
    print("And the difference between the two values is:",abs(pi-approxPi))
    print()
    print()
    
    
