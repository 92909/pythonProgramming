#program to calculate the electricity bill for a customer
customerId = input("Enter your ID : ")
customerName = input("Enter your name : ")
unitsConsumed = float(input("Enter the number of units consumed : "))
if unitsConsumed < 199:
    charges_per_unit = 1.20
elif 200 < unitsConsumed < 400:
    charges_per_unit = 1.50
elif 400 < unitsConsumed < 600:
    charges_per_unit = 1.80
elif unitsConsumed > 600:
    charges_per_unit = 2.00
else:
    print("Please enter the units consumed again. ")
total_bill = unitsConsumed * charges_per_unit
if total_bill > 400:
    subcharge = total_bill * 0.15
else:
    subcharge = 0
    total_bill = total_bill
total = total_bill + subcharge
if total_bill <= 100:
    total_bill = 100

print(customerId)
print(customerName)
print(unitsConsumed)
print(subcharge)
print(total_bill)
print(total)