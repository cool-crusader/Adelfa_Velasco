# Sean Gabriel Velasco
# 8-Adelfa

total_sales = 0
above_target = 0
below_target = 0
num_item = int(input("Enter the amount of food items you will buy: "))

for i in range(num_item):
    sales = int(input("Enter the total sales: "))
    total_sales += sales
    if sales >= 500:
        above_target += 1
    else:
        below_target += 1

def calculate_average(total_sales, num_item):
    average_sales = total_sales / num_item
    return average_sales

def sales_report(average_sales, above_target, below_target):
    print("CANTEEN SALES REPORT")
    print(f"Average sales: PHP {average_sales:.2f} | Meeting Target: {above_target:.2f} | Below Target: {below_target:2f}")

average_sales = calculate_average(total_sales, num_item)
sales_report(average_sales, above_target, below_target)