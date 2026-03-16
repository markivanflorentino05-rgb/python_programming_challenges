# Ask user to input fullname in incorrect casing, print with each character's case reversed.

full_name = input("Enter your fullname (incorrect casing): ")
reversed_case_name = full_name.swapcase()
print(reversed_case_name)