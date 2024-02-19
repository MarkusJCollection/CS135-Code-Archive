#The Rooted Tree class

from digraph1 import *

#----------------------RootedTree Class ------------------------

class RootedTree(Digraph):  #The RootedTree class inherits from the Digraph class
    
#I need a root, so we change __init__
    
    def __init__(self,root):
        
        self.root=root
        self.edgeSet={root:[]}
        self.vertexList=[root]

#Rooted trees are special so we change addEdge and addVertex
    def addEdge(self, source,destination):

        if source not in self.vertexList:
            print('Error: You cannot add an edge unless the source is in the tree')

        elif destination in self.vertexList:
            print('Error: A destination cannot have in-degree > 1')
            
        else:
            self.vertexList.append(destination)
            self.edgeSet[destination]=[]
            self.edgeSet[source].append(destination)
            
#Vertices cannot be added without an edge to an existing vertex, so this method gives an error
    def addVertex(self,v):
        print('Error: You cannot add a new vertex that is not connected to an existing vertex.')
        
#All other methods are inherited from Digraph, but we can write new methods that are
#specific to trees.

    def isLeaf(self,v):
        """A Boolean method that tells whether or not a vertex is a leaf"""
        if self.outDegree(v) == 0:
            return True
        else:
            return False
        
    def parent(self,v):
        """returns the parent of vertex v"""
        if v == self.root:
            return None
        else:
            for w in self.vertexList:
                if v in self.edgeSet[w]:
                    return w
    
    def children(self,v):
        """returns a list of the children of vertex v"""
        return self.edgeSet[v]
    
    def grandparent(self,v):
        """returns the grandparent of vertex v"""
        return self.parent(self.parent(v))
    
    def siblings(self,v):
        """returns a list of the siblings of vertex v"""
        sibs =[]
        for w in self.vertexList:
            if self.parent(v)==self.parent(w) and v != w:
                sibs.append(w)
        return sibs
    
    def cousins(self,v):
        """returns a list of the cousins of vertex v"""
        cous = []
        for w in self.vertexList:
            if self.parent(w) in self.siblings(self.parent(v)):
                cous.append(w)
        return cous
    
    def depth(self,v):
        """Finds the depth of a vertex v recursively""" 
        if v == self.root:
            return 0
        else:
            return 1+ self.depth(self.parent(v))
              
#Here's an example.
r=RootedTree(1)        #            1
r.addEdge(1,3)         #           /|\
r.addEdge(3,2)		   #          3 7 5
r.addEdge(2,4)         #         / / \ \
r.addEdge(1,5)         #        2 8   9 10
r.addEdge(2,6)		   #       / \ 
r.addEdge(1,7)         #      4   6
r.addEdge(7,8)		   #
r.addEdge(7,9)         
r.addEdge(5,10)		   

"""
print('The out-degree of vertex 1 is: ',r.outDegree(1))
print('The list of children of vertex 2 is ',r.children(2))
print('The list of siblings of vertex 7 is ',r.siblings(7))
print('The grandparent of vertex 6 is ',r.grandparent(6))
print('The list of the cousins of vertex 9 is ',r.cousins(9))
print('\nThe rooted tree r.')
print(r)
"""
