# Store Inventory
store = {"Book": 10, "Pen": 20, "Bag": 5}
print(f"Before Purchase: {store}")
item_to_buy = input("What do you want to buy: ").title()
item_quantity = int(input("How many do you want: "))
store[item_to_buy] -= item_quantity
print(f"After Purchase: {store}")