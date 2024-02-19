#November 13 Assignment

from digraph1 import *

W = Digraph()

f = open('following.txt','r')
for line in f:
    if line !='\n':
        linelist = line[:-1].split(':')
        source = linelist[0]
        destinationList = linelist[1].split(',')
        for dest in destinationList:
            if dest[-1]=='\n':
                dest = dest[:-1]
            W.addEdge(source,dest)
f.close()

W.vertexList.sort()
AM = W.adjMatrix()

fa = open('followingMatrix.txt','w')
for row in AM:
    for entry in row[:-1]:
        print(entry, end = ' ',file = fa)
    print(entry, file = fa)
fa.close()

#November 15

from matrixOps import *
AMS = SquareMatrix(AM)

P2 = AMS*AMS

whoIndex = []
for i in range(P2.dim):
    if P2.matrix[i][i] != 0:
        whoIndex.append(i)

whoNames = [W.vertexList[i] for i in whoIndex]

print(whoNames)



