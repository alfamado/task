# # 3. Tuple Operation using control flow
nigeria_state = tuple([
                        input("first nigeria state: ").title(),
                        input("Second nigeria state: ").title(),
                        input("Third nigeria state: ").title(),
                        input("fourth nigeria state: ").title(),
                        input("fifth nigeria state: ").title()
])
print(f"{nigeria_state[0]} {nigeria_state[-1]}")
if "Lagos" in nigeria_state:
    print("Lagos is part of Nigeria state listed")
else:
    print("Lagos is not part of Nigeria state listed")
print(len(nigeria_state))