# Sean Gabriel Velasco
# 8 - Adelfa


try:
    # Data Type Validation
    score = float(input("Enter examination score: "))

    # Range Validation
    if 0 <= score <= 100:
        print("Valid score.")
    else:
        print("Invalid score.")

except ValueError:
    print("Invalid input. Please enter a number.")