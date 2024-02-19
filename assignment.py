# Temperature conversion program
print("REMINDER : MAKE SURE YOUR UNITS ARE IN CAPITAL LETTERS")
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

if unit == 'C':
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}°C is {converted_temperature} in Fahrenheit")
elif unit == 'F':
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}°F is {converted_temperature} in Celsius")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")

# checking if a number is even or a odd number
number = int(input("Enter a number : "))
if number % 2 == 0:
    print("The number you entered is an even number")
else:
    print("The number you entered is an odd number")