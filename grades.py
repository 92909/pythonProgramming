
age = int(input("Enter your age : "))
income = int(input("Enter your income : "))
if age >= 21 and income > 21000 :
    print("You are eligible for a loan")
else:
    print("You cannot be granted a loan")


#eligibility to vote
age_to_vote = int(input("Enter your age : "))
country = str(input("Enter your nationality : "))
if age_to_vote >= 18 and country == "Kenyan" or "ugandan" or "tanzanian":
    print("You are eligible to vote!")
else:
    print("you are not eligible to vote")
# program to chech the grade of a student
grade = float(input("Enter your marks : "))
if grade > 70 < 100:
    print("You scored an A")
elif grade > 60 < 69:
    print("You scored a B")
elif grade > 50 < 59:
    print("You scored a C")
elif grade > 40 < 49:
    print("You scored a D")
elif grade > 0 < 39:
    print("You scored a E! Register for the supplementary exams as soon as possible!")
else:
    print("Please enter your marks again ")
