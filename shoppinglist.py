fruits = []
prices = []
total = 0
while True:
    fruit = input("ENter the food to buy. (press q to quit) : ")
    if fruit.lower() == "q":
        break
    else:
        price = int(input(f"Enter the price of the {fruit} : "))
        fruits.append(fruit)
        prices.append(price)
print("YOUR SHOPPING CART LIST IS : ")
for fruit in fruits:
    print(fruit, price)
total = total + sum(prices)
print(f"The total amount you spent on fruit shopping is kshs. {total} " )
print(f"The total amount spent on {fruits} is kshs {total}")