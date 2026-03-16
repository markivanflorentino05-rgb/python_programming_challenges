# Ask user to input fullname in incorrect casing, print in PascalCase.

full_name = input("Enter your fullname (incorrect casing): ")
# Split into words, capitalize each, then join
words = full_name.split()
pascal_name = "".join(word.capitalize() for word in words)
print(pascal_name)