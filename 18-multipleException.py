try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)

    list_example = [1, 2, 3]
    print("List item:", list_example[5])  

except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except IndexError:
    print("Index out of range error!")
except Exception as e:
    print("An unexpected error occurred:", e)
