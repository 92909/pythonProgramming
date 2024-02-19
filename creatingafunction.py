weight = int(input("Enter your weight : "))
unit = input("Enter the units for your weight (K) and L for pounds : ")
units = unit.upper()
if units == "K":
    total_weight = weight * 2.20462
    print(f"You weight is {total_weight} pounds")
elif units == "L":
    total_weight = weight / 2.20462
    print(f"YOur total weight is {total_weight} KGS.")
else:
    print("Please re-run the program to re-enter your weight!")
i = 1
while i <= 10:
    print(i * "*")
    i = i + 1

list = [1, 2, 5 ,3, 4]
list.remove(5)
print(list)
list.insert(4, 5)
print(list)
print(4 in list)
print(len(list))
   

numbers = [1, 2 ,3, 4, 5]
for list in numbers:
    print(list)
print(len(numbers))
 
num_range = range(5, 11, 5)
print(num_range)
for number in num_range:
    print(number)


def list_name(name, age):
    print(f"Happy birthdat to {name}")
    print(f"You are {age} years old!")
    print("HAppy birthday to you.")
list_name("Kim", 21)
list_name("john", 32)
list_name("Henry", 54)
list_name("Jack", 50)

def pay_bill(username, bill, date):
    print(f"Hello {username}")
    print(f"The duedate for pying your loan of kshs: {bill} is {date}")
pay_bill("Wycliff", 10000, "12th of May")

def create_name(firstName, lastName):
    firstName = firstName.capitalize()
    lastName = lastName.capitalize()
    return firstName + " " + lastName
fullName = create_name("wycliff", "kimani")
print(fullName)

names = input("Enter your name : ")
while names == "":
    print("You did not ente ryour name : ")
    names = input("ENter your  name : ")
else:
    print(f"Hello {names}")
age = int(input("Enter your age : "))
while age <= 0:
    print("Age cannot be negative!")
    age = int(input("Enter your age : "))
print(f"You are {age} years old")

food = input("Enter a food you like(press q to quit) : ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like(press q to quit) : ")
print("goodbye")

numb = int(input("Enter a number between 1 and 10 : "))
while numb < 1 or numb > 10:
    print(f"{numb} is invalid!")
    numb = int(input("Enter a number between 1 and 10 : "))
print(f"The number you entered is {numb}")