# Practical Lab - 23/09/24 - 01:30 to 3:30

print("Prime Number Between 1 to 100 : ", end="")
for number in range(2, 101):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number, end=" , ")
