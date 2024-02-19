class Cylinder():
    #Takes an input of Cylinder(radius,height)
    
    def __init__(self,r,h):
        self.__radius = r
        self.__height = h
        
    def getRadius(self):
        return self.__radius
    
    def getHeight(self):
        return self.__height
    
    def getVolume(self):
        from math import pi
        vol = self.__height*pi*self.__radius**2
        return round(vol,2)
        
    def __add__(self,c2):
        r = self.__radius + c2.getRadius()
        h = self.__height + c2.getHeight()
        return Cylinder(r,h)
    
    def __str__(self):
        return "Cylinder: radius {0}, height {1}, volume {2}".format(self.__radius,self.__height,self.getVolume())
      
a = Cylinder(2,8)
b = Cylinder(5,4)
c = a+b
print(c)