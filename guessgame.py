entry = 5
user_entry = int(input("Enter a number : "))
max_entries = 3
number_of_entries = 0
while user_entry != 5 and number_of_entries < max_entries:
        print("Incorrect entry. Try again!")
        user_entry = int(input("Enter a number : "))
        number_of_entries += 1

if user_entry == 5:
    print("You WOn!!!!")
else:
    print(f"You ran out of guesses. You lose. The correct number is {entry}" )