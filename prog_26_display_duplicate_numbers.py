# Ask user to input 10 numbers, then display all numbers that have duplicates.

entered_numbers = []

for i in range(10):
    user_input = input(f"Enter number {i + 1}: ")
    try:
        number = int(user_input)
        entered_numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")
        # Re‑ask for the same index if input is invalid
        while True:
            user_input = input(f"Enter number {i + 1} again: ")
            try:
                number = int(user_input)
                entered_numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

# Find duplicate numbers
counts = {}
for num in entered_numbers:
    counts[num] = counts.get(num, 0) + 1

duplicate_numbers = [num for num, count in counts.items() if count > 1]

if duplicate_numbers:
    print("Numbers that have duplicates:", duplicate_numbers)
else:
    print("No duplicate numbers found.")