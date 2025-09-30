word = input("Enter a word: ")
print(len(word))
if word == word.lower():
    print("word is lower")
elif word == word.upper():
    print("word is upper")
elif word == word.title():
    print("word is title")
else:
    print("not applicable")

print(word[::-1])
