# 2. Shopping list manager
shopping_list = []
item1 = input("Enter your first shopping item: ")
item2 = input("Enter your second shopping item: ")
item3 = input("Enter your third shopping item: ")
shopping_list.append(item1)
shopping_list.append(item2)
shopping_list.append(item3)
print(",".join(shopping_list))