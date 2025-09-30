# 6. Nepa customer details and bills
customer_full_name = input("What is your name ")
units_consumed = int(input("How much unit did you consumed in KWh "))
cost_per_unit = float(input("Cost per unit is "))
total_bill = units_consumed * cost_per_unit
print(f"Customer {customer_full_name}\nused {units_consumed} unit\nand the cost of each unit in KWh is {cost_per_unit}/n Total = {total_bill}")
