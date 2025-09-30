# Citizenship scholarship eligibility with control and error handling
try:
    citizen_name = input("Enter your name: ").title()

    try:
        citizen_age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        citizen_age = 0

    try:
        citizen_score = int(input("Enter your test score: "))
    except ValueError:
        print("Invalid score. Please enter a number.")
        citizen_score = 0

    citizenship = input("Are you a citizen of Nigeria (Yes/No): ").lower()
    enrollment_status = input("Are you a full-time undegraduate student in a recognised university (Yes/No): ").lower()
    other_scholarship = input("Are you a beneficiary of any other scholarship from oil and gas industry both local and foreign (Yes/No): ").lower()

    if (citizenship == "yes") and (enrollment_status == "yes") and (other_scholarship == "no"):
        print("Candidate meets basic criteria. Checking WAEC/WASSCE grades...")

        waec_subject = input("Enter WAEC key subjects including Math and English (separated by space): ").upper().split()
        waec_subject_grade = input("Enter WAEC grades for those subjects (separated by space): ").upper().split()
        waec_wassce_result = dict(zip(waec_subject, waec_subject_grade))
        print(f"WAEC Result: {waec_wassce_result}")

        # grades validation
        if all(g in ["A", "B"] for g in waec_subject_grade):
            eligibility_criteria = (citizen_age < 18) and (citizen_score > 70)
            print(f"Candidate: {citizen_name}\nAge: {citizen_age}\nScore: {citizen_score}\nEligible: {eligibility_criteria}")
        else:
            print("Candidate does not meet the required WAEC/WASSCE grade criteria (must be all A or B).")
    else:
        print("Candidate does not meet basic citizenship, enrollment, or scholarship criteria.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Scholarship eligibility check complete")