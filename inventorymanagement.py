#creating an inventory management system
from datetime import datetime

class product:
    def __init__(self, product_id, name, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock
        
    def calculate_value():
        total_value = total_value
class simple_product(product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price
    def der_product(self):
        print(self.name)
        print(self.unit_price)
    def calculate_value(self):
        total_value = self.quantity_in_stock * self.unit_price
        print(f"Total Value of stock : {total_value}")
    
class perishable_product(simple_product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock, unit_price)
        self.expiry_date = expiry_date
        
        
        
    def calculate_value(self):
        expiry_date2 = datetime.strptime(self.expiry_date, "%Y-%m-%d")
        shelf_life = expiry_date2 - datetime.now()
        print(f"Shelf life : {shelf_life}")
        total_value = self.quantity_in_stock * self.unit_price
        discount  = total_value * (20/100)
        print(f"Discount : {discount}")
        total_value1 = total_value - discount
        print(f"Total Value : {total_value1}")
        
class digital_products(product):
    def __init__(self, product_id, name, quantity_in_stock, current_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.current_price = current_price
    
    def calculate_value(self):
        total_value = self.current_price * self.quantity_in_stock
        print(f"Total value of digital products : {total_value}")
    
derproduct = simple_product("123456", "Laptops", int(input("Enter the number of laptops in store : ")), int(input("Enter price per unit : ")))
derproduct.der_product()
derproduct.calculate_value()
perishable = perishable_product("123456", "Laptops", int(input("Enter the number of laptops in store : ")), int(input("Enter price per unit : ")), "2024-12-12")
perishable.calculate_value()
digital = digital_products("123456", "Desktops", int(input("Enter the number of Desktops in store : ")), int(input("Enter the current price : ")))
digital.calculate_value()