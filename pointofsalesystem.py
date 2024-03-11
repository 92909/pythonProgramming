#creating a point of sale system

class sale_item:
    def __init__(self, item_id, name, unit_price):
        self.item_id = item_id
        self.name = name
        self.unit_price = unit_price
    
    def calculate_total(self):
        calculate_totals = self.item_quantity * self.unit_price
        print(f"Total cost kshs : {calculate_totals}")
    
class standard_item(sale_item):
    def __init__(self, item_id, name, unit_price, item_quantity):
        super().__init__(item_id, name, unit_price)
        self.item_quantity = item_quantity
        
    def calculate_total(self):
        return super().calculate_total()

class discounted_items(standard_item):
        def __init__(self, item_id, name, unit_price, item_quantity, discount_percentage):
             super().__init__(item_id, name, unit_price, item_quantity)
             self.discount_percentage = discount_percentage
            
            
        def calculate_total(self):
             totals = self.item_quantity * self.unit_price
             discount = (self.discount_percentage/100) * totals
             calculate_totals = totals - discount
             print(f"The total cost id kshs: {totals}")
             print(f"The discount given is kshs : {discount}")
             print(f"The total is kshs : {calculate_totals}")

class service_item(sale_item):
    def __init__(self, item_id, name, unit_price, hourly_rate, hours_service):
         super().__init__(item_id, name, unit_price)
         self.hourly_rate = hourly_rate
         self.hours_service = hours_service
        
    def calculate_total(self):
        total_cost_service = self.hourly_rate * self.hours_service
        print(f"Total cost of servive kshs : {total_cost_service}")



standard = standard_item(2100, input("Enter item name : "), int(input("Enter item price : ")), int(input("Enter the quantity of the items : ")))
standard.calculate_total()
discounts = discounted_items(2100, input("Enter item name : "), int(input("Enter item price : ")), int(input("Enter the quantity of the items : ")), int(input("Enter the discount percentsge rate : ")))
discounts.calculate_total()

service = service_item(2100, input("Enter item name : "), int(input("Enter item price : ")), int(input("Enter the hourly rate : ")), int(input("Enter the hours of service : ")))
service.calculate_total()