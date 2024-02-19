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
                
    def outDegree(self,v):
        if v in self.vertexList:
            return len(self.edgeSet[v])
        else:
            return -1  #indicates v is not a vertex in the digraph
    
    def inDegree(self,v):
        if v in self.vertexList:
            count = 0
            for w in self.vertexList:
                if v in self.edgeSet[w]:
                    count+=1
            return count
        else:
            return -1   #indicates v is not a vertex in the digraph
        
         
    def __str__(self):  #presents the Digraph in the form
                        # source: destination1, destination2, ...
         string=''
         for vertex in self.edgeSet:
             vstring=str(vertex)+':'
             if self.edgeSet[vertex] !=[]:
                 for v in self.edgeSet[vertex]:
                    vstring=vstring+ str(v)+','
             else:
                 vstring=vstring + ' None '
                
             string=string +vstring[:-1]+'\n'
         return string
        
        
    def adjMatrix(self):
        """returns the adjacency matrix for the digraph"""
        k = len(self.vertexList)  #number of rows and columns
        row = []  #initialize a row
        for i in range(k):  #populate the row with zeroes
            row.append(0) 
        matrix = [row]  #initialize the matrix with 1 row
        for i in range(k-1): #add additional rows
            matrix.append(row.copy())
        
        #Now loop through the matrix indices and insert 1 as needed
        for i in range(k):
            q=self.edgeSet[self.vertexList[i]]
            for j in range(k):
                v =self.vertexList[j]
                if v in q:
                    
                    matrix[i][j]=1   #There is an edge from vertex i to vertex j
        return matrix


