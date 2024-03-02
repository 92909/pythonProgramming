import math
#creating na simple payroll program
class employee:
    def __init__(self, employee_id, employee_name, weekly_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.weekly_salary = weekly_salary
    def calculate_payroll(self):
        print(f"Name :  {self.employee_name}")
        print(f"ID number : {self.employee_id}")
        print(f"Salary : {self.weekly_salary} ")
class salary_employee(employee):
    def salary_emp(self):
        print(f"Name :  {self.employee_name}")
        print(f"ID number : {self.employee_id}")
        print(f"Weekly Salary : {self.weekly_salary} ")
        
class hourly_employee(employee):
    def __init__(self, employee_id, employee_name, weekly_salary, houly_rate, hours_worked):
        super().__init__(employee_id, employee_name, weekly_salary)
        self.hourly_rate = houly_rate
        self.hours_worked = hours_worked
        
    def hourly_salary(self):
        total_salary = self.hours_worked * self.hourly_rate
        print(f"Hourly employee salary : {total_salary}")
    
    
class commission_employee(salary_employee):
    def __init__(self, employee_id, employee_name,employee_sales, salary_received, weekly_salary):
        super().__init__(employee_id, employee_name, weekly_salary)
        self.employee_sales = employee_sales
        self.salary_received = salary_received
    def commission_received(self):
        commission = (10/100) * int(self.employee_sales)
        print(f"Commission earned : {commission}")
        total_earnings = self.salary_received + commission
        print(f"Total earnings : {total_earnings}")
        

employee = employee("9092", "Kim", input("Enter the weekly salary : "))
employee.calculate_payroll()
employer = salary_employee("1234", "Kim", input("Enter the salary : "))
employer.salary_emp()
employ = hourly_employee("9290", "Wycliff Kimani", input("Enter the salary paid : "), int(input("Hourly rate : ")), int(input("Hours Worked : ")))
employ.hourly_salary()
commission = commission_employee("1090", "Kim Jackson", input("Sales made : "), int(input("Monthly salary : ")), input("Weekly salary : "))
commission.commission_received()
