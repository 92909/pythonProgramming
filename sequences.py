from datetime import datetime

# Prompting user for book details
book_id = input("Enter Book ID: ")
due_date_str = input("Enter Due Date (YYYY-MM-DD): ")
return_date_str = input("Enter Return Date (YYYY-MM-DD): ")

# Converting string dates to datetime objects
due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
return_date = datetime.strptime(return_date_str, "%Y-%m-%d")

# Calculating days overdue
days_overdue = (return_date - due_date).days

# Determining fine rate based on days overdue
if days_overdue <= 7:
    fine_rate = 20
elif days_overdue <= 14:
    fine_rate = 50
else:
    fine_rate = 100

# Calculating fine amount
fine_amount = fine_rate * days_overdue

# Displaying book details and fine information
print("\nLibrary Fine Details")
print("Book ID:", book_id)
print("Due Date:", due_date_str)
print("Return Date:", return_date_str)
print("Days Overdue:", days_overdue)
print("Fine Rate (Kshs per day):", fine_rate)
print("Fine Amount (Kshs):", fine_amount)
