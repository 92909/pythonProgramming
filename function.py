# a prograam to subtract dates
from datetime import datetime
date1 = input("Enter the date : ")
date2 = input("Enter the 2nd date : ")
savings_per_day = int(input(("Enter your days savings in kshs: ")))
date3 = datetime.strptime(date1, "%Y-%m-%d")
date4 = datetime.strptime(date2, "%Y-%m-%d")
date_total = date4 - date3
date_total = date_total.days
total_savings = date_total * savings_per_day
print(date_total)
print(total_savings)

#program to create a guessing game
right_guess = "Mountain"
user_guess = input("Guess  a name : ")
possible_guesses = 3
number_of_guesses = 0
out_of_guesses = False

while user_guess.capitalize() != "Mountain" and number_of_guesses < 3:
    print("OOPS! Try again!")
    user_guess = input("Guess  a name : ")
    number_of_guesses = number_of_guesses + 1

if user_guess.capitalize() == "Mountain":
    print("YOU WON")
else:
    print("You ran out of guesses. YOU LOSE")