# Federal Government Eligibility Requirement For Citizens
citizen_name = input("Enter your name: ").title()
citizen_age = int(input("Enter your age: "))
citizen_score = int(input("Enter your test score: "))
citizenship = input("Are you a citizen of Nigeria (Yes/No): ").lower()
Enrollment_status = input("Are you a full-time undegraduate student in a recognised university (Yes/No): ").lower()
other_scholarship = input("are you a beneficiary of any other scholarship from oil and gas industry both local and foreign (Yes/No): ").lower()
if (citizenship == "yes") and (Enrollment_status == "yes") and (other_scholarship == "no"):
    print("He is a citizen, enrolled full-time in recognised Nigeria University and isn't a beneficiary of any oil ang gas scholarship, checking age and score, WAEC?WASSCE grades for eligibility of scholarship")
    # waec_wassce_result = input(f"Enter waec results grades in 5 key subject including math and english, must be (A/B): ").split(", ")
    waec_subject = input("Enter waec key waec/wassce subject including math and english: ").split()
    waec_subject_grade = input("Enter waec grades").split()
    waec_wassce_result = dict(zip(waec_subject, waec_subject_grade))
    print(waec_wassce_result)
    if waec_subject_grade == "A" or "B":
        eligibility_criteria = (citizen_age < 18) and (citizen_score > 70)
        print(f"Candidate: {citizen_name}\nAge: {citizen_age}\nScore: {citizen_score}\nEligible: {eligibility_criteria}")