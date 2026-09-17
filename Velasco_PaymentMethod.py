# Sean Gabriel E. Velasco
# 8 - Adelfa

# Input: Where we will know what the customer will use
payment_method = input("Enter payment method: ")

# List the allowed payment methods
allowed_methods = ["Cash", "GCash", "Card"]

# Check if the input is valid
if payment_method in allowed_methods:
    print("Valid payment method.")
else:
    print("Invalid payment method.")