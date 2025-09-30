# Student score tracker
students_name = []
students_score = []
student_name = input("Enter the three student name(seperated by a comma): ").split(",")
students_name.append(student_name)
student_score = input("Enter the student scores(sererated by a comma): ").split(",")
students_score.append(student_score)

print("--------Student Name and Score--------")
print("student_name\t\t\tstudent_score")
print(f"{students_name}\t\t{students_score}")