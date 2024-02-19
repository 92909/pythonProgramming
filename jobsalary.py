
jobs = ["Receptionist - ", "Accountant - ", "Sales manager - ", "Cleaner - ", "Messager - ", "Chief Executive officer - "]
salaries = [21000, 31000, 100000, 54000, 7000, 60000, 5000000]
interested_job = input("Enter the job you are interested in : ")
for job in jobs:
    print(job)
for salary in salaries:
    print(salary)
    
    
if interested_job.capitalize() == "Receiptionist":
    print(f"The salary for {interested_job} is 21000")
elif interested_job.capitalize() == "Accountant":
    print(f"The salary for {interested_job} is 31000")
elif interested_job.capitalize() == "Sales manager":
    print(f"The salary for {interested_job} is 54000")
elif interested_job.capitalize() == "Cleaner":
    print(f"The salary for {interested_job} is 7000")
elif interested_job.capitalize() == "Messager":
    print(f"The salary for {interested_job} is 60000")
elif interested_job.capitalize() == "Chief executive officer":
    print(f"The salary for {interested_job} is 5000000")
else:
    print(f"{interested_job} is not available. Please consider these jobs ")
    print(jobs)