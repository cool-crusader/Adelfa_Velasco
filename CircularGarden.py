# Sean Gabriel Velasco
# 8-Adelfa
# LT 1: Circular Garden

# Imports the Math Library in the code
import math

# Get the Radius measurement
radius = float(input("Please enter your radius: "))


# Calculation of Area, Circumference, Square root, Area rounded up and down
area = math.pi * math.pow (radius, 2)
circumference = 2 * math.pi * radius
squareRoot = math.sqrt(area)
roundedUp = math.ceil(area)
roundedDown = math.floor(area)

# Display the final calculation
print(f"The Area of the Circular Garden is: , {area:.2f} square meters")
print(f"The Circumference of the Circular Garden is: {circumference:.2f} meters")
print(f"The Square of the Circular Garden is: {squareRoot:.2f}")
print(f"The rounded Up Area is: {roundedUp:.2f} square meters")
print(f"The rounded Down Area is: {roundedDown:.2f} square meters")