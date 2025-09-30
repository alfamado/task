# Unique member registration
name_enter = input("Enter three names: ").split(",")
check_uniqueness = set(name_enter)
result = {name_enter: len(name_enter) for name_enter in check_uniqueness}
print(result)