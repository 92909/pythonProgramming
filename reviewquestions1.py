import math

class circle:
    def __init__(self, pi, radius):
        self.pi = pi
        self.radius = radius
    def get_area(self):
        area = math.pi * (self.radius ** 2)
        print(f"The area of the circle is : {area}")
    def circumference(self):
        circumference = math.pi * (self.radius * 2)
        print(f"The circumference of the circle is : {circumference}")
c = circle(math.pi, int(input("Enter the radius of the circle : ")))
c.get_area()
c.circumference()
