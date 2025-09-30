'''# Explaining logic and program
num1 = int(input("Enter first number: ")) # Taking first number input from the user
num2 = int(input("Enter second number: ")) # Taking second number input from the user
print(f"{num1} == {num2} : {num1} == {num2}")
# Using the concept of dictionary of key and value, this is showing both key and information has the same input with no logical output
# This is showing if key and values are the same
print(f"{num1} != {num2} : {num1 != num2}")
# Using dictionary concept, we have ot key and values, operation shows whether input number with conditional operators are true or not
# This check  check if first number is equal to the second number
print(f"{num1} > {num2} : {num1 > num2}")
# Same as above, check conditions and returns either True or False
# This check if first number inputed is greater than the second number
print(f"{num1} < {num2} : {num1 < num2}")
# Same Explanation is applicable to this.
# This check if first number inserted is less than second number returning True or False

# Three Scenarios where we can use the above are
# 1. Checking age between two people
# 2. Checking Height or weight between two people
# 3. Checking Grades or Score between two people

# Checking the weight of Two brothers
'''
first_brother_weight = int(input("Enter First brother height in Kg: "))
second_brother_weight = int(input("Enter Second brother weight in Kg: "))

if first_brother_weight > second_brother_weight:
    print(f"First brother weigh {first_brother_weight - second_brother_weight} more")
elif first_brother_weight < second_brother_weight:
    print(f"Second brother weigh {second_brother_weight - first_brother_weight} than first brother")
else:
    print("They have the same weight")