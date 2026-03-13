even_count = 0
for i in range(10):
    if int(input(f"Enter number {i+1}: ")) % 2 == 0:
        even_count += 1
print(even_count)