numbers = []
for i in range(10):
    numbers.append(float(input(f"Enter number {i+1}: ")))

print("Numbers without duplicates:")
for num in numbers:
    if numbers.count(num) == 1:
        print(num)