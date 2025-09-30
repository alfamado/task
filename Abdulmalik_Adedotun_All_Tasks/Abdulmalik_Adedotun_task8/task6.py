candidate_name = input("Enter your name: ").title()
candidate_age = int(input("Enter your age: "))
uni_choice = input("Did you choode UNILAG as your first choice (Yes/No): ").lower()
utme_score = int(input("Enter your utme score: "))
result_sitting = input("Did you obtain your o_level result at first sitting (Yes/No): ").lower()
o_level_subject = input("Enter five O'Level subject relevent to course applied including english and math (seperate it using comma): ").title().split(",")
o_level_grade = input("Enter grade with a minimum grade of C6 with result obtained at one sitting: ").upper().split(",")
o_level_result = dict(zip(o_level_subject, o_level_grade))
print(f"Name: {candidate_name}\nAge: {candidate_age}\nFirst_Choice: {uni_choice}\nUtme SCore: {utme_score}\nOne Sitting: {result_sitting}\nWaec Result: {o_level_result}")
post_utme_eligibility = candidate_age >= 16 and utme_score >= 200 and result_sitting == "yes"
print(f"Student Eligibile for post utme: {post_utme_eligibility}")
post_utme_score = int(input("post utme score out of 100: "))
candidate_status = post_utme_eligibility == True and post_utme_score >= 40
print(f"You have been offered admission: {candidate_status}")