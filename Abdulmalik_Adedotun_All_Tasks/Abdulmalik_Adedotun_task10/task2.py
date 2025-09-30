# 12. ussd demo using control flow and error handling
print("Welcome to Madotech Communication")
while True:
    try:
        dial_ussd = input("Enter the ussd code e.g *556#: ")
        if dial_ussd != "*556#":
            print("Wrong ussd, try again")
            continue
        print("1. Airtime Balance\n 2. Recharge Airtime\n 3. Buy Data\n 4. Data Balance\n 5. Exit")
        choose_option = int(input("select between 1 to 5: "))
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
        elif choose_option == 5:
            print("Existing ussd")
            break
        else:
            print("Wrong number, choose between 1 to 4 to buy a plan")
    except ValueError:
        print("Invalid input, please enter a number")
    finally:
        print("ussd check completed")