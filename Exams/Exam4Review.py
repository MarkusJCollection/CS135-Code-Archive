from matrixOps import *

#A. Here is an adjacency matrix for a digraph
A = [[0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0]]

#The vertex list for the digraph is [1,2,3,4,5]
# Without creating the Digraph object for the matrix, write the code to answer these questions.
#1. How many edges are in the digraph?
#2. What is the in-degree of vertex 4?
#3. How many paths of length 5 are there from vertex 2 to vertex 5?

from digraph1 import *

#B. 1. Create a digraph with vertex list [1,2,3,4,5,6,7,8,9,10].
#   2. Add an edge between vertices x and y if x is even and y is odd.
#

#C. The file words.txt contains many words. Use the data in this file to
#create a Digraph object with the following properties.
#1. Each distinct word is vertex.
#2. There is an edge from vertex x to vertex y only if len(x) > len(y)


#D.  Below is the beginning of a class called Stew

class Stew():
    def __init__(self, name, base = 'beef'):
        self.base = base
        self.name = name
        self.other = []


    def whatBase(self):
        return self.base
    
    
    
    def addIng(self,ingredientList):
        for item in ingredientList:
            self.other.append(item)
        return self.other
    
    
    def __str__(self):
        ingList = ''
        desc = '{0} is {1} stew with '.format(self.name,self.base)
        for item in self.other:
            
        return desc


b = Stew('barry')
b.addIng(['chicken','pork','lettuce','tomato'])




#1. Write an accessor method for self.base
#2. Write a method that adds items to the self.other list
#3. Write a __str__ method that works as follows:
#		Suppose the Stew object whoop = Stew('myStew','chicken')
#       and whoop.other is the list ['noodles','carrots','peppers']
#    then, print(whoop) will produce this string 'myStew is chicken stew with noodles, carrots, and peppers.'
