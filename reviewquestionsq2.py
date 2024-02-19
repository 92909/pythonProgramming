def add_product(name, price, quantity):
    print(f"Name : {name}, Price : {price}, Quantity :  {quantity}")
def update_price(product, new_price):
    add_product.price = new_price
    print(product, new_price)
    print(f"The new price is : {new_price} dollars")
def update_quantity(product, new_quantity):
    add_product.quantity = new_quantity
    print(product, new_quantity)
    print(f"The new quantity is {new_quantity}")
add_product("Laptops", 100000, 10)
update_price("Laptops", 50)
update_quantity("Desktops", 200)
