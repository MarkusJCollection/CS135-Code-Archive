#Creating a list of Taco objects from a data file
#containing their ingredients

from tacoClass import *

def makeTaco(ingredients):
    """Makes a Taco object from a list of ingredients.
    Assumes the list entries appear in this order:
    shell,meat,filling1,filling2,filling3, filling4, sauce"""
    
    t = Taco(ingredients[0],ingredients[1])
    for i in range(2,6):
        t.addFilling(ingredients[i])
    if ingredients[6] != 'mild':
        t.changeSauce(ingredients[6])
    return t

#Open the file
tacofile = open('tacos.txt','r')

#Initialize the list of Tacos
tacoList = []
#Skip over the headings in the file
for i in range(4):
    tacofile.readline()
    

for taco in tacofile:    #Read each line of the file
    ingredients=taco.split()  #Make the string a list
    nextTaco = makeTaco(ingredients)  #Make a Taco object from the list
    tacoList=tacoList +[nextTaco]  #Add the Taco to the list of Tacos
#Close the file
tacofile.close()

hardCounter= 0
softCounter= 0
softMild= 0
hardChickenMild= 0
hardBeefFlamingJalapeno= 0

for taco in tacoList:
    if taco.shell == 'hard':
        if taco.meat == 'chicken' and taco.sauce == 'mild':
            hardChickenMild +=1
        elif taco.meat == 'beef' and taco.sauce == 'flaming' and 'jalapenos' in taco.filling :
            hardBeefFlamingJalapeno +=1
        hardCounter +=1
    elif taco.shell == 'soft':
        if taco.sauce == 'mild':
            softMild +=1
        softCounter+=1
