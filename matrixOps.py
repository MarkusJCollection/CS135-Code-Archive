#Square Matrix Class

class SquareMatrix():
    
    def __init__(self, array):
        self.matrix = array
        self.dim = len(array)
    
    def __add__(self,array2):
        row = [0]*self.dim
        newarray=[]
        for k in range(self.dim):
            newarray.append(row.copy())
        for i in range(self.dim):
            for j in range(self.dim):
                newarray[i][j]=self.matrix[i][j] + array2.matrix[i][j]
        new=SquareMatrix(newarray)
        return new
    
          
    def __mul__(self,m):
        row = [0]*self.dim
        newarray=[]
        for k in range(self.dim):
            newarray.append(row.copy())
        for i in range(self.dim):
            for j in range(self.dim):
                Cij=0
                for k in range(self.dim):
                    Cij=Cij+self.matrix[i][k]*m.matrix[k][j]
                newarray[i][j]=Cij
        new = SquareMatrix(newarray)
        return new
    
    def __pow__(self,n):
        new = self
        for i in range(n-1):
            new = new* self
        return new
    
    def __str__(self):
        string=''
        for i in range(self.dim):
            string=string+str(self.matrix[i])+'\n'
        return string