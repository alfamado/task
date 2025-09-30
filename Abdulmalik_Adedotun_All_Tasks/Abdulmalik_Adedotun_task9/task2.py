# Unique voter system using control flow
registered_voters = set()
for name in range(10):
    voter_full_name = input(f"voter full name {name+1}: ")
    if voter_full_name in registered_voters:
        print("Already registered")
    else:
        registered_voters.add(voter_full_name)
        print(registered_voters)
print(f"number of unique voters is {len(registered_voters)}")