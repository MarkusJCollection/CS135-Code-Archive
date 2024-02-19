#CS135  Exam #4
#This is a code completion exam.
#Write the necessary code as needed.
#Upload this file when you finish.

#Enter your name here:   Markus Jesse   


#1.

"""Here is the beginning of a Pizza class. Write the methods as specified."""

class Pizza():
    def __init__(self,shape,crust):
        """shape options are 'round' and 'rectangular'
           crust options are 'thin' and 'thick' """
        self.shape = shape
        self.crust = crust
        self.toppings = []
    #a.  Write a method to add a topping to the toppings list
        
    def addTopping(self,item):
        if type(item) == list:
            for topping in item:
                self.toppings.append(topping)
        else:
            self.toppings += [item]
        pass
        
        
        
        
        
        
        
    #b.  Write an accessor method for shape
    def whatShape(self):
        return self.shape
        
    #c.  Suppose that the pizza object, P, is round, thick crust, and has pepperoni, bacon
        # and olives as toppings.  Write the __str__ method needed to produce
        #    'This is a round, thick crust pizza with pepperoni, bacon, and olives'
        # when print(P) is executed
        
  
    def __str__(self):
        desc = "The pizza is a {0}, {1} crust pizza".format(self.shape,self.crust)
        if len(self.toppings) > 0:
            desc += ' with'
            for topping in self.toppings[:-1]:
                desc += ' '+str(topping)+','
            desc += ' and ' + self.toppings[-1]
        desc += '.'
        return desc

        
        
        
        
       
P = Pizza('round','thick')
P.addTopping('pepperoni')
P.addTopping(['bacon','olives'])

P.whatShape()
print(P)




#2. The digraph1 file is in Moodle. Run the code below and then the code needed to answer the questions

from digraph1 import *

Q= Digraph()
for i in range(2,51):
    Q.addVertex(i)
#  Add an edge from each vertex to every vertex that is a divisor of the given vertex.
#  Thus, vertex 2 would have an edge to itself only, but vertex 50 would have edges to
#  vertices 2,5,10,25,and 50. Note: a is a divisor of b if b%a == 0.

for vertex in Q.vertexList:
    for i in range(2,51):
        if vertex%i == 0:
            Q.addEdge(vertex,i)


"""
Q.edgeSet
"""




#3.  The text file wordGraph.txt is in Moodle.


W =Digraph()

#Read that file to create a Digraph. Each word in the file is a vertex of W and
# there is an edge between two vertices if
# the vertex words have the same number of letters.

infile = open('wordGraph.txt','r')


for line in infile:
    line = line.split()
    for word in line:
        W.addVertex(word)
        
for vertex in W.vertexList:
    for other in W.vertexList:
        if other != vertex:
            if len(other) == len(vertex):
                W.addEdge(vertex,other)



infile.close()

"""
W.edgeSet
"""




#4.  Here is the adjacency matrix of a digraph.

A =[[1,0,1,0,0],[1,0,1,0,0],[0,1,0,0,0],[0,0,1,1,1],[1,1,0,0,0]]


# The ordered vertex list of the graph is ['a','b','c','d','e']
# Write the code to answer these questions using the matrix A.
# Do not make a Digraph object.


#a. What is the out-degree of vertex 'b'?
outB=0
for number in A[1]:
    if number == 1:
        outB += 1


#b. What is the in-degree of vertex 'c'?
inC = 0
for i in range(len(A)):
    if A[i][2] == 1:
        inC += 1
        
        



#c. How many paths of length 4 are there from vertex 'd' to vertex 'b'?
from matrixOps import *

B=SquareMatrix(A)**4

DtoB = B.matrix[3][1]





#d. Suppose we add an edge from vertex 'a' to vertex 'e'.  Change the
#  adjacency matrix to reflect that addition.
A[0][4] = 1


"""
print(outB)
print(inC)
print(DtoB)
print(A)
"""
        
          
    
    
