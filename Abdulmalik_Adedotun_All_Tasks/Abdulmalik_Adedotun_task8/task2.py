# Federal Government Eligibility Requirement For Citizens
citizen_name = input("Enter your name: ").title()
citizen_age = int(input("Enter your age: "))
citizen_score = int(input("Enter your test score: "))
citizenship = input("Are you a citizen of Nigeria (Yes/No): ").lower()
enrollment_status = input("Are you a full-time undergraduate student in a recognised university (Yes/No): ").lower()
other_scholarship = input("Are you a beneficiary of any other scholarship from oil and gas industry both local and foreign (Yes/No): ").lower()

waec_subject = input("Enter WAEC subjects (including Math and English, space separated): ").upper().split(",")
waec_subject_grade = input("Enter WAEC grades (space separated): ").upper().split(",")
waec_wassce_result = dict(zip(waec_subject, waec_subject_grade))
print(f"WAEC Result: {waec_wassce_result}")

basic_check = (citizenship == "yes") and (enrollment_status == "yes") and (other_scholarship == "no")

waec_check = set(waec_subject_grade).issubset({"A", "B"})


eligibility_criteria = basic_check and waec_check and (citizen_age < 18) and (citizen_score > 70)

messages = {
    True: f"Candidate: {citizen_name}\nAge: {citizen_age}\nScore: {citizen_score}\nEligible: True",
    False: f"Candidate: {citizen_name}\nNot Eligible for Scholarship"
}
print(messages[eligibility_criteria])