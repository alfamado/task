# Attendance Tracker1
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
months = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

name = input("Enter Student's name: ")
gender = input("What is your Gender: ")
course_track = input("What is your Course Track: ")
month = int(input("Current month number (1-12): "))
day = int(input("current day number(1-7): "))
print(f"{name}")
print(f"{gender}")
print(f"{course_track}")
print(days[day - 1])
print(months[month - 1])