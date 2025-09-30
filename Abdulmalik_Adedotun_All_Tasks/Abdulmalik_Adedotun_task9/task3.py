# 12. ussd demo using control flow
print("Welcome to Madotech Communication")
dial_ussd = input("Enter the ussd code e.g *556#: ")
if dial_ussd == "*556#":
    print("1. Airtime Balance\n 2. Recharge Airtime\n 3. Buy Data\n 4. Data Balance")
    choose_option = int(input("select between 1 to 4: "))
    if choose_option == 1:
        balance = 97.50
        print(f"your balance is ₦{balance}K")
    elif choose_option == 2:
        recharge_airtime = int(input("How much do you want to recharge: "))
        print(f"Dear Customer, your recharge of ₦{recharge_airtime} is successful.")
    elif choose_option == 3:
        print("1. Daily Plan\n2. Weekly plan\n3. Monthly\n 4.Unlimited")
        choose_plan = input("Pick a plan: ")
        if choose_plan == 1:
            print("You have successfully activate a daily plan")
        elif choose_plan == 2:
            print("You have successfully activate a weekly plan")
        elif choose_plan == 3:
            print("You have successfully activate a monthly plan")
        elif choose_plan == 4:
            print("You have successfully activate the unlimited plan")
        else:
            print("Wrong number, Try again!")
    elif choose_option == 4:
        data_balance = 1.56
        type = ["Daily", "Weekly", "Monthly", "Unlimited"]
        print(f"Your data balance {type[2]}: {data_balance}gb")
    else:
        print("Wrong number, choose between 1 to 4 to buy a plan")
else:
    print("you've dialled a wrong ussd, dial *556#")