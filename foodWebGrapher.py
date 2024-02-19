foodweb = open('foodweb.txt','r')

from digraph import *


Web = Digraph()






for line in foodweb:
    if line != '\n':
        animals = line.split(':')
        source = animals[0]
        
        Web.addVertex(source)
        
        
        
        food = animals[1][:-1]
        if food != ' None':
            prey = food.split(',')
            for item in prey:
                Web.addEdge(source,item)






"""    
for line in foodweb:
    if line != '\n':
        line = line.split(':')
        source = line[0]
        Web.addVertex(source)
        if line[1] != ' None ':
            prey = line[1][:-1].split(',')
            for animal in prey:
                    Web.addEdge(source,animal)
            
"""





vertN = len(Web.vertexList)
scorp = len(Web.edgeSet['Scorpion'])


def whatEat(animal):
    return len(Web.edgeSet[animal])

def eats(prey):
    eaterList = []
    for animal in Web.vertexList:
        eater = Web.edgeSet[animal]
        if prey in eater:
            eaterList += animal
    return eaterList


for eater in Web.vertexList:
    highest = 0
    length = len(eater)
    if length > highest:
        highest = length
        high = eater





foodweb.close()