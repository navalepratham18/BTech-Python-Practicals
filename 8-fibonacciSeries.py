
# to find Nth num
n = int(input("Enter the value of N: "))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f"The {n}th Fibonacci number is:", fibonacci(n))


# to find till Nth num
n = int(input("\nEnter the value of n: "))
a = 0
b = 1
print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a = b
    b = a + b