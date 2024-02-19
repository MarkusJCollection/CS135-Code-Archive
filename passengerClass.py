#Passenger Class

class Passenger():
    def __init__(self, cabinclass,age:float,gender,survived,lastname, firstname):
        self.cabinclass = cabinclass
        self.age = age
        self.gender = gender
        self.__survived = survived  #hidden
        self.__lastname = lastname  #hidden 
        self.__firstname = firstname #hidden 
    
    def getAge(self):
        return self.age
    
    def getGender(self):
        return self.gender
    
    def getCabin(self):
        return self.cabinclass
    
    def getSurvived(self):
        return self.__survived
    
    def getName(self):
        return self.__firstname + ' '+self.__lastname
    
    def __str__(self):
        if self.__survived == '1':
            survived = 'survived'
        else:
            survived = 'did not survive'
        return self.getName()+' age '+ str(self.age) + ' '+ survived + ' the disaster.'

#Example
p1 = Passenger('2',45.5,'M','0','Potter','Dr. Cyrus Q.')
p2 = Passenger('2',40,'F','1','Potter','Mrs. Cyrus Q.')
#print(p1)
#print(p2)
