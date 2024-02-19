'''from datetime import datetime
dueDate = input("Enter the due date (YYYY-MM-DD): ")
returnDate = input("Enter the return date (YYYY-MM-DD): ")
date = datetime.strptime(dueDate, "%Y-%m-%d")
date1 = datetime.strptime(returnDate, "%Y-%m-%d")
daysOverdue = date1 - date
print(daysOverdue)
'''

class House():
    def __init__(self, location):
        self.location = location
    def chairs(self, colour, number):
        chairs_count = int(input("Enter the number of chairs : "))
        if chairs_count < 10:
            print(f"You have {chairs_count} chairs")
            print(f"They are of {colour} in colour")
        else:
            print(f"You have {chairs_count} chairs that are {colour} in colour")
    def television(self, numb, size, side):
        if numb >= 2:
            print(f"You have {numb} TVs that are on the {side}  side. they are {size} inches big")
        else:
            print(f"You have {numb} TV that is on the  {side} and is {size} inches big")

h = House("Ruiru")
h1 = House("Kiambu")
print(h.location)
print(h1.location)
h.chairs("grey", 10)
h.television(1, 72, "left")