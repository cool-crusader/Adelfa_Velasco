# Calculating Distance Between Two Points Using Math and I/O Libraries (Improved)
# Sean Gabriel Velasco
# Date: 9/24/26

# Imports the Math library to the program for me to use
import math

# Gets the x and y values from the user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Formula
distance = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

# Output
print(f"The distance between 2 points is: {distance:.2f}")



# Reflection
# Using a library is more practical than writing all calculations from scratch,
# because the math library already has the functions ready-made like pow().
# In this activity, it saved me from having to invent my own square root code,
# so the program is shorter, clearer and less likely to have mathematical errors.