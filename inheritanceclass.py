class clothes:
    def __init__(self, color, price, name):
        self.color = color
        self.price = price
        self.name = name
    def show(self):
        print(f"This {self.name} is of colour {self.color} and costs kshs {self.price}")
    def kimani(self):
        print("My name is Kimutai")
        
class t_shirt(clothes):
    def kim(self):
        print("kim")
class trousers(clothes):
    def kim(self):
        print("Kimani")
class hood(clothes):
    def kim(self):
        print("Kimutai")

c = clothes("red", 1000, "clothes")
c.show()
t = t_shirt("black", 500, "t-shirt")
t.kimani()
t.kim()
tr = trousers("dark-grey", 2000, "trousers")
tr.kimani()
tr.kim()




'''
try:
    kim = int(input("Number : "))
    print(kim)
except:
    print("Invalid answer ! ")'''