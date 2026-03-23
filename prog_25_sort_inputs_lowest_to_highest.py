numbers = []
while True:
    user_input = input("Enter a number (or any letter to stop): ")
    try:
        numbers.append(float(user_input))
    except ValueError:
        break

numbers.sort()
print("Sorted numbers (Lowest to Highest):")
print(numbers)