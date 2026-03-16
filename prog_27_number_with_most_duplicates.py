# Continuously ask for numbers until invalid input.
# Display the number with the most duplicates (highest frequency).

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
    # Count frequencies
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    # Find the number with the highest frequency
    most_frequent_number = max(frequency, key=lambda n: frequency[n])
    highest_count = frequency[most_frequent_number]

    print(f"The number with the most duplicates is {most_frequent_number} "
          f"(appears {highest_count} times).")
else:
    print("No valid numbers were entered.")