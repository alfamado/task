# Day and Activities Pairing
days_in_a_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
activity = input("What do you do in three specific days: ").split(",")
specific_activities = {days_in_a_week: activity for days_in_a_week, activity in zip(days_in_a_week, activity)}
print(specific_activities)