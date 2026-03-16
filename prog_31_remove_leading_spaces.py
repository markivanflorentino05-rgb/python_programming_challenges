# Ask user to input fullname with leading spaces, then print without them.

full_name = input("Enter your fullname (with leading spaces): ")
trimmed_name = full_name.lstrip()
print(trimmed_name)