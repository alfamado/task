# 12. ussd demo
print("Welcome to Madotech Communication")
dial_ussd = input("Enter the ussd code e.g *556#: ")
print("1. Airtime Balance\n 2. Recharge Airtime\n 3. Buy Data\n 4. Data Balance")
choose_option = int(input("select between 1 to 4"))
print(f"are you sure you want to proceed with {choose_option}")
print(f"{choose_option} Your balance is 10")
print("You are running low on airtime, press 2 to recharge or * to go back to the main menu")

