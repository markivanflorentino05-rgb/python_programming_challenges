seen_numbers = []
while True:
    user_input = input("Enter a number (or any letter to stop): ")
    try:
        num = float(user_input)
        if num in seen_numbers:
            print("Duplicate")
        else:
            print("Unique")
            seen_numbers.append(num)
    except ValueError:
        break