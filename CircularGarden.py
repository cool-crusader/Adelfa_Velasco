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

README.md
# Project Title: Circular Garden Calculator

## Description: Everything About the Program
This program calculates the Area, Circumference, the Square Root, the Area rounded up and down of a Circular Garden depending on the radius you enter.

## How to run the program
Input your Radius Measurement

## Input needed
The only Input you need is the radius of the circle

## Output Examples
Please enter your radius: 5
The Area of the Circular Garden is: , 78.54 square meters
The Circumference of the Circular Garden is: 31.42 meters
The Square of the Circular Garden is: 8.86
The rounded Up Area is: 79.00 square meters
The rounded Down Area is: 78.00 square meters

## Author:
Name: Sean Gabriel E. Velasco
Grade and Section: 8-Adelfa

# Computational Thinking
## 1. Problem Identification
We need a program that gets the radius of a circular garden and calculates its area, circumference, square root of the area, and the area rounded down and up.
## 2. Problem Decomposition
Ask for the radius
Compute area
Compute circumference
Compute square root of area
Round area down and up
Show the results
## 3. Pattern Recognition
This is a basic circle problem. We can use the math library (math.pi, math.pow, math.sqrt, math.floor, math.ceil) instead of writing the formulas ourselves.
## 4. Data Representation
Input: radius (float)
Outputs: area, circumference, square root, floor, ceil
## 5. Algorithm Development
import math

Ask user for radius
area = π × radius²
circumference = 2 × π × radius
squareRoot = √area
roundedDown = floor(area)
roundedUp = ceil(area)

Display all results
