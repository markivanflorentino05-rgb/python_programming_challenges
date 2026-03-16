# Continuously ask for numbers until invalid input.
# Display the average of all entered numbers.

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
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    print(f"The average is {average:.2f}.")
else:
    print("No valid numbers were entered.")