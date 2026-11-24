# Sean Gabriel Velasco
# 8-Adelfa

food = []

for i in range(1, 6):
    food_order = input(f"Enter order {i}: ")
    food.append(food_order)

print("Original orders:")
print(food)

more_food = input("Enter additional order: ")
food.append(more_food)
print("Updated orders:")
print(food)

priority_food = input("Enter priority order: ")
food.insert(0, priority_food)
print("Updated orders:")
print(food)

search = input("Search for an order: ")
if search in food:
    print(f"Number of occurrences: {food.count(search)}")
    print(f"First index: {food.index(search)}")
else:
    print("Order not found.")

cancel = input("Enter order to cancel: ")
if cancel in food:
    food.remove(cancel)
print("Updated orders:")
print(food)

last_order = food.pop()
print(f"Last order removed: {last_order}")

food.sort()

print("== FINAL ORDER REPORT =====")
print(f"Orders: {food}")
print(f"Remaining Orders total: {len(food)}")
