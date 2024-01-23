
radius = int(input("Enter nthe radius of the circle = "))
base = int(input("Enter the base of the triangle = "))
height = int(input("Enter the height of the triangle = "))
area_of_a_circle = 3.142 * radius ** 2
area_of_a_triangle = 0.5 * (base * height)
area_of_a_cylinder = 3.142 * (radius  ** 2 ) * height
print(f"The area of the circle is {area_of_a_circle}")
print(f"The area of the triangle is {area_of_a_triangle}")
print(f"The area of the cylinder is {area_of_a_cylinder}")
sum_of_total = area_of_a_circle + area_of_a_triangle + area_of_a_cylinder
print(f"The sum of the area of the figures above is : {sum_of_total}")
'''
pals = ["John", "wycliff", "kimani", "johnson", "patrick"]
cars = [120, 300, 900, 876, 787]
payments = [12000, 13000, 32000, 21222, 645444, 70000]
print(pals[1:-2])
pals.sort()
print(pals)
pals.sort(reverse = True)
print(pals)
pals.reverse()
print(pals)
print(cars)
print(max(cars))
print(sum(cars))
pals.append("kimutai")
print(pals)
pals.insert(1, "Douglas")
cars.insert(1, "156")
print(pals)
print(cars)
pals[3] = "Livingstone"
print(pals)
"""pals.extend(payments)
print(pals)"""
pals.remove("Douglas")
print(pals)
pals.pop(-3)
print(pals)
del pals[3]
del pals[1]
del pals[2]
print(pals)
pal = list(pals)
print(pal)
pals.reverse()
print(pals)
'''