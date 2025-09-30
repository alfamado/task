# Nigeria states using loop and error control
while True:
    try:
        nigeria_state = tuple([
            input("First Nigeria state: ").title(),
            input("Second Nigeria state: ").title(),
            input("Third Nigeria state: ").title(),
            input("Fourth Nigeria state: ").title(),
            input("Fifth Nigeria state: ").title()
        ])

        print(f"\nFirst state: {nigeria_state[0]} | Last state: {nigeria_state[-1]}")

        if "Lagos" in nigeria_state:
            print("Lagos is part of Nigeria states listed")
        else:
            print("Lagos is not part of Nigeria states listed")

        print(f"Total number of states entered: {len(nigeria_state)}")
        break # valid input, exit loop

    except Exception as e:
        print(f"Error: {e}. Please try again.")
    finally:
        print("Nigeria states input check complete")