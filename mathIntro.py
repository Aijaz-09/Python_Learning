# exponent operator: **
# Functions:
#     round(a)|round(a,2), abs(b), pow(a,b), min(a,b,..), max(a,b,..)
# import math:
#     math.pi, math.e, math.sqrt(a), math.ceil(x), math.floor(x)
import math

choice = int(input("Enter 1 for circle, 2 for right Triangle Hypotenuse: "))

if choice == 1:
    radius = float(input("Enter radius of the circle: "))
    circumference = 2 * math.pi * radius
    print(f"The circumference is {round(circumference, 2)}cm")
    area = math.pi * pow(radius, 2)
    print(f"The area is {round(area, 2)}cm^2")
else:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    hypotenuse = math.sqrt(pow(base, 2) + pow(height, 2))

    print(f"The hypotenuse is {round(hypotenuse, 2)}cm")