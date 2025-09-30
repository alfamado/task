# 5. Modifying tuple indirectly
shopping_tuple = (
                    input("Enter first shopping item: "),
                    input("Enter second shopping item: "),
                    input("Enter third shopping item: ")   
)
shopping_list = list(shopping_tuple)

add_item = [
                input("Enter fourth shopping item: "),
                input("Enter fifth shopping item: ")
]

total_item = shopping_list + add_item
print(total_item)
total_item_in_tuple = tuple(total_item)
print("|".join(total_item_in_tuple))