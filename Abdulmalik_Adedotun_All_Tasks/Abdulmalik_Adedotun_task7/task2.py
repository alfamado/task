# Supermarket Price List
store_item = ["Rice", "Beans", "Garri", "Milk", "Milo"]
store_price = (input("Enter price: ").split(", "))
store_item_prices = dict(zip(store_item, store_price))
print(store_item_prices)
# store_item_prices.update({store_item[input("Enter the item to update price: ")]})
item = input("Enter the item to update price: ")
if item in store_item_prices:
    new_value = input(f"Enter the item you want to update {store_item_prices[item]:}: ")
    store_item_prices[item] = new_value
    print(store_item_prices)