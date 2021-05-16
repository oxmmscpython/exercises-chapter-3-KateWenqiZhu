import numpy

class Circle:

    def __init__(self, centre, radius):
        self.radius = radius
        self.centre = centre

    def __contains__(self,other):
        diff=numpy.subtract(other,self.centre)
        if diff[0]**2+diff[1]**2 < self.radius**2:
            return True
        else: 
            return False
        