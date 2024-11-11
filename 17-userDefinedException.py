class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("The number is negative.")
    else:
        print("The number is positive.")

try:
    check_positive(-10)
except NegativeNumberError as e:
    print(e)
