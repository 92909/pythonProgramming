'''age = int(input("Please enter your age : "))
name = str(input("Please enter your name : "))
name = name.title()
if age >= 18:
    print(f"Hello {name} 👊✋. Your are eligible to vote! 👍")
else:
    print(f"Hello {name} 👊✋. YOU ARE STILL UNDERAGE. GO BACK HOME!!!! 😂😂😂")

price_range = int(input("Please enter the range price : "))
list1 = ["Eggs," "Milk," "Bread," "Butter," "Cheese," "Yogurt," "Fresh fruits"]
list2 = ["Sugar," "Flour," "Coffee," "Tea," "Jam or jelly," "Peanut butter," "Cereal," "Oats," "Nuts"]
list3 = [ "Honey," "Snack items (e.g., chips, crackers)," "Frozen vegetables."]
if price_range > 10000:
    print(list1)
elif price_range > 1000 < 9999:
    print(list3)
else:
    print(list2)

print(" ".join(list1) )'''

number = int(input("Enter the number : "))
print(f"the value input is {number}")
