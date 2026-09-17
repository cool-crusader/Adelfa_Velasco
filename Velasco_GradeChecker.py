# Sean Gabriel Velasco
# 8 - Adelfa

# Asks the user for a grade input and convert it to an integer
grade = int(input("Enter your grade: "))

# Check if the grade falls within the valid range of 0 to 100
if 0 <= grade <= 100:
    print("Valid grade:", grade)
else:
    print("Invalid grade, Grade must be between 0 and 100")