import random

numbers = [random.randint(1, 100) for i in range(20)]

print("Generated List:", numbers)

target = int(input("Enter a number to search for: "))

found = False
index = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        index = i
        found = True
        break

if found:
    print(f"Number {target} found at index {index}")
else:
    print(f"Number {target} not found.")
