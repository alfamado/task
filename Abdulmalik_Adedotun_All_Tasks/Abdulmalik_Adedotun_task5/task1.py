# 1. Create and display
dish = []
for i in range(3):
    favourite_dish = input(f"Enter your three favourite Nigeria food {i+1}: ")
    dish.append(favourite_dish)
dishes = tuple(dish)
print(dishes)
print("\n".join(dishes))