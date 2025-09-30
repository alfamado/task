# 3. Tuple Operation
nigeria_state = tuple([
                        input("first nigeria state: "),
                        input("Second nigeria state: "),
                        input("Third nigeria state: "),
                        input("fourth nigeria state: "),
                        input("fifth nigeria state: ")
])
print(f"{nigeria_state[0]} {nigeria_state[-1]}")
print("Lagos" in nigeria_state)
print(len(nigeria_state))