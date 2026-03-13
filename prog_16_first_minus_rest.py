numbers = []
for i in range(10):
    numbers.append(float(input(f"Enter number {i+1}: ")))

result = numbers[0]
for num in numbers[1:]:
    result -= num
print(result)