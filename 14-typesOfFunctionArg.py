
def calculate_area(length, width):
    return length * width

def print_student_info(name, age, grade):
    print(f"Student Name: {name}, Age: {age}, Grade: {grade}")

def greet(name="Nooob"):
    print(f"Hello, {name}!")

def add_numbers(*args):
    return sum(args)

print("Area:", calculate_area(5, 10))  
print_student_info("iiiaamnooob",2, 1) 
print_student_info(age=16, grade="10th", name="NooB") 
greet()  
print("Sum:", add_numbers(1, 2, 3, 4, 5))  
