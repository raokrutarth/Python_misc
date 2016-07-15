#Krutarth Rao
import math
class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):

        area = math.pi*4*(self.radius**2)
        return area


    def volume(self):

        volume = (4/3) * math.pi * (self.radius**3)
        return volume
    
    
        
