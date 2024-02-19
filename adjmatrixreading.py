from digraph1 import *


infile = open('adjacencymatrix.txt','r')



matrix = Digraph()

#Used to find how many lines are in the adjacency matrix.
i=0
for line in infile:
    matrix.addVertex(chr(97+i))
    i+=1
    
infile.close()



infile = open('adjacencymatrix.txt','r')

#Initializes i at -1 for it to count what matrix is being tampered with.
#Has 1 immediately added, therefore starting at 0.
i=-1
for line in infile:
    
    #Splits the line into a list of each value of the adjacency matrix.
    row = line.split()
    #For every number, it changes the value into an integer.
    rows = [int(a) for a in row]
    
    #Length of the matrix used for determining dimensions.
    length = len(row)
    
    #Accumulator specifying what row is being worked on.
    i+=1
    
    #For every value in a row, if it is equal to 1 then an edge is added between such vertices.
    for k in range(length):
        if rows[k] == 1:
            matrix.addEdge(chr(97+i),chr(97+k))

infile.close()