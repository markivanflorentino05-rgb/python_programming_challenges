num1 = int(input("Enter start: "))
num2 = int(input("Enter end: "))

start = min(num1, num2)
end = max(num1, num2)

for i in range(start + 1, end):
    print(i)