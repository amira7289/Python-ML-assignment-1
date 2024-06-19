#a program in python that checks if a string starts with a given prefix
#or ends with a given suffix

str = "This is the python program"

# startswith()
print(str.startswith("This"))
print(str.startswith("This", 4, 10))
print(str.startswith("is", 8, 14))

print("\n")

# endswith
print(str.endswith("program"))
print(str.endswith("python", 2, 8))
print(str.endswith("program", 5, 8)