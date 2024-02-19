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