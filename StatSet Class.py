class StatSet():
    
    def __init__(self):
        self.__valList = []
    
    def values(self):
        return self.__valList
    
    def addNumber(self, x):
        self.__valList += [x]
        self.__valList.sort()
        pass
    
    def count(self):
        return len(self.__valList)
    
    def minVal(self):
        return self.__valList[0]
    
    def maxVal(self):
        return self.__valList[-1]
    
    
    def median(self):
        middle = len(self.__valList)/2
        
        
        if '.5' not in str(middle):
            middle = int(middle) - 1
            return self.__valList[middle],self.__valList[middle+1]
        else:
            middle = int(middle)
            return self.__valList[middle]
    
    
    def mean(self):
        summation=sum(self.__valList)
        return summation/len(self.__valList)
    
    
    
    
    def StdDev(self):
        from math import sqrt
        values = self.__valList
        mean = self.mean()
        
        sums = 0
        for number in values:
            sqr = (number-mean)*(number-mean)
            sums += sqr
        stdDev = round(sqrt(sums/len(self.__valList)),2)
        return stdDev

    
    
    
    
    
    
    
    
    
    
    
stats=StatSet()
stats.addNumber(1)
stats.addNumber(2)    
stats.addNumber(13)
stats.addNumber(17)
stats.addNumber(-31)
stats.addNumber(17)
stats.addNumber(3)
stats.addNumber(17)
stats.addNumber(20)
stats.addNumber(14)
stats.addNumber(-30)
stats.addNumber(-30)
    
    