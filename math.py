answer = str(input("Please enter the shape of your diagram : "))
if answer == "triangle":
    base = int(input("enter the base of the triangle : "))
    height = int(input("enter the height : "))
    print(0.5 * base * height)
elif answer == "square":
    measurement = int(input("Enter the base od the square : "))
    print(measurement ** 2)
elif answer == "rectangle":
    length = int(input("Enter the length of the rectangle : "))
    width = int(input("Enter the width of the rectangle : "))
    print(length * width)
elif answer == "circle":
    radiuss = int(input("Enter the radius of the circle : "))
    print(3.142 * radiuss ** 2)
elif answer == "trapezium":
    a = int(input("Enter the a of the trapezium : "))
    b = int(input("enter the b of the trapezium : "))
    height_of = int(input("Enter the height of the trapezium : "))
    print(0.5 * (a + b) * height_of)
else:
    print("Please re-enter the shape of your diagram!")