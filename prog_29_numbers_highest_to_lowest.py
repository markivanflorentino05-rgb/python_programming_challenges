# Continuously ask for numbers until invalid input.
# Display all numbers sorted from highest to lowest.

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
    numbers.sort(reverse=True)
    print("Numbers from highest to lowest:", numbers)
else:
    print("No valid numbers were entered.")