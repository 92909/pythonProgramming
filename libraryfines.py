# Program to calculate the fine to be charged
from datetime import datetime
bookId = input("Enter the Book ID : ")
dueDate = input("Enter the due date (YYYY-MM-DD): ")
returnDate = input("Enter the return date (YYYY-MM-DD): ")
date = datetime.strptime(dueDate, "%Y-%m-%d")
date1 = datetime.strptime(returnDate, "%Y-%m-%d")
daysOverdue = date1 - date
daysOverdue1 = daysOverdue.days
if daysOverdue1 < 7:
    fine_rate = 20
elif 7 < daysOverdue1 < 14:
    fine_rate = 50
else:
    fine_rate = 100
total_amount = daysOverdue1 * fine_rate
print("Date entered:", date)
print("Date entered:", date1)
print(daysOverdue1)
print(fine_rate)
print(total_amount)
