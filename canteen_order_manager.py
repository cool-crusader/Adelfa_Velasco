# Sean Gabriel Velasco
# 8-Adelfa

food = []

for i in range(1,6):
    foods = int(input(f"Input quiz {i} grades: "))
    food.append(foods)

print(food)



more_food = str(input("Enter additional orders: "))
food.append(more_food)

search = str(input("Search for an order: "))
print(f"")