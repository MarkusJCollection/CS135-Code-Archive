#Directed Graph Class
# A directed graph consists of a set of vertices and a set of edges

class Digraph():
    def __init__(self):
        self.edgeSet={}   #edgeSet is a dictionary whose key is a vertex
                          #and whose value is a list of adjacent vertices
        
        self.vertexList=[]  #vertexList is a list of all vertices in the Digraph
        
    def addVertex(self,v):   #Adds a vertex to the Digraph
        if v not in self.vertexList:
            self.vertexList.append(v)
            self.edgeSet[v]=[]
    
    def addEdge(self, source, destination):  #Adds an edge to the Digraph
        
        if source in self.vertexList:   #is source already in Digraph?
            self.edgeSet[source].append(destination)
            
        else:
            self.vertexList.append(source)
            self.edgeSet[source]=[destination]
       
        if destination not in self.vertexList:  #is destination already in Digraph?
                self.addVertex(destination)
                
       
    def __str__(self):  #presents the Digraph in the form
                        # source: destination1, destination2, ...
         string=''
         for vertex in self.edgeSet:
             vstring=str(vertex)+': '
             if self.edgeSet[vertex] !=[]:
                 for v in self.edgeSet[vertex]:
                    vstring=vstring+ str(v)+', '
             else:
                 vstring=vstring + ' None  '
                
             string=string +vstring[:-2]+'\n'
         return string
"""
#Here's an example that constructs a Digraph object, g1, manually.
#This is the digraph in the Introduction to Digraphs document
g1=Digraph()   #Make a Digraph object
g1.addVertex(1)  #add a vertex called 1
g1.addEdge(1,2)  #make an edge from vertex 1 to vertex 2
g1.addEdge(1,3)
g1.addEdge(1,4)
g1.addEdge(3,2)
g1.addEdge(2,4)
   

print('g1: ')
print(g1) #uses the _str_ method

#Here's an example of constructing a Digraph object, g2, from a data file.
#The file graph1.txt is in Moodle.

infile=open('graph1.txt','r')  
g2=Digraph()
for line in infile:
    if line !='EOF':
        lineList=line[:-1].split(',')
        v=lineList[0]
        g2.addVertex(v)
        for u in lineList[1:]:
            g2.addEdge(v,u)
infile.close()


print('g2:')
print(g2)
 """ 
