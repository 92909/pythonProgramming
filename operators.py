#divisibility def test. checking an even number
num1 = int(input("Enter a number : "))
if num1 % 2 == 0:
    print("The number is divisible by 2 ")
else:
    print("The number is indivisible")

#program to calculate and output the discount given
price = float(input("ENter the price of the item : "))
if price > 10000:
    discount = (5 / 100) * price
    print(f"The discount given is : {discount}")
else:
    print("No discount given")
    