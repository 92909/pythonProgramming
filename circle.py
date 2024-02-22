import math

class circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)
        
    def circumference(self):
        return math.pi * (self.radius * 2)
cir = circle(int(input("Enter the radius of the circle : ")))
print(cir.area())
print(cir.circumference())