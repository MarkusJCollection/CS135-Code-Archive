#multidimensional arrays

def howtoIndex():
    multi=[[1,5],[5,3],[0.5,35]]
    print(multi)
    
    print(multi[1])
    print(multi[1][1])
    
    
    multi[1].append(4)
    multi.append([4])
    print(multi)
    
def matrixUsage():
    
    """a lot of this works with each inner list not being even,
    but bear in mind most usages will work if they are."""
    
    matrix=[[1,2,3],[4,5,6],[7,8.6,999],[.5,6,3]]
    
    print("Row Num:",len(matrix)) 
    print("Row Num:",len(matrix[0])) #(assuming all are even)
    
    #finds sum of array 
    sumA=0
    for i in matrix:
        for j in i:
            sumA+=j
        print("Current sum:{0}".format(sumA))
    print ("Sum:{0}".format(sumA))
    
    if 4 in matrix: 
        print("4 was found in matrix.")
        #wont find it, since there are only lists in "level 1" of the matrix
    if 4 in matrix[1]:
        print("4 is in row 1 of the matrix.")
    
    


