# Ask user to input fullname in incorrect casing, print in snake_case.

full_name = input("Enter your fullname (incorrect casing): ")
# Convert to lowercase and replace spaces with underscores
snake_name = full_name.lower().replace(" ", "_")
print(snake_name)