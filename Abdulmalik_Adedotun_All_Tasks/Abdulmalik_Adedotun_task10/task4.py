# Registered voters using loop and error handling
registered_voters = set()

while True:
    try:
        for i in range(10):
            voter_full_name = input(f"Voter full name {i+1}: ").title()

            if voter_full_name in registered_voters:
                print("Already registered")
            else:
                registered_voters.add(voter_full_name)
                print(f"Registered voters so far: {registered_voters}")

        print(f"\nRegistration complete. Number of unique voters: {len(registered_voters)}")
        break # exit loop after successful registration

    except Exception as e:
        print(f"Error occurred: {e}. Try again.")
    finally:
        print("Voter registration cycle complete")