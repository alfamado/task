user_names = input("List the five names: ")
five_names = user_names.lower().split(" ")
five_names.sort()
print(five_names)
[print(f"{i}") for i in five_names]