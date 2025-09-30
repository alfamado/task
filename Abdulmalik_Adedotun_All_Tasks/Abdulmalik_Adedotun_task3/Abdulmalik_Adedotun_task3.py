''' 
# 1. Display string in uppercase
name = "Abdulmalik Adedotun"
print(name.upper())

# 2. First and Last Character
course = "python"
print(course[0],course[-1])

# 3. Input and Print
ask_name = input("What is your name: ")
print("Hello,!","where is the user input")
print(f"It is here: {ask_name}")

# 4. Count number of character
count_character = "Abdulmalik Adedotun"
print(count_character.index("n"))

# 5. Replacing a word
text = "Hello World"
print(text.replace("World", "Python"))

# 6. Checking substring without case insensitive
character = "I love coding with python"
print("Python" in character)
search = input("input a word: ")
print("Search word: ", "python" in search.lower())

# 7. reverse a string without[::-1]
word = "Abdulmalik"
reversed_string = "".join(reversed(word))
print(reversed_string)

# 8. Removing spaces
school = "  Federal Science and Technical College  "
print(school.strip())

# 9. counting and printing
count_vowel = "I love programming"
counts = count_vowel.lower()
print(counts.count('a') + counts.count('e') + counts.count('i') + counts.count('o') + counts.count('u') + counts.count('A') + counts.count('E') + counts.count('I') + counts.count('O') + counts.count('U'))

# 10. type conversion
char = "1234"
print(int(char) * 2)

# 11. Spliting String
fruits = "apple,banana,orange"
print(fruits.split(",", 2))

# 12. printing an input in new line
sentence = input("Enter a sentence: ")
split_line = "\n".join(sentence.split())
print(split_line)

# 13. Replacing a special character with another 
replacement = "I love football"
print(replacement.replace(" ", "_"))

# 14. counting a number of times a letter appears
letter = "Banana"
print(letter.count('a'))

# 15. checking if a string start in a sentence
website = "https://livescores.com"
print(website.startswith("https://"))
'''

count_vowel = "I love programming"
counts = count_vowel.lower()
print(counts.count('a') + counts.count('e') + counts.count('i') + counts.count('o') + counts.count('u') + counts.count('A') + counts.count('E') + counts.count('I') + counts.count('O') + counts.count('U'))