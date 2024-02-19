#Introduction to Classes in Python

#Defining a class

class Taco():
    
    #Every class has a constructor always the __init__ method
    def __init__(self,shell='soft', meat='beef', sauce = 'mild'):  #Every class method has self as a formal parameter
        self.shell = shell
        self.meat = meat
        self.sauce = sauce
        self.filling = []
        
    
    def getMeat(self):  #Accessor method
        return self.meat
    
    def getShell(self): #Accessor method
        return self.shell
    
    def getSauce(self):  #Accessor method
        return self.sauce
    
    def getFillings(self):  #Accessor method
        return self.filling
    
    def changeSauce(self,sauce):
        self.sauce = sauce
    
    def changeMeat(self,meat):
        self.meat = meat
    
    def changeShell(self,shell):
        self.shell = shell
    
    def addFilling(self, newfilling):
        self.filling = self.filling +[newfilling]
    
             
    #The __str__ method overloads the print function. It must return a string.
    
    def __str__(self):
        
        description = 'A {0},{1}-shell taco with {2}'.format(self.sauce,self.shell,self.meat)
        
        if len(self.filling) > 0:
            fillingString =','
            for item in self.filling[:-1]:
                fillingString = fillingString + ' '+item +','
            fillingString = fillingString[:-1] + ' and '+self.filling[-1]
        else:
            fillingString = ''
        return description + fillingString +'.'


#Examples 
#Create default Taco objects
taco1 = Taco()
taco2 = Taco()

#Creat non-default Taco object
taco3 = Taco('hard','tuna')
taco4 = Taco(meat='tofu',sauce = 'flaming')

#Change the sauce
taco3.changeSauce('hot')   #Notice the syntax: classObjectName.classMethod(parameter)

#Add some filling ingredients
taco1.addFilling('cheese')  
taco1.addFilling('lettuce')

for item in ['jalapenos','pickles','black_olives']:
    taco4.addFilling(item)





    
    
