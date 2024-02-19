#CS135  Exam #4
#This is a code completion exam.
#Write the necessary code as needed.
#Upload this file when you finish.

#Enter your name here:      


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
    def addTopping(self,topping):
        self.toppings.append(topping)
        
    #b.  Write an accessor method for shape
    def getShape(self):
        return self.shape
    
    #c.  Suppose that the pizza object, P, is round, thick crust, and has pepperoni, bacon
        # and olives as toppings.  Write the __str__ method needed to produce
        #    'This is a round, thick crust pizza with pepperoni, bacon, and olives'
        # when print(P) is executed
    def __str__(self):
        string ='This is a '+self.shape + ', '+self.crust + ' crust pizza with'
        for t in self.toppings[:-1]:
            string = string + ' '+ t + ','
        string = string + ' and '+self.toppings[-1]
        return string

p = Pizza('round','thick')
print(p)










#2. The digraph1 file is in Moodle. Run the code below and then the code needed to answer the questions

from digraph1 import *

Q= Digraph()
for i in range(2,51):
    Q.addVertex(i)
#  Add an edge from each vertex to every vertex that is a divisor of the given vertex.
#  Thus, vertex 2 would have an edge to itself only, but vertex 50 would have edges to
#  vertices 2,5,10,25,and 50. Note: a is a divisor of b if b%a == 0.
for v in Q.vertexList:
    for n in range(2,v):
        if v%n == 0:
            Q.addEdge(v,n)
print('\nQ:\n{0}'.format(Q))

#3.  The text file wordGraph.txt is in Moodle.


W =Digraph()

#Read that file to create a Digraph. Each word in the file is a vertex of W and
# there is an edge between two vertices if
# the vertex words have the same number of letters.
infile = open('wordGraph.txt','r')
for line in infile:
    linelist = line.split()
    for w in linelist:
        if w not in W.vertexList:
            W.addVertex(w)
infile.close()
for word1 in W.vertexList:
    for word2 in W.vertexList:
        if len(word1) == len(word2):
            W.addEdge(word1,word2)

print('\nW:\n{0}'.format(W))

#4.  Here is the adjacency matrix of a digraph.



A =[[1,0,1,0,0],[1,0,1,0,0],[0,1,0,0,0],[0,0,1,1,1],[1,1,0,0,0]]

#The ordered vertex list of the graph is ['a','b','c','d','e']

# Write the code to answer these questions using the matrix A.  
# Do not make a Digraph object.

#a. What is the out-degree of vertex 'b'?

outCount = 0
for item in A[1]:
    if item == 1:
        outCount+=1
print("The out-degree of vertex 'b' is",outCount)

#b. What is the in-degree of vertex 'c'?

inCount = 0
for row in A:
    if row[2] == 1:
         inCount+=1
print("The in-degree of vertex 'c' is",inCount)

#c. How many paths of length 4 are there from vertex 'd' to vertex 'b'?
from matrixOps import *
Am = SquareMatrix(A)
A2=Am**4

print("There are {0} paths of length 4 from vertex 'd' to vertex 'b'.".format(A2.matrix[3][1]))

#d. Suppose we add an edge from vertex 'a' to vertex 'e'.  Write the code to change the
#  adjacency matrix to reflect that addition.

A[0][4]=1

print('\nA with new edge from a to e:')
print(A)


    
