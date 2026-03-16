# Continuously ask for numbers until invalid input.
# Display the highest number entered.

numbers = []

while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Program terminated.")
        break

if numbers:
    highest_number = max(numbers)
    print(f"The highest number is {highest_number}.")
else:
    print("No valid numbers were entered.")