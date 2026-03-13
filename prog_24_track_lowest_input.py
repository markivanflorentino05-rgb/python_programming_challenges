lowest = None
while True:
    user_input = input("Enter a number (or any letter to stop): ")
    try:
        num = float(user_input)
        if lowest is None or num < lowest:
            lowest = num
    except ValueError:
        break

if lowest is not None:
    print(f"Lowest number: {lowest}")