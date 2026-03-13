numbers = []
for i in range(10):
    numbers.append(float(input(f"Enter number {i+1}: ")))

seen = []
print("Numbers (first entry only):")
for num in numbers:
    if num not in seen:
        print(num)
        seen.append(num)