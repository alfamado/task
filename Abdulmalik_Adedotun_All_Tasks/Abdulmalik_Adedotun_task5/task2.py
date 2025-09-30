# 2. Tuple and Input
friends = [
            input("First friend: "),
            input("Second friend: "),
            input("Third friend: "),
            input("Fourth friend: "),
            input("Fifth friend: ")
]
print(tuple(friends))
best_friend = tuple(friends)
print(best_friend[::-1])