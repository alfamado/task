# Student Profile Builder Information
student_name = input("Enter student's full name: ")
student_age = int(input("Enter student's age: "))
student_gender = input("Enter gender (Male/Female): ")

subjects_studied = ("Math", "English", "Accounting")
scores = tuple(float(input(f"Enter score for {subject}: ")) for subject in subjects_studied)

guardian_name = input("Enter guardian's name: ")
guardian_phone = input("Enter guardian's phone number: ")

enter_hobbies = input("Enter at least 3 hobbies (separated by commas): ")
hobbies_uniqueness = set(hu.strip() for hu in enter_hobbies.split(","))

student_details = {
    "Student_Info": {
        "Name": student_name.title(),
        "Age": student_age,
        "Gender": student_gender.capitalize()
    },
    "Academics": {subject: score for subject, score in zip(subjects_studied, scores)},
    "Guardian_Info": {
        "Name": guardian_name.title(),
        "Phone": guardian_phone
    },
    "Hobbies": list(hobbies_uniqueness)
}

# Derived Data
student_details["Academics"]["Average"] = sum(scores) / len(scores)
student_details["Student_Info"]["Initials"] = "".join([name[0] for name in student_name.split()])
student_details["Hobbies Count"] = len(hobbies_uniqueness)

# Output Section
print("\n\t=== STUDENT DETAILS ===")
print(f"Name:\t\t{student_details['Student_Info']['Name']}")
print(f"Age:\t\t{student_details['Student_Info']['Age']}")
print(f"Gender:\t\t{student_details['Student_Info']['Gender']}")
print(f"Initials:\t{student_details['Student_Info']['Initials']}")
print("\n--- Academic Grade ---")
print(student_details["Academics"])
print("\n--- Guardian Info ---")
print(student_details["Guardian_Info"])
print("\n--- Hobbies ---")
print(student_details["Hobbies"])
print(f"\nTotal Hobbies:\t{student_details['Hobbies Count']}")
print(f"Average Score:\t{student_details['Academics']['Average']:.2f}")