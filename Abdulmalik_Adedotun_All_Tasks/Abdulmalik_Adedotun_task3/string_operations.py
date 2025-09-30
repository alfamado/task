name = "Abdulmalik Adedotun"
print(name.upper())

sentence = "Python is dynamic"
print(sentence.title())

text = "    Abuja    "
print(text.strip())

message = "I love Java"
print(message.replace("Java", "Python"))

text = "Hello ABEOKUTA"
print(text.swapcase())

text = "Nigeria   "
print(text.rstrip())

fruits = "mango orange banana"
print(fruits.split())

text = "one,two,three,four"
print(text.rsplit(",", 2))

lines = "Line 1\nLine 2\Line 3"
print(lines.splitlines())

words = ["I", "Love", "Python"]
print(" ".join(words))

text = "Python"
print(text.center(20, "-"))

text = "Python"
print(text.ljust(10, "*"))

text = "Python"
print(text.rjust(10, "*"))

num = "42"
print(num.zfill(5))

print("Lagos".isalpha())
print("Lagos123".isalpha())

print("12345".isdigit())
print("123a".isdigit())

print("Python3".isalnum())
print("Python 3".isalnum())