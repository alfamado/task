# 10. School fees details
school_name = input("What is the name of your school ")
tuition_fee = float(input("Tuition fee is "))
hostel_fee = float(input("Hostel fee is "))
feeding_fee = float(input("Feeding fee is "))
Total_fee = tuition_fee + hostel_fee + feeding_fee
print(f"{school_name}")
print(f"{tuition_fee} = ")
print(f"{hostel_fee} = ")
print(f"{feeding_fee} = ")
print(f"Total amount to be paid is {Total_fee}")
