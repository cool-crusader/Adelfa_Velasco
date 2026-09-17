# Sean Gabriel Velasco
# 8 - Adelfa


pin = input("Create a 6-digit PIN: ")

# Check both length (must be 6) and content (digits ONLY)
if len(pin) == 6 and pin.isdigit():
    print("Valid PIN.")
else:
    print("Invalid PIN. Enter exactly 6 digits.")