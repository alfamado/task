# Student Record
student = {}
student_name = input("Enter your name: ").title()
student["Name"] = student_name
student_age = int(input("Enter your age: "))
student["Age"] = student_age
student["score"] = [70, 89, 90]
average_score = sum(student["score"]) / len(student["score"])
student_passed = average_score >= 50
teenager = student_age >= 13 and student_age <= 19
print(f"Student Record:\nName : {student_name}\nAge : {student_age}\nScore : {student["score"]}\nPassed : {student_passed}\nTeenager : {teenager}")