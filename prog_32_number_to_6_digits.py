# Ask user to input a number (0-1000), print it in 6-digit format with leading zeros.

number_input = input("Enter a number (0-1000): ")
try:
    number = int(number_input)
    if 0 <= number <= 1000:
        formatted_number = f"{number:06d}"
        print(formatted_number)
    else:
        print("Number out of range. Please enter between 0 and 1000.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")