# 4. Tuple Unpacking
user = [
        input("Enter your First Name: "),
        input("How old are you: "),
        input("What is your favourite color: "),
        input("Your Home Town: ")
]
profile = tuple(user)
print(profile)

name, age, favourite_color, home_town = profile[0], profile[1], profile[2], profile[3]
print(f"Name\t Age\t Favoure_Color\tHome_Town")
print(f"{name}\t {age}\t {favourite_color}\t        {home_town}")