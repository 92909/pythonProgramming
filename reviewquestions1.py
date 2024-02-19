class circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        area = 3.142 * self.radius ** 2
        print(area)
    def get_circumference(self):
        circumference = 3.142 * (self.radius * 2)
        print(circumference)
c = circle(7)
print(c)
c.get_area()
c.get_circumference()
