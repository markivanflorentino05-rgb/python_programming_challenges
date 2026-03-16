# Ask user to input fullname in incorrect casing, print in proper casing.

full_name = input("Enter your fullname (incorrect casing): ")
proper_name = full_name.title()
print(proper_name)