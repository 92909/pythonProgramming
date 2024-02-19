principal = int(input("Enter the principle : "))
while principal <= 0:
    print("Your principal cannot be zero or a negative!")
    principal = int(input("Enter the principle : "))
rate = int(input("Enter the rate : "))
while rate <= 0:
    print("Your interest rate cannot be zero or a negative!")
    principal = int(input("Enter the interest rate in %: "))
time = int(input("Enter the time : "))
while time <= 0:
    print("Your time cannot be zero or a negative!")
    principal = int(input("Enter the time in years : "))
    
interest_accrued = principal * (rate / 100) * time
total_interest = principal + interest_accrued
print(f"The principal is kshs {principal}")
print(f"The rate of interest is {rate} %")
print(f"The time taken is {time} years ")
print(f"The interest accrued over the years is kshs. {interest_accrued}")
print(f"The total money in the bank is kshs. {total_interest}")