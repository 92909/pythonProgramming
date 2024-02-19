class bankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    
    def deposit(self, amount_available):
        self.balance = self.balance + amount_available
        print(amount_available)
        print(self.balance)
        
    def withdraw(self, amount_to_withdraw):
        if amount_to_withdraw > self.balance:
            print("You do not have enough alance in your account!")
        else:
            self.balance = self.balance - amount_to_withdraw
        print(f"The amount withdrawn is : kshs {amount_to_withdraw} ")
        print(f"The remaining balance in the account is kshs {self.balance}")
    def check_balance(self):
        print(f"The remaining balance in te account is {self.balance}")
        
    def customer_details(self):
        print(f"Your name is {self.customer_name}")
        print(f"Your account number is {self.account_number}")
        print(f"You openned the account on {self.date_of_opening}")
    def depositing(self, amount_to_deposit):
        print(f"The amount deposited is {amount_to_deposit} making the total balance to be {(self.balance + amount_to_deposit)}")
b = bankAccount(11089, 200000, "2020-12-12", "Wycliff Kimani")
b.deposit(50000)
b.withdraw(amount_to_withdraw = int(input("Enter the amount you need to withdraw : ")))
b.check_balance()
b.customer_details()
b.depositing(amount_to_deposit = int(input("ENter the amount you wish to deposit : ")))