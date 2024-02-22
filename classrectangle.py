from datetime import datetime
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
        
    def area(self):
        return self.length * self.width
    
    
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
    
    

rect = rectangle(int(input("Enter the length of the rectangle : ")), int(input("Enter the width of the rectangle : ")))
print(f"The area of the rectangle is : {rect.area()} ")
print(f"The area of the rectangle is : {rect.perimeter()} ")

'''date1 = input("Enter the first date :")
date2 = input("Enter the 2nd date : ")
date3 = datetime.strptime(date1, "%Y-%m-%d")
date4 = datetime.strptime(date2, "%Y-%m-%d")
days = date3 - date4
print(days) '''